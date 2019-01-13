<template>
    <div id="subjectTeacher">
        <div v-if="teachers.length > 0">
            <h4 class="font-weight-bold my-3">Teachers</h4>
            <teacher-list :people='teachers' @person-click="personClicked($event)"></teacher-list>
        </div>
        <div v-else class="d-flex justify-content-center align-items-center" > 
            <div class="text-center col-auto py-4">
                <h1 class="color_2 mb-5">
                    <span class="color_2 fa-layers fa-fw fa-3x" style="vertical-align: top;">
                        <i class="fas fa-ban" data-fa-transform="grow-7"></i>
                        <i class="fas fa-user" data-fa-transform="shrink-7"></i>
                    </span>
                </h1>
                <h3 class="color_3 text-uppercase">No Teacher</h3>
                <h6 class="color_3 text-upperase" style="line-height : 1.3em !important">{{subject.name}} does not have
                    any teachers yet</h6>
            </div>
        </div>

    </div>
</template>
<script>
import teacherList from '../../../components/People.vue';
import {mapGetters} from 'vuex';
export default{
    name : "SubjectTeacher",
    computed : {
        ...mapGetters('subject', {
            subject : 'getSubject'
        }),
        teachers(){
            let _teachers = _.map(this.subject.subject_teachers, subject_teacher => {
                return subject_teacher.teacher
            });
            return _teachers;
        },
    },
    components:{
        teacherList, 
    }, 
    methods:{
        personClicked(person){
            console.log(person);
        }
    }
}
</script>
<style lang="stylus">

</style>
