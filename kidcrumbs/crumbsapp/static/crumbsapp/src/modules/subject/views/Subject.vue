<template>
    <div id="subject">
        <page>
        <section slot="header">
            <page-header class="border-bottom border_1 primary-bg" >
                <div slot="pageTitle" class="d-flex align-items-center mb-2">
                    <div class="col-auto px-1">
                        <avatar :image="profile.avatar" :alt="profile.username" > </avatar>
                    </div>
                    <div class="col px-2">
                        <h5 class="color_white m-0 text-capitalize">{{profile.last_name}} {{profile.first_name}}</h5>
                    </div>
                </div>
                <div slot="pageMenu">
                    <div class="d-flex">
                        <div class="col-auto px-2 clickable" @click="signOut"><span class="fas fa-sign-out-alt fa-fw color_white"></span></div>
                    </div>
                </div>
            </page-header>
        </section>
        <section id="subjectContent" class="p-4 bg_0">
            <router-view></router-view>
        </section>
        </page>
    </div>
</template>
<script>
import avatar from '../../../components/avatar.vue';
import page from '../../../components/page.vue';
import pageHeader from '../../../components/pageHeader.vue';
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "Subject",
    components:{
        page,
        pageHeader,
        avatar,
    },
    computed :{
        ...mapGetters('profile', { profile:'getProfile' }),
    },
    methods : {
        ...mapActions('auth', ['logout']),
        signOut(){
            this.logout().then( response => {
                this.$router.push({name : 'app'});   
            });
        }
    }

}
</script>
<style lang="stylus">
#subject
    #subjectContent
        min-height 90vh
        padding-bottom 100px !important

</style>
