<template>
    <div id="classroomProfile">
       <section class="header text-center pb-3">
           <div>
           <h3 class="font-weight-bold m-0" >{{classroom.className}}</h3>
           <p class="m-0 color_3 font-weight-bold" style="margin-top : -5px !important"><small class="color_3">{{classroom.session.year}} - {{classroom.group_base.category}}</small></p>
           </div>
           <div class="mt-2" v-if="classroom.head_teacher">
               <div class="" v-if="classroom.head_teacher.avatar" key="avatar">
                   <md-avatar class="">
                       <img :src="classroom.head_teacher.avatar" :alt="classroom.head_teacher.names">
                   </md-avatar>
               </div>
               <div v-else key="noAvatar">
                   <md-avatar class="">
                       <md-avatar class="md-avatar-icon">
                           <md-icon class="fas fa-user fa-fw fa-lg"></md-icon>
                       </md-avatar>
                   </md-avatar>
               </div>
               <div class="" >
                   <p :style="{color:`${color} !important`}" class="m-0">{{classroom.head_teacher.names}}</p>
                   <p class="m-0 " style="margin-top:-5px !important"><small class="color_3">head teacher</small></p>
               </div>
           </div>
       </section>
       <hr>
       <section class="overview py-3">
           <h5 class="font-weight-bold text-center" >Overview of {{classroom.className}}</h5>
            <p>{{classroom.overview}}</p>
       </section>
       <hr>
       <section class="about py-3 text-center">
           <h5 class="font-weight-bold">About {{classroom.group_base.name}}</h5>
           <p class="colr_white"> {{classroom.group_base.description}}</p>
       </section>
    </div>
</template>
<script>
export default{
    name : "ClassroomProfile",
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
