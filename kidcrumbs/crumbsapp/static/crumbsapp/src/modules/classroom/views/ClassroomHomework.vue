<template>
    <div id="ClassroomHomework" class="">
        <homework></homework>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
import homework from '../components/homework.vue';
export default {
    name: "ClassroomHomework",
    components : {
        homework
    },
    computed : {
        ...mapGetters('classroom', {classroom : 'getClassroom' } ),
    }
};
</script>
<style lang="stylus">
</style>
