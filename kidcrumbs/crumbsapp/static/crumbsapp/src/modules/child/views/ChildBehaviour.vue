<template>
    <div id="childBehaviour" class="">
        <h4 class="font-weight-bold">Behaviours</h4>
        <hr>
        <section class="header">
                <dtpicker :disable-time="true" :dark="isDark" :without-header="true" v-model="date" format="YYYY-MM-DD" :auto-close="true" formatted="dddd, MMMM DD, YYYY" label="Select date"></dtpicker>
        </section>
        <hr>
        <section v-if="habit">
            <student-attitude :id="habit.id" :editable="false"></student-attitude>
        </section>
        <section v-else class="no-habit d-flex align-items-center justify-content-center">
            <div class="text-center col-auto">
                <h1 class="display-2 color_2"><i class="fas fa-people-carry fa-fw"></i></h1>
                <h3 class="color_3 text-uppercase">No Behaviours Today</h3>
            </div>
        </section>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import studentAttitude from "../../habit/views/StudentAttitude.vue";
export default{
    name : "ChildBehaviour",
    created(){
        this.init();
    },
    components:{
        studentAttitude
    },
    data(){
        return {
            date : null,
        }
    },
    computed:{
        ...mapGetters([
            'getTheme'
        ]),
        ...mapGetters('child', [
            'getChildClassroom',
            'getChildHabitsByGroup'
        ]),
        isDark(){
            return this.getTheme == 'dark';
        },
        habit(){
            return _.find(this.habits, {date : this.date});
        },
        habits() {
            let habits = _.compact(_.map(this.getChildHabitsByGroup(this.getChildClassroom.id), _habit => {
                _habit.date = moment(_habit.routine.date).format("YYYY-MM-DD");   
                // only display edited habits and routines with permissions to display. 
                if (_habit.editted_habit && _habit.routine.public_display) 
                    return _habit;
            })); 
            return habits
        }
    },
    methods : {
        ...mapActions('child',[
            "fetchChildHabitsByGroup",
        ]),
        ...mapActions('group',[
            "fetchGroupHabits",
        ]),
        init(){
            this.date = this.$route.params.date;
        },
    },
    watch:{
        '$route'(to,from){
            this.init();       
        },
        date(val){
            this.$router.push({name: "childBehaviour", params:{date:this.date}});
        }
    },

}
</script>
<style lang="stylus">
#childBehaviour
    .no-habit
        min-height 40vh
</style>

