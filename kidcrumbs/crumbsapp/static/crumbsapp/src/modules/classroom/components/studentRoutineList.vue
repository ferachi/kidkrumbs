<template>
    <div id="studentRoutineList">
        <div v-if="isLoading" key="loading">
             
        </div>
        <div v-else key="loaded">
            <div class="d-flex flex-wrap" >
                <div class="col-xl-3 col-md-4 col-6 student text-center" v-for="routine in studentRoutines"
                                                                         @click="studentClicked(routine)">
                    <div class="py-2">
                        <div v-if="routine.student.avatar">
                            <md-avatar class="md-avatar md-large">
                                <img :src="routine.student.avatar" :alt="routine.student.username">
                            </md-avatar>
                        </div>
                        <div v-else>
                            <md-avatar class="md-avatar-icon md-large">
                                <md-icon class="fas fa-user-circle md-size-3x"></md-icon>
                            </md-avatar>
                        </div>
                    </div>
                    <h6 class="font-weight-bold m-0">{{routine.student.first_name}}</h6>
                    <p :class="[routine.editted_habit ? 'primary-color' : 'color_3']" >{{routine.student.last_name}}</p>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import avatar from '../../../components/avatarHolder.vue';
export default {
    name : 'StudentRoutineList',

    created(){
        this.routeChanged();
    },
    data(){
        return {
            studentRoutines : [],
            isLoading:true
        }
    },
    props:['id'],
    computed : {
        ...mapGetters('routine', {
            routine : "getRoutine"
        }),
        ...mapGetters('group', {
            students : 'getGroupStudents'
        })
    },
    methods:{
        ...mapActions('routine',{
            fetchRoutine:'fetchRoutineWithProps'
        }),
        studentClicked(routine){
            this.$router.push({name: 'studentBehaviour', params:{routineId:routine.id}});
        },
        routeChanged(){
            this.isLoading = true; 
            this.fetchRoutine(this.id).then(routine => {
                // habits is actually students routine
                this.studentRoutines = _.sortBy(_.map(routine.habits, _habit => {
                    if(_.isString(_habit.student))
                        _habit.student = _.find(this.students, {user : _habit.student});
                    return _habit;
                }), _routine => [_routine.editted_habit == true,  _routine.student.username]);
                this.isLoading = false;
            });
        }
    },
    components:{
        avatar
    },
    watch:{
        '$route'(val){
            this.routeChanged();
        }
    }

}

</script>
<style lang="stylus">

</style>
