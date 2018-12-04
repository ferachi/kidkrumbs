<template>
    <div id="resultFrequency" class="d-flex justify-content-center">
       <div class="col px-0">
           <div class="header text-center">
                <h6 class="my-1 color_4 text-capitalize">  Average Assessment score distribution</h6>
                <p class="primary-color m-0 text-center">{{session.start}} - {{session.end}}</p>
           </div>
           <div class="histogram-holder text-center">
               <histogram title="frequency" :width="600" :height="400" :data="histogramData" class="" :padding="0.1" :showGuide="true"> </histogram>
           </div>
       </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import histogram from '../../../components/histogram.vue'
export default{
    name : "resultFrequency",
    created(){
    },
    components : {
        histogram
    },
    computed : {
        ...mapGetters('result', { resultSummary:'getResultSummary', session:'getSessionDuration'}),
        ...mapGetters('grade', [ 'getGrades']),
        histogramData(){
            return this.resultSummary;
        }
    },
}
</script>
<style lang="stylus">
#resultFrequency
    .histogram-holder
        max-width 100vw
        overflow-x auto
</style>

