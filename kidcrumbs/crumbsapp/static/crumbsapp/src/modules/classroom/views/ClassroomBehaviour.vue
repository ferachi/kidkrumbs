<template>
    <div id="ClassroomBehaviour" class="">
        <transition name="fade" mode="out-in">
            <router-view></router-view>
        </transition>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
export default {
    name: "ClassroomBehaviour",
    components : {
    },
    computed : {
        ...mapGetters('classroom', {classroom : 'getClassroom' } ),
    }
};
</script>
<style lang="stylus">
</style>
