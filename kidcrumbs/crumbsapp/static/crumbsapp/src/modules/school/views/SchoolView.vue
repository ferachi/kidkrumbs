<template>
    <div id="SchoolView" >
        <transition name="fade-left" mode="out-in">
            <router-view></router-view>
        </transition>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "SchoolView",
}
</script>
<style lang="stylus">
</style>
