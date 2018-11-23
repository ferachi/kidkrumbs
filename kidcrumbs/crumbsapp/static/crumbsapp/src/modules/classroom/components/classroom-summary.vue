<template>
    <div id="classroomSummary">
       <section class="header">
            <h1 class="font-weight-bold m-0" >{{classroom.className}}</h1>
           <h6 class="m-0 color_3 font-weight-bold">{{classroom.session.year}} - {{classroom.group_base.category}}</h6>
           <div class="d-flex mt-2 align-items-center">
               <div class="col-auto px-0">
                   <md-avatar class="">
                       <img :src="classroom.head_teacher.avatar" :alt="classroom.head_teacher.names">
                   </md-avatar>
               </div>
               <div class="col-auto" v-if="classroom.head_teacher">
                   <p :style="{color:`${color} !important`}" class="m-0">{{classroom.head_teacher.names}}</p>
                   <p class="m-0 " style="margin-top:-5px !important"><small class="color_3">head teacher</small></p>
               </div>
           </div>
            <hr>
       </section>
       <section class="overview my-2">
           <h6 class="font-weight-bold">Overview of {{classroom.className}}</h6>
            <p>{{classroom.overview}}</p>
            <hr>
       </section>
       <section class="about p-2" :style="{background:`${color} !important`}">
           <h6 class="color_white">About {{classroom.group_base.name}}</h6>
           <p class="color_white"> {{classroom.group_base.description}}</p>
       </section>
    </div>
</template>
<script>
export default{
    name : "ClassroomSummary",
    props : ['classroom'],
    computed:{
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
