<template>
    <div id="childSubjects">
        <h4 class="font-weight-bold">Subjects</h4>
        <hr>
        <subjects :subjects="subjects" @subject-click="subjectClicked($event)"></subjects>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
import subjects from '../../subject/components/subjects.vue';
export default{
    name : "childSubjects",
    computed:{
        ...mapGetters('child', {
           subjects : 'getChildSubjects'
        })
    },
    components:{
        subjects
    },
    methods:{
        subjectClicked(subject){
            this.$router.push({name : 'subjectDetail', params:{id:subject.id}});
        }

    }
}
</script>
<style lang="stylus">

</style>
