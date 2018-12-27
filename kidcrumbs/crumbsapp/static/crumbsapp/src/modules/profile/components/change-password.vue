<template>
    <div id="accountEdit">
        <h4 class="font-weight-bold">Change Password</h4>
        <form id="changePasswordForm" @submit.prevent="validateBeforeSubmit" novalidate>
            <div class="form-group">
                <md-field>
                    <label>Old Password</label>
                    <md-input v-model="password" data-vv-name="password" v-validate="{min:8,
                        max:20,regex:/^(?!.*[^a-zA-Z0-9|^\s,@_-]).*$/, required : true, passwordcheck:true}"  type="password" name="password"></md-input>
                </md-field>
                <span v-show="errors.has('password')" class="text-danger">{{ errors.first('password') }}</span>
            </div>
            <div class="form-group">
                <md-field>
                    <label>New Password</label>
                    <md-input v-model="newPassword" v-validate="{min:8, max:20, regex:/^(?!.*[^a-zA-Z0-9|^\s,@_-]).*$/,required : true}"  type="password" name="newPassword" data-vv-as="new
                        password"></md-input>
                </md-field>
                <span v-show="errors.has('newPassword')" class="text-danger">{{ errors.first('newPassword') }}</span>
            </div>
            <div class="form-group">
                <md-field>
                    <label>Confirm Password</label>
                    <md-input v-model="confirmPassword" v-validate="{min:8, max:20, regex:/^(?!.*[^a-zA-Z0-9|^\s,@_-]).*$/,required : true, confirmed:newPassword}"  type="password" data-vv-as="password"name="confirmPassword"></md-input>
                </md-field>
                <span v-show="errors.has('confirmPassword')" class="text-danger">{{ errors.first('confirmPassword') }}</span>
            </div>
            <md-button type="submit" class="md-secondary m-0" >Change password</md-button>
        </form>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import avatar from '../../../components/avatar.vue';
import { SweetModal } from 'sweet-modal-vue';

export default{
    name : "accountEdit",
    created(){
    },
    data(){
        return {
            username:'',
            password :'',
            newPassword :'',
            confirmPassword :'',
        }
    },
    methods: {
        ...mapActions('person',['changePassword']),
        validateBeforeSubmit(){
            this.$validator.validateAll().then(result =>{
                if(result){ 
                    this.changePassword(this.newPassword).then(profile => {
                        changePasswordForm.reset();
                        this.$emit('password-change');
                    });
                }
                else{
                    console.log(this.errors, this.fields)
                }
            })
        }
    }
}
</script>
<style lang="stylus"></style>
