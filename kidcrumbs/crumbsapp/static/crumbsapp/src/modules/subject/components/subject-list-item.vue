<template>
    <div class="subject-list-item d-flex my-3 align-items-center">
        <div class="col-auto p-1 first-char" :style="{'background':color}">
            <h2 class="rammeto text-center color_white align-middle m-0">{{firstChar}}</h2>    
        </div>
        <div class="col">
            <h6 class="m-0">{{subject.name}}</h6>
            <p class="color_3 m-0">{{subject.subject_code}}</p>
        </div>
    </div>
</template>
<script>
export default{
    name : "SubjectListItem",
    props : ['subject'],
    computed:{
        firstChar(){
            return this.subject.name.charAt(0);
        },
        color(){
            return this.subject.color.toLowerCase()
        }
    }
}
</script>
<style lang="stylus">
.subject-list-item
    .first-char
        width 50px
        height @width
        border-radius 50%

</style>
