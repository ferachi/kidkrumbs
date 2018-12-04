<template>
    <div class="resultSummary">
        <div class="d-flex">
            <div class="col-auto" v-for="summary in summaries">
                <rPallete :title="summary.title" :subject="summary.subject" :session="summary.session" :score="summary.score" :maxScore="summary.maxScore"></rPallete>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import rPallete from './result-summary-pallette.vue';
export default {
    name : "ResultSummary",
    components:{
        rPallete
    },
    computed : {
        ...mapGetters('result', {
            minScore:'getMinResult',
            maxScore:'getMaxResult',
            totalScore:'getTotalScores',
            assessmentScores:'getTotalAssessmentScores',
            session : 'getSessionDuration'
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
    },
}
</script>
<style lang="stylus">

</style>
