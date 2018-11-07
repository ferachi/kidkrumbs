<template>
    <div id="mainApp" class="bg_0">
        <div class="d-flex">
            <section class="col-auto p-0">
                <nav class="d-none d-lg-block bigscreens-menu border-right border_2">
                    <siteMenu> </siteMenu>
                </nav>
            </section>
            <section class="col d-flex justify-content-center p-0 app-content">
                <div class="col-xl-8 col px-0">
                    <router-view></router-view>
                </div>
            </section>
            <section class="d-lg-none mobile-menu">
                <nav class="border-top border_2">
                    <siteMenu></siteMenu>
                </nav>
            </section>
        </div>
        <!--  COMMENTED OUT SECTION
            UNCOMMENT IF MOBILE MENU ABOVE GIVES AN ISSUE
        <section v-if="false">
            <nav class="d-lg-none mobile-menu">
                <siteMenu></siteMenu>
            </nav>
        </section>
        -->
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from "vuex";
import menu from "./menu.vue";
export default{
    name : "MainApplication",
    components:{
        siteMenu : menu
    },
}
</script>
<style lang="stylus" >
#mainApp
    .app-content
        min-height 98vh
        max-height 98vh
        overflow-y auto
        padding-bottom 30px
    .mobile-menu
        position absolute
        bottom 0
        min-width 100vw

</style>
