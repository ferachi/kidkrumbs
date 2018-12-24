<template>
    <div id="childActivity" class="">
        <h4 class="font-weight-bold">Activities</h4>
        <hr>
        <activityDetailByDate :groupId="classroom.id"></activityDetailByDate>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import activityDetailByDate from "../../activities/views/ActivityDateDetail.vue";
export default{
    name : "ChildActivity",
    created(){
    },
    data(){
        return{
        }
    },
    components:{
        activityDetailByDate
    },
    computed:{
        ...mapGetters('child', {'classroom' : 'getChildClassroom'})
    }
}
</script>
<style lang="stylus">
</style>

