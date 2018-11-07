<template>
    <div class="activity-caption">
        <div class="d-flex align-items-center">
            <div class="col-auto d-flex align-items-center justify-content-center text-center color-head p-0 px-lg-4" :style="{'background-color':`${activity.color.toLowerCase()} !important` }">
                <h1 class="display-4 color_0 m-0">{{activity.note.charAt(0)}}</h1>
            </div>
            <div class="col px-2">
                <h5 class="" >{{date}}</h5>
                <p class="color_5">{{activity.note}}</p>
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
            return moment(this.activity.date, "YYYY-MM-DD").format("DD/MM/YYYY");
        }
    }

};
</script>
<style lang="stylus">
.activity-caption
    .color-head
        
        min-height 80px
        min-width @min-height

</style>
