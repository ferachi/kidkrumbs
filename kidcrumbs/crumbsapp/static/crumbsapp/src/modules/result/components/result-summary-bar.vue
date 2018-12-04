<template>
    <div id="resultSummaryBar" class="d-flex justify-content-center">
       <div class="col px-0">
           <div class="header text-center">
                <h6 class="my-1 color_4 text-capitalize text-center"> Total scores obtained for each subject</h6>
                <p class="primary-color m-0 text-center">{{session.start}} - {{session.end}}</p>
                <!-- <p class="primary&#45;color m&#45;0">{{session.start}} &#45; {{session.end}}</p> -->
           </div>
           <div class="bar-holder text-center">
            <bar-chart title="results" :width="600" :height="300" :grading="getGrades" :data="barData" class=""
                :padding="0.1" :showGuide="true"> </bar-chart>
           </div>
       </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import barChart from '../../../components/bar_chart.vue'
export default{
    name : "resultSummaryBar",
    created(){
    },
    components : {
        barChart
    },
    computed : {
        ...mapGetters('result', { resultSummary:'getBaseSubjectResultSummary', 'session':'getSessionDuration'}),
        ...mapGetters('grade', [ 'getGrades']),
        barData(){
            return _.map(_.cloneDeep(this.resultSummary), result => {
                result.label = result.base;
                result.score = result.average;
                return result;
            })
        }
    },
}
</script>
<style lang="stylus">
#resultSummaryBar
    .bar-holder
        max-width 100vw
        overflow-x auto
</style>

