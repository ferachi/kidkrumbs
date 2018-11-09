<template>
    <div id="activityItemView" class="py-3">
        <div class="activity-item">
            <div class="px-3">
                <h5 class="color_3" >@ {{activity._time}}</h5>
                <h4 class="m-0" :style="{color: `${activity.color.toLowerCase()} !important`}">{{activity.title}}</h4>
                <p class="mb-1">{{activity.description}}</p>
                <p class="text-lg-right m-0"><small class="font-weight-bold color_3">{{activity.created_by.names}} </small></p>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "activityItemView",
    props:['activity'],
    computed:{
        time(){
            return moment(this.activity.time, "kk:mm:ss").format("hh:mm a");
        }
    }
};
</script>
<style lang="stylus" scoped>
#activityItemView
    .activity-item
        min-height 20vh
</style>
