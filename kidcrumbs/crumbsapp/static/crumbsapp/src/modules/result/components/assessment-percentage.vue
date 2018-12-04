<template>
    <div id="assessmentPercentages" class="d-flex justify-content-center">
       <div class="col-auto px-0">
           <div class="header text-center">
                <h6 class="my-1 color_4 text-capitalize"> Average obtained for each assessment</h6>
                <p class="primary-color m-0 text-center">{{session.start}} - {{session.end}}</p>
           </div>
            <assessment-chart title="results" :width="600" :height="400" :grading="getGrades" :data="results" 
                :padding="0.1" :showGuide="true"> </assessment-chart>
       </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import assessmentChart from '../../../components/bar-chart.vue'
export default{
    name : "assessmentPercentages",
    created(){
    },
    components : {
        assessmentChart
    },
    computed : {
        ...mapGetters('result', { results:'getAssessmentPercentageScores', session:'getSessionDuration'}),
        ...mapGetters('grade', [ 'getGrades']),
    },
}
</script>
<style lang="stylus">
#resultSummaryBar
    max-width 100vw
    overflow-x auto
</style>

