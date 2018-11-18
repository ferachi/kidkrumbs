<template>
    <div id="subjectList">
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
import subjects from '../components/subjects.vue';
export default{
    name : "SubjectList",
    created(){
        this.fetchSubjects().then( subjects => {
            console.log( subjects , 'fo');
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
    }
}
</script>
<style lang="stylus">

</style>
