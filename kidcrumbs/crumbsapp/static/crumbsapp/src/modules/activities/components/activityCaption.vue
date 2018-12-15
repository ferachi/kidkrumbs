<template>
    <div class="activity-caption">
        <div class="d-flex align-items-center">
            <div class="col-auto d-flex align-items-center justify-content-center text-center color-head p-0 px-lg-4" :style="{'background-color':`${activity.color.toLowerCase()} !important` }">
                <h1 class="display-4 color_0 m-0 text-uppercase">{{activity.note.charAt(0)}}</h1>
            </div>
            <div class="col px-2 d-flex flex-wrap">
                <div class="col-lg-auto col-12 order-lg-1">
                    <h6 class="" ><small class="color_4">{{date}}</small></h6>
                </div>
                <div class="col">
                    <h6 class="color_5">{{note | truncate(100)}}</h6>
                    <div class="d-flex">
                        <div class="col-auto px-2">
                            <h6><small class="color_3"><span class="font-weight-bold"> {{activityCount}} </span><i class="fas fa-stopwatch fa-fw"></i></small></h6>
                        </div>
                        <div class="col-auto px-2">
                            <h6><small class="color_3"><span class="font-weight-bold"> {{commentCount}} </span><i class="fas fa-comments fa-fw"></i></small></h6>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "activityCaption",
    props :['activity'],
    computed:{
        date(){
            return moment(this.activity.date, "YYYY-MM-DD").format("MMMM DD, YYYY");
        },
        activityCount(){
            return this.activity.activities.length;
        },
        commentCount(){
            return this.activity.comments.length;
        },
        note(){
            return _.upperFirst(this.activity.note)
        }
    }

};
</script>
<style lang="stylus">
.activity-caption
    .color-head
        height 70px
        width @height

</style>
