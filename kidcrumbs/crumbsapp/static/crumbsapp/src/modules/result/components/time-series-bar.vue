<template>
    <div id="resultSummaryBar" class="d-flex justify-content-center flex-wrap">
       <div class="col px-0">
           <div class="header text-center">
                <h6 class="my-1 color_4 text-capitalize" v-if="displayedScore == 'averageScore'"> Average scores obtained per term</h6>
                <h6 class="my-1 color_4 text-capitalize" v-else-if="displayedScore == 'minScore'"> Minimum scores obtained per term</h6>
                <h6 class="my-1 color_4 text-capitalize" v-else-if="displayedScore == 'maxScore'"> Maximum scores obtained per term</h6>
                <h6 class="my-1 color_4 text-capitalize" v-else> Positions obtained per term</h6>
                <p class="primary-color m-0">{{session.start}} - {{session.end}}</p>
           </div>
           <div class="time-series-plot text-center">
                       <timeseries title="timeseries" :width="600" :height="350" :grades="grades" :data="timeData"
                                   :showGuide="true" xLabel="DURATION" :yLabel="yLabel" :invertY="invertPlot"> </timeseries>
           </div>
           <div class=" d-flex flex-wrap justify-content-center">
               <div class="col-sm-auto col-12 px-1">
               <md-radio v-model="displayedScore" value="averageScore">average scores</md-radio> 
               </div>
               <div class="col-sm-auto col-12 px-1">
                   <md-radio v-model="displayedScore" value="minScore">min scores</md-radio> 
               </div>
               <div class="col-sm-auto col-12 px-1">
                   <md-radio v-model="displayedScore" value="maxScore">max scores</md-radio> 
               </div>
               <div class="col-sm-auto col-12 px-1">
                   <md-radio v-model="displayedScore" value="position">position</md-radio> 
               </div>
           </div>
       </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import timeseries from '../../../components/time_series.vue'
export default{
    name : "resultSummaryBar",
    created(){
    },
    components : {
        timeseries
    },
    computed : {
        ...mapGetters('result', { results:'getResultSummary', session: 'getSessionDuration'}),
        ...mapGetters('grade', [ 'getGrades']),
        timeData(){
            let results = _.cloneDeep(this.results),
                termRes = _.groupBy(results, 'term');

            
            let _td = _.sortBy( _.map(termRes, _tr => {
                let studentScore = _.sumBy(_tr, 'score'),
                    minScore = _.minBy(_tr, 'score').score,
                    maxScore = _.maxBy(_tr, 'score').score,
                    position = _tr[0].position,
                    studentTotal = _tr[0].studentTotal,
                    sessionStart = _tr[0].sessionStart,
                    sessionEnd = _tr[0].sessionEnd,
                    assessmentMaxScore = _.sumBy(_tr, 'maxScore'),
                    averageScore = _.round(studentScore/assessmentMaxScore * 100),
                    res = {position,minScore, maxScore, assessmentMaxScore, averageScore, date:_tr[0].termEnd,
                        studentTotal, sessionStart, sessionEnd};
                res['score'] = res[this.displayedScore]; 
                return res;
            }), 'date');

            return _td;
        },
        grades(){
            if(this.displayedScore == 'position'){
                this.invertPlot = true;
                this.yLabel = "POSITIONS";
                return d3.range(1,this.timeData[0].studentTotal + 2);
            }
            this.yLabel = "SCORES(%)";
            this.invertPlot = false;
            return _.map(this.getGrades, g => g.maxScore);
        }
    },
    data(){
        return {
            displayedScore : 'averageScore',
            invertPlot : false,
            yLabel  : "SCORES(%)"
        }
    }
}
</script>
<style lang="stylus">
#resultSummaryBar
    .time-series-plot
        max-width 100vw
        overflow-x auto
</style>

