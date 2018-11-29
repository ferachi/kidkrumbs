<template>
    <div id="childResult" class="">
        <div class="d-flex justify-content-end"> 
        </div>
        <hr>
        <h6 class="text-uppercase font-weight-bold ">Scores Summary</h6>
        <div class="d-flex flex-wrap align-items-center">
            <div class="col-md-8 col-12 px-0 py-3 order-lg-0 order-1">
                    <summary-line class="col px-0" ></summary-line>
            </div>
            <div class="col-md-4 col-12 px-0 py-3 order-lg-1 order-0">
                    <summary-pane class="col px-0"></summary-pane>
            </div>
        </div>
        <hr>
        <h6 class="text-uppercase font-weight-bold">Result Summary</h6>
        <div class="d-flex flex-wrap align-items-center">
            <div class="col-lg col-12 px-0 py-3">
                <div class="rep-box d-flex align-items-center justify-content-center ">
                    <pie-chart class="col px-0"></pie-chart>
                </div>
                <h6 class="text-center "><small class="color_5">Percentage of grades obtained by student</small></h6>
            </div>
            <div class="col-lg-auto col-12 px-0 py-3 ">
                <div class="rep-box d-flex align-items-center justify-content-center ">
                    <summary-bar class="col px-0"></summary-bar>
                </div>
                <h6 class="text-center "><small class="color_5">Average scores per subject enrolled</small></h6>
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
        ...mapGetters('child',['getChildResults', 'getChild']),
        ...mapGetters('result',[
            'getTotalAverageScore',
        ]),
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
</style>

