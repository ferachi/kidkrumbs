<template>
    <div id="kidkrumbs">
        <section class="site-header">
            <site-header></site-header>
        </section>
        <section class="site-body bg_0">
            <transition name="fade" mode="out-in">
            <router-view></router-view>
            </transition>
        </section>
        <section class="bg_0 site-footer py-3 d-none d-lg-block">
            <footer-base></footer-base>
        </section>
    </div>
</template>
<script>
import siteHeader from '../components/site-header.vue';
import footerBase from '../components/footer.vue';
export default{
    name : 'KidKrumbs',
    components : {
        siteHeader,
        footerBase
    }
}
</script>
<style lang="stylus">
#kidkrumbs
    .site-body
        height 85vh
    .site-footer
        height 8vh
</style>


