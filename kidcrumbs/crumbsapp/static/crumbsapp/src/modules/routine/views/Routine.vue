<template>
    <div id="routine">
        <div v-if="isLoading" key="loading">
        
        </div>
        <div v-else key="loaded">
            <div class="header">
                <p>dates</p>
             </div>
            <div  class="views">
                <router-view></router-view>
            </div>
            <div v-if="showEmpty" class="empty-holder d-flex align-items-center justify-content-center" >
                <div class="col-auto text-center editable" v-if="editable">
                    <h1 @click="addRoutine">
                        <span class="color_2 fa-stack fa-4x" style="vertical-align: top;">
                            <i class="far fa-circle fa-stack-2x"></i>
                            <i class="fas fa-plug fa-stack-1x"></i>
                        </span>
                    </h1>
                    <h5>
                        No routine has been added. Click the plug to add a new routine.
                    </h5>
                </div>
                <div class="col-auto text-center non-editable" v-else>
                    <h1>
                        <span class="color_2 fa-stack fa-4x" style="vertical-align: top;">
                            <i class="far fa-circle fa-stack-2x"></i>
                            <i class="fas fa-times fa-stack-1x"></i>
                        </span>
                    </h1>
                    <h5>
                        Did not find any Habit. 
                    </h5>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : "Routine",
    created(){
                // TODO: this is a test only
                // this should be this.getGroupStudents & getGroupHabits
                // as this method should only be called in a
                // groups' module by which before it is called
                // the groups and its props should be in the store
                this.fetchGroupWithProps(this.groupId).then( group => {
                    this.getRoutineDetail();
                })
    },
    components:{
    },
    props:{
        editable:{
            type : Boolean,
            default:true
        }
    },
    data(){
        return {
            date:moment().add(1,'d').format("YYYY-MM-DD"), // gets todays date
            groupId: "944e18be-0b51-4ab5-a584-a87811cf1886", // test group
            isLoading : true,
            routine : null,
            showEmpty: true,
            array:["2"]
        }
    },
    computed:{
        ...mapGetters('routine', [
            'getGroupRoutinesByDate'
      ]),
        ...mapGetters('profile',{
            profile : "getProfile",
        }),
        ...mapGetters('group', {
           group : 'getGroup' 
        })
    },
    methods : {
        ...mapActions('routine',[
            'fetchGroupRoutines',
            'saveRoutine',
            'saveStudentsRoutines',
            'saveStudentsAttitudes'
        ]),
        ...mapActions('group',[
            'fetchGroupWithProps'
        ]),
        ...mapMutations("routine", [
        ]),
        getRoutineDetail(){
            // fetch this groups routines
            this.fetchGroupRoutines(this.groupId).then(routines => {
                console.log(routines, 'routines');
                if(routines.length == 0){
                    return;
                }
                // get the routine specified by the date
                this.routine = this.getGroupRoutinesByDate(this.groupId, this.date);

                // if no routine for the date specified show empty place holder
                if(!this.routine){
                    this.showEmpty = true;
                }
                else{
                    //fetch from server and display
                    this.showEmpty = false;
                    this.$router.push({name: 'routine', params:{id:this.routine.id}});
                }
                this.isLoading = false;
                
            });

        },
        addRoutine(){
            // create a routine for today
            let routine = {comment:"",group : this.groupId, date: moment().add(1,'d').format("YYYY-MM-DD"), created_by : this.profile.user}
            this.saveRoutine(routine).then( routine => {
                // creating routines for all the students in the group
                let routines = _.map( this.group.students, student =>{
                    return { routine : routine.id, student : student.user, message:"", created_by:this.profile.user};
                });

                // saving these routines
                this.saveStudentsRoutines(routines).then( _routines => {

                    // create default attitudes(habit responses) for each student
                    let studentAttitudes = _.flatMap(_routines, _routine =>{
                        return _.flatMap(this.group.habits, habit =>{
                            console.log('habit', habit);
                            return _.map(habit.options, option =>{
                                return {
                                    habit_option : option.id,
                                    student_routine : _routine.id,
                                    title : option.title,
                                    value : option.habit_type == "CH" ? "NO" : ""
                                }
                            })
                        })
                    });

                    // save the attitudes
                    this.saveStudentsAttitudes(studentAttitudes).then( attitudes =>{
                        console.log('saved', studentAttitudes, attitudes);
                        this.getRoutineDetail();
                    });
                });
            });
        }
    }

}
</script>
<style lang="stylus">
#routine
    .empty-holder
        min-height 80vh

</style>

