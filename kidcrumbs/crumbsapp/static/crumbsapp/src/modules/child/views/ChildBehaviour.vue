<template>
    <div id="childBehaviour" class="">
        <section class="header">
                <dtpicker :disable-time="true" :dark="isDark" :without-header="true" v-model="date" format="YYYY-MM-DD" :auto-close="true" formatted="dddd, MMMM DD, YYYY" label="Select date"></dtpicker>
        </section>
        <section>
            <router-view></router-view>
        </section>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : "ChildBehaviour",
    created(){
        let group = this.getCurrentClassroom;
        Promise.all([this.fetchGroupHabits(group.id),this.fetchChildHabitsByGroup(group.id)]).then( props => {
            this.habits = _.map(props[1] , _habit => {
                _habit.date = moment(_habit.routine.date).format("YYYY-MM-DD");   
                return _habit;
            }); 
            this.habits = _.filter(this.habits, _habit => {
                // only display edited habits and routines with permissions to display. 
                return _habit.editted_habit && _habit.routine.public_display; 
            })
            
            this.date =  moment().format("YYYY-MM-DD");
        });
    },
    components:{
    },
    data(){
        return {
            date : null,
            habits : [], 
            habit : null
        }
    },
    computed:{
        ...mapGetters([
            'getTheme'
        ]),
        ...mapGetters('child', [
            'getCurrentClassroom'
        ]),
        isDark(){
            return this.getTheme == 'dark';
        }
    },
    methods : {
        ...mapActions('child',[
            "fetchChildHabitsByGroup",
        ]),
        ...mapActions('group',[
            "fetchGroupHabits",
        ]),
        dateChanged(){
            this.habit = _.find(this.habits, {date : this.date});
            if(this.habit) 
                this.$router.push({name: "childHabits", params:{id:this.habit.id}});
            else
                this.$router.push({name:"noChildHabits"});
        }
    },
    watch:{
        date(val){
            this.dateChanged();
        }
    },

}
</script>
<style lang="stylus">
</style>

