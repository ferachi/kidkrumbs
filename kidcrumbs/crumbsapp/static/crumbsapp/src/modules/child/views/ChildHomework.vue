<template>
    <div id="childHomework">
        <h4 class="font-weight-bold">Home works</h4>
        <hr>
        <homework-list :classroomId="classroom.id"></homework-list>
    </div>
</template>
<script>
import homeworkList from "../../homework/views/HomeworkList.vue";
import {mapGetters} from 'vuex';
export default {
    name: "ChildHomeworkView",
    components:{
        homeworkList,
    },
    computed : {
        ...mapGetters('child', {classroom:'getChildClassroom'})
    }
};
</script>
<style lang="stylus">
</style>
