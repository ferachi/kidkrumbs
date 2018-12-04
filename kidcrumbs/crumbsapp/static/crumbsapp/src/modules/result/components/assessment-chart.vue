<template>
    <div id="assessmentPercentages" class="d-flex justify-content-center">
       <div class="col px-0">
           <div class="header text-center">
                <h6 class="my-1 color_4 text-capitalize"> Total scores obtained for each subject</h6>
                <!-- <p class="primary&#45;color m&#45;0">{{session.start}} &#45; {{session.end}}</p> -->
           </div>
           <div class="chart-holder text-center">
               <assessment-chart title="assessments" :width="600" :height="400" :grading="getGrades" :data="assessmentData" :padding="0.1" :showGuide="true"> </assessment-chart>
           </div>
       </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import assessmentChart from '../../../components/bar_chart.vue'
export default{
    name : "resultSummaryBar",
    created(){
    },
    components : {
        assessmentChart
    },
    computed : {
        ...mapGetters('result', { results:'getAssessmentPercentageScores'}),
        ...mapGetters('grade', [ 'getGrades']),
        assessmentData(){
            return _.map(_.cloneDeep(this.results), result => {
                console.log(result);
                let {assessment:label, averageScore : score} = result;
                console.log({label, score});
                return {label, score};
            })
        }
    },
}
</script>
<style lang="stylus">
#assessmentPercentages
    .chart-holder
        max-width 100vw
        overflow-x auto
</style>

