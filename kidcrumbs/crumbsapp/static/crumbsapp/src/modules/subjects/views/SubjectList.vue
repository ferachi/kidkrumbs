<template>
    <div id="subjectList">
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "SubjectList",
    created(){
        this.fetchSubjects().then( subjects => {
            this.subjects = subjects;
            console.log(this.subjects, 'subjects');
        }
    },
    data(){
        return {
            subjects : []
        }
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
