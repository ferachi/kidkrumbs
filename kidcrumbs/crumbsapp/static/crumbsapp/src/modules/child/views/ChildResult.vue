<template>
    <div id="childResult" class="">
        <div v-if="hasResults">
            <h4 class="font-weight-bold m-0">Results</h4>
            <h6 class="m-0" ><small class="color_4">Summary of results obtained by <span
                                    class="font-weight-bold text-uppercase color_5">
                        {{child.names}} </span> from {{getSessionDuration.start}} to
                    {{getSessionDuration.end}}</small></h6>

            <hr>
            <h6 class="text-uppercase font-weight-bold ">Scores Summary</h6>
            <div class="d-flex flex-wrap align-items-center">
                <div class="col-md-8 col-12 px-0 py-3 order-lg-0 order-1">
                    <summary-line class="col px-0" ></summary-line>
                </div>
                <div class="col-md-4 col-12 px-0 py-3 order-lg-1 order-0 text-center">
                    <summary-pane class="col px-0"></summary-pane>
                    <div class="py-3">
                        <md-button class="md-primary md-dense md-raised" @click="$router.push({name:'resultDetail',
                        params:{username:child.username}})"> view details <i class="fas fa-chart-line fa-fw" ></i> </md-button>
                    </div>
                </div>
            </div>
            <hr>
            <div class="d-flex flex-wrap align-items-center">
                <div class="col-12 px-0 py-3 ">
                    <h5 class="text-center m-0"><small class="color_5">Average scores per subject enrolled
                            <br> <span class="color_3"> for </span><span class="font-weight-bold">{{child.names}}</span>
                            <span class="color_3">from {{getSessionDuration.start}} to {{getSessionDuration.end}}</span></small></h5>
                    <div class="rep-box d-flex align-items-center justify-content-center ">
                        <summary-bar class="col-auto px-0"></summary-bar>
                    </div>
                    <h6 class="text-center "><small class="color_5"></small></h6>
                    <hr>
                </div>
                <div class="col-12 px-0 py-3">
                    <h5 class="text-center m-0"><small class="color_5">Percentage of grades obtained
                            <br> <span class="color_3"> by </span><span class="font-weight-bold">{{child.names}}</span>
                            <span class="color_3">from {{getSessionDuration.start}} to {{getSessionDuration.end}}</span></small></h5>
                    <div class="rep-box d-flex align-items-center justify-content-center ">
                        <pie-chart class="col-auto px-0"></pie-chart>
                    </div>
                </div>
            </div>
        </div>
        <div v-else>
            <h4 class="font-weight-bold m-0">Results</h4>
            <hr>
            <div class="d-flex justify-content-center align-items-center empty-result">
                <div class="text-center col-auto">
                    <h3 class="color_3 text-uppercase">No Results</h3>
                    <h1 class="display-2 color_2"><i class="fas fa-chart-bar fa-2x"></i></h1>
                    <h6 class="color_3 text-upperase" style="line-height : 1.3em !important"><span class="text-uppercase">{{child.names}}</span> <br/>
                        Has no result for display yet.</h6>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import pieChart from '../components/pieChart.vue';
import summaryBar from '../components/resultSummaryBar.vue';
import summaryPane from '../components/resultSummaryPane.vue';
import summaryLine from '../components/resultSummaryLine.vue';
export default{
    name : "ChildResult",
    computed : {
        ...mapGetters('child',{results:'getChildResults', child:'getChild' }),
        ...mapGetters('result',[
            'getTotalAverageScore',
            'getSessionDuration'
        ]),
        hasResults(){
            return this.results.length > 0;
        }
    },
    components:{
        pieChart,
        summaryBar,
        summaryPane,
        summaryLine
    }
}
</script>
<style lang="stylus">
#childResult
    .rep-box
        min-height 300px
    .empty-result
        min-height 40vh
</style>

