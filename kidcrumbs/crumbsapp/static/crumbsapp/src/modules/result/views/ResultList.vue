<template>
    <div id="resultList">
        <transicion :isLoading="loading">
        <section class="d-flex justify-content-center">
            <div class="col-8">
                <header class="p-3">
                    <h4 class="text-center text-uppercase m-0">Students</h4>
                </header>
                <div>
                    <students :people="students" @person-click="personClicked($event)">
                    </students>
                </div>
            </div>
        </section>
        </transicion>
    </div>
</template>
<script>
import {mapActions, mapGetters, mapMutations} from 'vuex';
import transicion from '../../../components/transicion.vue';
import students from '../../../components/People.vue';
export default {
    name : "ResultList",
    created (){
        this.fetchData();
    },
    computed:{
        ...mapGetters('school',['getSchool'])
    },
    components:{
        transicion,
        students
    },
    data(){
        return {
            loading : true,
            students : []
        }
    },
    methods : {
        ...mapActions('school', ['fetchSchoolStudents']),
        ...mapMutations('child', ['setChild']),
        fetchData(){
            this.fetchSchoolStudents(this.$route.params.schoolId).then(students => {
                this.students = students;
                this.loading = false;
            });
        },
        personClicked(student){
            this.setChild(student);
            this.$router.push({name:'resultDetail', params:{username : student.username}});
        }
    }
}
</script>
<style lang="stylus">

</style>
