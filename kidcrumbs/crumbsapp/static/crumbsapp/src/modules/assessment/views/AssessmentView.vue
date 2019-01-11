<template>
    <div id="assessmentView" >
        <page-header class="border-bottom border_1 primary-bg" >
            <div slot="pageTitle" class="d-flex align-items-center mb-2">
                <div class="col-auto px-1">
                    <avatar :image="profile.avatar" :alt="profile.username" > </avatar>
                </div>
            <div class="col px-2">
                <h5 class="color_white m-0 text-capitalize">{{profile.last_name}} {{profile.first_name}}</h5>
            </div>
            </div>
            <div slot="pageMenu" >
                <div class="d-flex">
                    <div class="col-auto px-2 clickable" @click="signOut"><span class="fas fa-sign-out-alt fa-fw color_white"></span></div>
                </div>
            </div>
        </page-header>
        <transition name="fade" mode="out-in">
            <router-view></router-view>
        </transition>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import pageHeader from '../../../components/pageHeader.vue';
import avatar from '../../../components/avatar.vue';
export default{
    name : 'assessmentView',
    computed : {
        ...mapGetters('profile', {profile : 'getProfile'}),
    },
    components : {
        pageHeader,
        avatar
    },
    methods:{
        ...mapActions('auth', ['logout']),
        signOut(){
            this.logout().then( response => {
                this.$router.push({name : 'app'});   
            });
        }
    }
}
</script>
<style lang='stylus'>
</style>

