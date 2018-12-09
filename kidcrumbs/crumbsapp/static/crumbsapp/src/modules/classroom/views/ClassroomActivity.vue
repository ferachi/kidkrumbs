<template>
    <div id="ClassroomActivity" class="">
        <h1>Activity</h1>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
export default {
    name: "ClassroomActivity",
    components : {
    },
    computed : {
        ...mapGetters('classroom', {classroom : 'getClassroom' } ),
    }
};
</script>
<style lang="stylus">
</style>
