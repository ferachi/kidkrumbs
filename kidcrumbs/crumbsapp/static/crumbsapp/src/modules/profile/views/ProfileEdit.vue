<template>
    <div id="ProfileEdit" class="px-xl-5 px-lg-3">
        <form @submit.prevent="validateBeforeSubmit" novalidate>
            <section class="pb-3">
                <h4>Basic Details</h4>
                <hr>
                <basic-edit :profile="profile"></basic-edit>
            </section>
            <section class="py-3">
                <h4>Account Details</h4>
                <hr>
                <account-edit :profile="profile"></account-edit>
            </section>
            <div class="clearfix py-3">
                <md-button type="submit" :disabled="isNotValid" class="md-primary md-raised float-right">ok with edit</md-button>
            </div>
        </form>
        <section class="edit-info text-center pt-4">
        <hr>
            <h6 class="primary-color text-uppercase">Information</h6>   
            <p>This page is primarily exhibited to edit your basic details. If you intend to edit more than what is presented
            here, please consult your schools' <strong class="primary-color">Administration</strong>.</p>
            <hr>
        </section>
        <section>
            <modal ref="modal" :enable-mobile-fullscreen="false" :modal-theme="getTheme" :overlay-theme="getTheme"
                   :blocking="true" :icon="icon">
            <div v-if="icon=='success'">
                <h5 class="color_4">Details successfully updated</h5>
            </div>
            <div v-else>
                <h5 class="color_4">Some error occured please verify your details.</h5>
            </div>
            </modal>
        </section>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import basicEdit from '../components/basic-edit-form.vue';
import accountEdit from '../components/account-edit-form.vue';
import {Validator} from 'vee-validate';
import { SweetModal } from 'sweet-modal-vue';
import http from '../../../http';

export default{
    name : "ProfileEdit",
    created(){
        this.profileCopy = _.cloneDeep(this.profile);

        let user = this.profile.user;
        const isUnique = (value) => {
            return http.post('/api/people/check_username/', { user:user,newUsername: value }).then((response) => {
                // Notice that we return an object containing both a valid property and a data property.
                return {
                    valid: response.data.valid,
                    data: {
                        message: response.data.message
                    }
                };
            });
        };



        const isOldPassword = (value) => {
            let data = {user, password : value};
            return http.post('/api/people/validate_password/', data).then((response) => {
                // Notice that we return an object containing both a valid property and a data property.
                return {
                    valid: response.data.valid,
                    data: {
                        message: response.data.message
                    }
                };
            });
        };

        Validator.extend('uniquename', {
            validate: isUnique,
            getMessage: (field, params, data) => {
                return data.message;
            }
        });

        Validator.extend('passwordcheck', {
            validate: isOldPassword,
            getMessage: (field, params, data) => {
                return data.message;
            }
        });
    },
    components :{
        basicEdit,
        accountEdit,
        modal: SweetModal
    },
    computed : {
        ...mapGetters('person', {'profile' : 'getProfile'}),
        ...mapGetters(['getTheme']),
        isFormDirty(){
            return _.some(this.fields, field => field.pristine)
        },
        isFormPristine(){
            return _.every(this.fields, field => field.pristine)
        },
        hasErrors(){
            return this.errors.items.length > 0 
        },
        hasEdit(){
            let diff = _.differenceWith([this.profile], [this.profileCopy], _.isEqual);
            return !_.isEmpty(diff);
        },
        isNotValid(){
            return !this.hasEdit || (this.isFormDirty && this.hasErrors) 
        }
    },

    data(){
        return {
            icon : '',
            profileCopy : {}
        }
    },
    methods : {
        ...mapActions('person', ['updateProfile']),
        validateBeforeSubmit(){
            this.$validator.validateAll().then(result =>{
                if(result){
                    this.updateProfile().then(profile => {
                        this.icon = 'success';
                        this.profileCopy = _.cloneDeep(this.profile);
                        this.$refs.modal.open(); 
                    })
                    .catch(err => {
                        this.icon = 'error';
                        this.$refs.modal.open(); 
                    })

                }
                else{
                    console.log(this.errors, this.fields)
                    alert('Correct them errors!');
                }
            })
        }
    }
}
</script>
<style lang="stylus">
</style>
