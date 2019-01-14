<template>
    <div id="siteHeader"  class="py-4 py-lg-2 bg_0" >
        <section class="header-content d-flex align-items-center h-100">
            <div class="d-flex col px-0">
                <div class="col px-2">
                    <h5 class="m-0 primary-color font-weight-bold text-uppercase">KidCrumbs</h5>
                </div>
                <div class="col-auto px-2">
                    <div class="d-none d-md-block">
                        <div class="d-flex align-items-center">
                            <div class="col-auto text-center clickable" v-for="menu in menus":key="menu.name"
                            v-if="menu.bigDisplay" @click="menuClick(menu)">
                                <div v-html="menu.icon" :class="{'primary-color' : menu.isActive}"></div>
                                <div><small class="color_3 text-lowercase" :class="{'primary-color' : menu.isActive}">{{menu.title}}</small></div>
                            </div>
                        </div>
                    </div>
                    <div class="d-md-none">
                        <div class="d-inline-block clickable" @click="show">
                            <span class="fas fa-fw fa-bars"></span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section>
            <modal ref="modal" :enable-mobile-fullscreen="true" width="100%" class="full-height" :modal-theme="theme" :overlay-theme="theme" >
                <div>
                    <section class="mobile-menu d-flex align-items-center">
                        <div class="col text-center">
                        <div v-for="menu in menus":key="menu.name" class="my-3">
                            <div @click="mobileMenuClick(menu)"><h3 class="color_3 text-capitalize" :class="{'primary-color' :menu.isActive}">{{menu.title}}</h3></div>
                        </div>
                        </div>
                    </section>
                    <section class="text-center">
                        <small class="m-0 color_3">created by  <span class="fas fa-frog fa-fw primary-color"></span>
                            <span class="color_4">Fercube</span></small>
                    </section>
                </div>
            </modal>
        </section>
    </div>
</template>
<script>
import {mapGetters, mapMutations, mapActions} from 'vuex';
import { SweetModal } from 'sweet-modal-vue';

export default{
    name : 'siteHeader',
    created(){
        this.watchRoute(this.$route);
    },
    computed : {
        ...mapGetters({theme : 'getTheme'}),
        ...mapGetters('auth' ,['isAuthenticated']),
        ...mapGetters('home' ,['getMenus']),
        menus(){
            if(this.isAuthenticated)
                return _.filter(this.getMenus,menu => menu.name != 'login')
            else
                return _.filter(this.getMenus,menu => menu.name != 'crumbs')
        }
    },
    components:{
        modal:SweetModal
    },
    methods : {
        ...mapActions('home', ['activateMenu']),
        show(){
            this.$refs.modal.open();
        },
        menuClick(menu){
            this.$router.push({name:menu.link});
        },
        mobileMenuClick(menu){
            this.$router.push({name:menu.link});
            setTimeout(() => {
                this.$refs.modal.close();
            },300);
        },
        ...mapMutations("page", ["setPage"]),
        watchRoute(_route){

            // find the parent link/route
            let route = _route.matched.find( record => {
                return record.meta.krumbMenu
            });

            // activate the menu if it exist
            if(route){
                // set the page
                this.setPage(route.meta.page);

                // activate menu
                let menu = this.menus.find( menu => menu.link == route.meta.page);
                this.activateMenu(menu);
            }
        }
    },
    data(){
        return {
        }
    },
    watch:{
        '$route'(newVal){
            this.watchRoute(newVal);
        }
    }
}
</script>
<style lang="stylus">
#siteHeader
    height 7vh
    .full-height
        .sweet-modal
            height 100% !important
    .mobile-menu
        height 75vh
</style>


