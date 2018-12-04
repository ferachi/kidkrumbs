<template>
    <div id="resultOverview">
        <div class="d-flex flex-wrap p-2">
            <div class="col-lg px-1 bg_0 m-1 pt-4">
                <tseries></tseries>
            </div>
            <div class="col-lg-6 col-xl-4 px-1 m-1 bg_0 pt-4">
                <piechart></piechart>
            </div>
            <div class="col-lg col-xl-4 px-1 m-1 bg_0 pt-4">
                <apiechart></apiechart>
            </div>
            <div class="col-xl col-lg-12 col px-1 m-1 bg_0 pt-4">
                <barchart></barchart>
            </div>
            <div class="col-lg-12 col-xl-6 px-1 m-1 bg_0 pt-4">
                <rfreq></rfreq>
            </div>
            <div class="col-xl col-lg-12 px-1 m-1 bg_0 pt-4">
                <aChart></aChart>
            </div>
            <div class="col-sm-12 col-lg col-xl col-md   bg_0 px-1 m-1 pt-4 " v-for="summary in summaries">
                <rPallete :title="summary.title" :subject="summary.subject" :session="summary.session" :score="summary.score" :maxScore="summary.maxScore"></rPallete>
            </div>
            <div class="col-xl-3 col-lg-12 px-1 m-1 bg_0 pt-4">
                <grade-arc></grade-arc>
            </div>
        </div>
    </div>
</template>
<script>
import barchart from './result-summary-bar.vue';
import rSummary from './result-summary.vue';
import aChart from './assessment-chart.vue';
import rfreq from './result-frequency.vue';
import tseries from './time-series-bar.vue';
import piechart from './pie-chart.vue';
import gradeArc from './grade-arc-chart.vue';
import apiechart from './assessment-pie-chart.vue';
import rPallete from './result-summary-pallette.vue';
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default {
    name : "ResultOverview",
    props : ['results'],
    components:{
        barchart,
        piechart,
        tseries,
        rfreq,
        aChart,
        apiechart,
        rPallete,
        gradeArc
    },
    computed :{
        ...mapGetters('result', {
            minScore:'getMinResult',
            maxScore:'getMaxResult',
            totalScore:'getTotalScores',
            assessmentScores:'getTotalAssessmentScores',
            session:'getSessionDuration'
        }),
        summaries(){
            return [
                {score : this.minScore.score, maxScore:this.minScore.maxScore, session:{start:this.session.start,
                    end:this.session.end},subject: this.minScore.subject, title:"Minimum score ever obtained"},
                {score : this.maxScore.score, maxScore:this.maxScore.maxScore, session:{start:this.session.start,
                    end:this.session.end},subject: this.maxScore.subject, title:"Maximum score ever obtained"}, 
                {score : this.totalScore, maxScore:this.assessmentScores, session:{start:this.session.start,
                    end:this.session.end},subject: '', title:"Maximum score ever obtained"}
                ]
        }
    }
}
</script>
<style lang="stylus">
</style>
