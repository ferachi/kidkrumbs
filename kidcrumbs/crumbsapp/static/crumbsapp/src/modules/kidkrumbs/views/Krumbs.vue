<template>
    <div id="krumbs">
        <div class="d-flex">
            <section class="col-auto p-0">
                <nav class="d-none d-lg-block bigscreens-menu border-right border_2">
                    <sitemenu> </sitemenu>
                </nav>
            </section>
            <section class="col p-0 app-content">
                <transition name="fade" mode="out-in">
                    <router-view></router-view>
                </transition>
            </section>
            <section class="d-lg-none mobile-menu">
                <nav class="border-top border_2">
                    <sitemenu></sitemenu>
                </nav>
            </section>
        <!--  COMMENTED OUT SECTION
            UNCOMMENT IF MOBILE MENU ABOVE GIVES AN ISSUE
        <section v-if="false">
            <nav class="d-lg-none mobile-menu">
                <siteMenu></siteMenu>
            </nav>
        </section>
        -->
        </div>
    </div>
</template>
<script>
import menu from "../../../components/menu.vue";
export default{
    name : 'krumbs',
    components:{
        sitemenu : menu
    }
}
</script>
<style lang="stylus">
#krumbs
    .app-content
        min-height 98vh
        max-height 100vh
        overflow-y hidden
        padding-bottom 100px
    .mobile-menu
        position absolute
        bottom 0
        min-width 100vw
</style>

