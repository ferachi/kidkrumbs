<template>
    <div id="gradeArcChart" class=" d-flex justify-content-center">
        <div class="col-auto px-0">
            <h6 class="my-1 color_4 text-capitalize text-center" > Score and Grade summary</h6>
            <p class="primary-color m-0 text-center">{{session.start}} - {{session.end}}</p>
        </div>
        <div class="chart-holder">
            <arc-chart title="gradeChart" :width="350" :height="350" :label="label" :percentage="percentage" :color="color" > </arc-chart>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import arcChart from '../../../components/arc_chart.vue'
export default{
    name : "gradeArcChart",
    created(){
    },
    components : {
        arcChart
    },
    computed : {
        ...mapGetters('result', [ 'getTotalAverageScore', 'getSessionDuration']),
        ...mapGetters('grade', [ 'getGrader']),
        percentage(){
            return this.getTotalAverageScore;
        },
        label(){
            return `Grade : ${this.grade} `
        },
        grade(){
            return this.getGrader.gradeScale(this.percentage);
        },
        color(){
            return this.getGrader.gradeColors[this.grade];
        },
        session(){
            return this.getSessionDuration;
        }

    },
}
</script>
<style lang="stylus">
#gradeArcChart
    .chart-holder
        max-height 100vw
        overflow-x auto
</style>

