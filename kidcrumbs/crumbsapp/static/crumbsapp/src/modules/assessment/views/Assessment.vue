<template>
    <div id="assessment" >
        <transition name="fade" mode="out-in">
            <router-view></router-view>
        </transition>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : 'assessment',
    computed : {
    },
    components : {
    },
    methods:{
    }
}
</script>
<style lang='stylus'>
#assessment
    max-height 100vh
    overflow-y auto
</style>

