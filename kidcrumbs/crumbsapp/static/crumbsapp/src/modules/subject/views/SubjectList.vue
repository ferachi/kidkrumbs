<template>
    <div id="subjectList">
        <subjects :subjects="subjects" @subject-click="subjectClicked($event)"></subjects>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
import subjects from '../components/subjects.vue';
export default{
    name : "SubjectList",
    created(){
        this.fetchSubjects().then( subjects => {
            this.subjects = subjects;
        });
    },
    data(){
        return {
            subjects : []
        }
    },
    components:{
        subjects
    },
    methods:{
        ...mapActions('subject',[
            'fetchSubjects'
        ]),
        subjectClicked(subject){
            this.$router.push({name : 'subjectDetail', params:{id:subject.id}});
        }

    }
}
</script>
<style lang="stylus">

</style>
