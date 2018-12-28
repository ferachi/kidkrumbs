<template>
    <div id="More" class="" >
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
        <section id="moreContent" class="p-3 bg_0">
            <more-menu></more-menu>
        </section>
        </page>
    </div>
</template>
<script>
import transicion from '../../../components/transicion.vue';
import avatar from '../../../components/avatar.vue';
import page from '../../../components/page.vue';
import moreMenu from '../components/menu.vue';
import pageHeader from '../../../components/pageHeader.vue';
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "More",
    created(){
    },
    components:{
        page,
        pageHeader,
        transicion,
        avatar,
        moreMenu
    },
    computed :{
        ...mapGetters('profile', { profile:'getProfile' }),
    },
    data(){
        return {
            isLoading  : true,
        }
    },
    methods : {
        ...mapActions('auth', ['logout']),
        signOut(){
            this.logout().then( response => {
                this.$router.push({name : 'notAllowed'});   
            });
        }
    }
}
</script>
<style lang="stylus">
#More
    #moreContent
        min-height 90vh
        padding-bottom 100px !important
</style>
