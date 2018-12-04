<template>
    <div id="pie" class=" d-flex justify-content-center">
        <div class="col px-0">
            <h6 class="my-1 color_4 text-capitalize text-center" > Percentage of grades obtained </h6>
            <p class="primary-color m-0 text-center">{{session.start}} - {{session.end}}</p>
            <div class="pie-holder text-center">
                <pie title="pieSum" :width="350" :height="350" :data="pieData" class="col-auto px-0" :labels="labels"> </pie>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import pie from '../../../components/pie_chart.vue'
export default{
    name : "pieChart",
    created(){
    },
    components : {
        pie
    },
    computed : {
        ...mapGetters('result', [ 'getGradeFrequency', 'getSessionDuration']),
        ...mapGetters('grade', [ 'getGrades']),
        pieData(){
            return _.map(this.getGradeFrequency, grade => {
                let {grade : label, percentage, color} = grade;
                return {label, percentage, color}
            })
        },
        labels(){
            return _.map( this.getGrades, grade => {
                let {grade : label, color} = grade;
                return {label, color}
            })
        },
        session(){
            return this.getSessionDuration;
        }
    },
}
</script>
<style lang="stylus">
#pie
    .pie-holder
        max-width 100vw
        overflow-x auto
</style>

