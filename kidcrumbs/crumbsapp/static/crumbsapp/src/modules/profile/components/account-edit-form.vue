<template>
    <div id="accountEdit">
        <div class="d-flex flex-wrap justify-content-between align-items-center">
            <div class="col-12 col-lg-8 col-xl-6  px-0">
                <md-field class="mb-0">
                    <label>Username</label>
                    <md-input name="username" v-validate="{max:60, regex:/^(?!.*[^a-zA-Z0-9|^\s_@]).*$/, uniquename:true}"
                        v-model="profile._username" ></md-input>
                </md-field>
                <span v-show="errors.has('username')" class="text-danger">{{ errors.first('username') }}</span>
            </div>
            <div class="col-12 col-lg-auto px-0 pt-3">
                <md-button class="md-secondary m-0" @click="show">Change password</md-button>
            </div>
        </div>
        <section>
            <modal ref="modal" :enable-mobile-fullscreen="false" :modal-theme="getTheme" :overlay-theme="getTheme"
                   :blocking="true" :icon="icon">
            <div v-if="!hidePasswordForm">
                <change-password @password-change="passwordChanged"></change-password>
            </div>
            <div v-else>
                <h4 class="color_4">Password changed successfully</h4>
            </div>
            </modal>
        </section>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import avatar from '../../../components/avatar.vue';
import { SweetModal } from 'sweet-modal-vue';
import changePassword from './change-password';
export default{
    name : "accountEdit",
    props : ['profile'],
    inject : ['$validator'],
    computed :{
        ...mapGetters(['getTheme'])
    },
    components : {
        changePassword,
        modal : SweetModal
    },
    data(){
        return {
            icon:'',
            hidePasswordForm:false
        }
    },
    methods : {
        show () {
            this.hidePasswordForm = false;
            this.icon = '';
            this.$refs.modal.open(); 
        },
        hide () {
            this.$refs.modal.close(); 
        },
        passwordChanged(){
            this.hidePasswordForm = true;
            this.icon = 'success';
            // this.hide();
        }
        
    }
}
</script>
<style lang="stylus"></style>
