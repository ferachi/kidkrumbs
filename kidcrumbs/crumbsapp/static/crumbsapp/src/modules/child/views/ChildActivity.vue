<template>
    <div id="childActivity" class="">
        <router-view></router-view>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : "ChildActivity",
    created(){
        this.activityId = this.getCurrentActivity.id;
        this.$router.push({name:"childActivityDetail", params:{id:this.activityId}});

    },
    data(){
        return{
            activityId : 0,
        }
    },
    computed:{
        ...mapGetters('activity', [
            'getCurrentActivity'
        ]),
    },
}
</script>
<style lang="stylus">
</style>

