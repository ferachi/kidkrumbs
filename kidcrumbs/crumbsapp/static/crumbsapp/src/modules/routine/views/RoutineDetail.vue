<template>
    <div class="routineDetail">
        <!-- <md&#45;checkbox class="md&#45;primary" v&#45;model="array" value="2" :disabled="true">Array</md&#45;checkbox> -->
        <div class="d-flex">
            <div @click="showDetail(routine.id)" class="col-6 col-md-3 col-xl-2 routines px-4" v-for="routine in studentRoutines">
                <div class="student text-center">
                    <avatar :image="routine.student.avatar" size="fa-8x" :rounded="true"></avatar> 
                    <h6 class="font-weight-bold m-0">{{routine.student.first_name}}</h6>
                    <p :class="[routine.editted_habit ? 'primary_color' : 'color_3']" >{{routine.student.last_name}}</p>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import avatar from '../../../components/avatarHolder.vue';
export default{
    name : "RoutineDetail",
    created(){ 
        this.fetchRoutine(this.$route.params.id).then(routine => {
            let studentsRoutines = this.fetchStudentsRoutines(routine.id),
                groupStudents = this.fetchGroupStudents(routine.group);
            Promise.all([studentsRoutines, groupStudents]).then( props =>{
                 this.studentRoutines= _.map(props[0], studentRoutine => {
                    studentRoutine.student = _.find(props[1], {user : studentRoutine.student}); 
                    return studentRoutine;
                });
            });
        });
    },
    components:{
        avatar,
    },
    data(){
        return {
            studentRoutines : []
        }
    },
    computed:{
        ...mapGetters('routine', {
            routine:'getRoutine',
        }),
        ...mapGetters('group', {
            students : 'getGroupStudents',
            habits : 'getGroupHabits'
        })

    },
    methods : {
        ...mapActions('routine', [
            'fetchRoutine',
            'fetchStudentsRoutines'
        ]),
        ...mapActions('group',[
            'fetchGroupStudents'
        ]),
        showDetail(id){
            this.$router.push({name:'studentRoutine', params:{routineId:id}});
        }
    }

}
</script>
<style lang="stylus">
</style>

