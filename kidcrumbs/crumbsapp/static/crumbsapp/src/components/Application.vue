<template>
    <div id="mainApp" class="bg_aux">
        <section class="">
            <transition name="fade" mode="out-in">
            <router-view></router-view>
            </transition>
        </section>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from "vuex";
export default{
    name : "MainApplication",
}
</script>
<style lang="stylus" >
</style>
