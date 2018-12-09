<template>
    <div id="ClassroomHomework" class="">
        <h1>Homework</h1>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
export default {
    name: "ClassroomHomework",
    components : {
    },
    computed : {
        ...mapGetters('classroom', {classroom : 'getClassroom' } ),
    }
};
</script>
<style lang="stylus">
</style>
