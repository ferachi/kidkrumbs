<template>
    <div id="resultSummaryBar" >
       <div class="">
            <bar-chart title="results" :width="600" :height="300" :grading="getGrades" :data="barData" > </bar-chart>
       </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import barChart from '../../../components/bar_chart.vue'
export default{
    name : "resultSummaryBar",
    created(){
        console.log(this.getGrades);
    },
    data(){
        return {
            gradeScale : null
        }
    },
    components : {
        barChart
    },
    computed : {
        ...mapGetters('result', { resultSummary:'getBaseSubjectResultSummary'}),
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
    max-width 100vw
    overflow-x auto
</style>

