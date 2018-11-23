<template>
    <div class="classroom-list-item d-flex justify-content-center p-0">
        <div class="bg_0 border border_1 menu clickable col px-0 d-flex h-100 pb-3" >
            <div class="col px-0 h-100">
                <div class="w-100 py-3 h-75 d-flex align-items-center justify-content-center" :style="{background:color}">
                    <h1 class="display- color_white m-0">{{classroom.group_base.short_name}}</h1>
                </div>
                <div class="p-2">
                    <h6 class="m-0"><span>{{classroom.className}}</span> </h6>
                    <p class="m-0" style="margin-top:-4px !important"><small class="color_3">{{classroom.session.year}}</small></p>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default{
    name : "ClassroomListItem",
    props : ['classroom'],
    computed:{
        firstChar(){
            return this.classroom.group_base.name.charAt(0);
        },
        color(){
            return this.classroom.color.toLowerCase()
        }
    }
}
</script>
<style lang="stylus">
.classroom-list-item
    height 180px
</style>
