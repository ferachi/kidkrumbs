<template>
    <div id="childHomework">
        <homework-list></homework-list>
    </div>
</template>
<script>
import homeworkList from "../../homework/views/HomeworkList.vue";
export default {
    name: "ChildHomeworkView",
    components:{
        homeworkList,
    }
};
</script>
<style lang="stylus">
</style>
