<template>
    <div id="subjectTeacher">
        <h5 class="righteous">{{subject.name}} Teachers</h5>
        <teacher-list :people='teachers' @person-click="personClicked($event)"></teacher-list>
    </div>
</template>
<script>
import teacherList from '../../../components/PersonList.vue';
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
