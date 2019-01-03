<template>
    <div id="login" class="bg_aux px-2">
        <div class="login d-flex justify-content-center lign-items-center">
            <div class="col-lg-4 col-xl-3 bg_0 h-75 p-4" >
                <form @submit.prevent="validateBeforeSubmit" novalidate>
                    <h4 class="font-weight-bold text-center ">Login</h4>
                    <div class="form-group py-2">
                        <label>Username</label>
                        <input class="form-control form-control-sm" name="username" v-validate="{max:60, regex:/^(?!.*[^a-zA-Z0-9|^\s_@]).*$/}"
                                                                                    v-model="user.username" />
                        <span v-show="errors.has('username')" class="text-danger">{{ errors.first('username') }}</span>
                    </div>
                    <div class="form-group py-2">
                        <label>password</label>
                        <input class="form-control form-control-sm" v-model="user.password" data-vv-name="password" v-validate="{min:8,
                        max:20,regex:/^(?!.*[^a-zA-Z0-9|^\s,@_-]).*$/, required : true, }"  type="password"
                                                                                            name="password" />
                        <span v-show="errors.has('password')" class="text-danger">{{ errors.first('password') }}</span>
                    </div>
                    <div>
                        <button class="btn btn-primary btn-block"> Login </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : 'Login',
    data(){
        return {
            user:{username:'', password:''},
            error:'',
            hasError : false
        }
    },
    methods : {
        ...mapActions('auth', ['login']),
        validateBeforeSubmit(){
            this.$validator.validateAll().then(result =>{
                if(result){
                    this.login(this.user).then(profile => {
                        this.hasError = false; 
                        this.$router.push({name : 'profile'})
                    })
                    .catch(err => {
                        this.hasError = true;
                        console.dir(err);
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
#login
    .login
        height 85vh
</style>

