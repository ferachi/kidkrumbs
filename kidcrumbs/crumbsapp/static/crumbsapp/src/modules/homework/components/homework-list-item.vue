<template>
    <div class="subject-list-item d-flex my-3 align-items-center">
        <div class="col-auto p-1 first-char " :class="[homework.isExpired ? 'secondary-bg' : 'primary-bg']">
            <h2 class="rammeto text-center color_white align-middle m-0" >{{firstChar}} </h2>    
        </div>
        <div class="col">
            <div class="d-flex justify-content-between align-items-center">
                <div class="col-autom p-0">
                    <h6 class="m-0 font-weight-bold ">{{homework.subject.name}}</h6>
                </div>
                <div class="col-auto p-0">
                    <p class="m-0 col-auto"><small class="color_3">{{assignedDate}}</small></p>
                </div>
            </div>
            <p class="m-0 mb-3 mt-1">{{homework.description}}</p>
            <div class="">
                <p class="m-0" style="margin-bottom : -5px !important;"><small>submision: {{submissionDate}}</small></p>
                <p class="m-0"><small class="color_3"> teacher : {{homework.teacher}}</small></p>
            </div>
        </div>
    </div>
</template>
<script>
export default{
    name : "HomeworkItem",
    props : ['homework'],
    computed:{
        firstChar(){
            return this.homework.subject.name.charAt(0);
        },
        submissionDate(){
            return moment(this.homework.submission_date, "YYYY-MM-DD").format("ddd MMM Do, YYYY");
        },
        assignedDate(){
            return moment(this.homework.assigned_date, "YYYY-MM-DD").format("ddd MMM Do, YYYY");
        },
        isExpired(){
            return moment(this.homework.submission_date,"YYYY-MM-DD").isBefore(moment().format("YYYY-MM-DD"));
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
