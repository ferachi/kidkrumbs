<template>
    <div id="childActivity" class="">
        <activityDetailByDate></activityDetailByDate>
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
}
</script>
<style lang="stylus">
</style>

