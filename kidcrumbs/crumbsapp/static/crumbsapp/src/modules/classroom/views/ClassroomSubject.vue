<template>
    <div id="ClassroomSubject" class="">
        <h4 class="text-capitalize font-weight-bold">Subjects</h4>
        <hr>
        <subjects :subjects="subjects" @subject-click="subjectClicked($event)"></subjects>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
import subjects from '../../subject/components/subjects.vue';
export default {
    name: "ClassroomSubjects",
    components : {
        subjects
    },
    computed : {
        ...mapGetters('classroom', {classroom : 'getClassroom', subjects : 'getClassroomSubjects'}),
        ...mapGetters('profile', {profile : 'getProfile' }),
    },
    data(){
        return {
        }
    },
    methods : {
        subjectClicked(subject){
            this.$router.push({name : 'subjectDetail', params:{id:subject.id}});
        }
    }
};
</script>
<style lang="stylus">
</style>
