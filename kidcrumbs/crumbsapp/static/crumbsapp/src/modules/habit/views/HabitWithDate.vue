<template>
    <div id="habitDetail">
        <section class="header d-flex flex-wrap mt-2 mb-3">
            <div class="col-xl-3 col-12 pt-3">
                <dtpicker :disable-time="true" :dark="isDark" :without-header="true" v-model="date" format="YYYY-MM-DD"
                :auto-close="true" formatted="dddd, MMMM DD, YYYY" label="Select date"></dtpicker>
            </div>
            <div class="col d-flex " v-if="routine"> 
                <div class="col">
                    <md-field>
                        <label>comment</label>
                        <md-textarea md-autogrow v-model="routine.comment"></md-textarea>
                    </md-field>
                </div>
                <div class="col-auto pt-4">
                    <p class="color_5" @click="modifyRoutine"><span class="fas fa-lg fa-save fa-fw"></span></p>
                </div>
                <div class="col-auto pt-4">
                    <p class="color_5" @click="show"><span class="fas fa-lg fa-trash fa-fw"></span></p>
                </div>
            </div>
        </section>
        <section >
            <div v-if="routine">
                <student-list :id="routine.id"></student-list>
                <modal ref="modal" :enable-mobile-fullscreen="false" :modal-theme="getTheme" :overlay-theme="getTheme">
                    <div class="d-flex justify-content-center">
                        <div class="col col-lg-10 py-2 ">
                            <confirm-action @confirm="removeRoutine($event)">
                                <h4>Are you sure you want to to delete this routine</h4>
                            </confirm-action>
                        </div>
                    </div>
                </modal>
            </div>
            <div v-else>
                <no-habit :editable="editable" @add-routine="addRoutine"></no-habit>
            </div>
        </section>        
    </div>
</template>
<script>
import { SweetModal } from 'sweet-modal-vue';
import {mapGetters, mapActions, mapMutations} from 'vuex';
import StudentRoutineList from './StudentRoutineList.vue';
import NoHabit from './HabitNotFound.vue';
import confirmAction from '../../../components/confirm-action.vue';
export default {
    name : 'HabitDetail',
    created(){
        let date = this.$route.params.date;
        if(moment(date, "YYYY-MM-DD").isValid()){
            this.date = moment(date, "YYYY-MM-DD").format("YYYY-MM-DD");
            this.routine = this.getRoutineByDate(this.date);
        }
        this.dateChanged();
    },
    data(){
        return {
            date: moment().format("YYYY-MM-DD"),
            routine: null
        }
    },
    props:{
        editable:{
            type : Boolean,
            default : true
        }
    },
    computed : {
        ...mapGetters('group', {
            group:'getGroup',
            getRoutineByDate:'getGroupRoutineByDate',
        }),
        ...mapGetters('profile',{
            profile : 'getProfile'
        }),
        ...mapGetters([
            'getTheme'
        ]),
        isDark(){
            return this.getTheme == 'dark';
        }
    },
    components:{
        NoHabit,
        confirmAction,
        modal : SweetModal,
        studentList : StudentRoutineList
    },
    methods:{
        ...mapMutations('routine', [
            'setRoutine',
        ]),
        ...mapActions('routine', [
            'saveRoutine',
            'updateRoutine',
            'deleteRoutine',
            'saveStudentsRoutines',
            'saveStudentsAttitudes'
        ]),
        dateChanged(){
            if(this.routine){
                this.setRoutine(this.routine);
            }
            this.$router.push({name:'habitWithDate', params:{date:this.date}});
        }, 
        show () {
            this.$refs.modal.open(); 
        },
        hide () {
            this.$refs.modal.close(); 
        },
        addRoutine(){
            let routine = {comment:"",group : this.group.id, date:this.date , created_by : this.profile.user}
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
                        this.routine = routine;
                    });
                });
            });
        },
        modifyRoutine(){
            this.updateRoutine(this.routine).then(routine =>{
                this.$toasted.show("Routine updated");
            })
        },
        removeRoutine(canDelete){
            // delete routine
            if(canDelete)
            this.deleteRoutine(this.routine.id).then(id => {
                this.routine = null;
            });
            this.$refs.modal.close(); 
        }
    },
    watch:{
        routine(val){
            this.dateChanged();
        },
        date(val){
            this.routine = this.getRoutineByDate(val);
        },
        '$route'(){

        }
    }

}

</script>
<style lang="stylus">

</style>
