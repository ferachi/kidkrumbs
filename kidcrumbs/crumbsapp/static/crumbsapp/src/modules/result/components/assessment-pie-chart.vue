<template>
    <div id="apie" class=" d-flex justify-content-center">
        <div class="col px-0">
            <h6 class="my-1 color_4 text-capitalize text-center" > Percentage of grades obtained </h6>
            <p class="primary-color m-0 text-center">{{session.start}} - {{session.end}}</p>
            <div class="pie-holder text-center">
                <asspie title="assessmentPieChart" :width="350" :height="350" :data="pieData" class="col-auto px-0" :labels="labels"> </asspie>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import asspie from '../../../components/pie_chart.vue'
export default{
    name : "apieChart",
    created(){
    },
    components : {
        asspie
    },
    computed : {
        ...mapGetters('result', [ 'getPercentageAssessmentWritten', 'getSessionDuration']),
        ...mapGetters('grade', [ 'getGrades']),
        pieData(){
            return _.map(this.getPercentageAssessmentWritten, assessment => {
                let {assessment : label, percentage, color} = assessment;
                return {label, percentage, color}
            })
        },
        labels(){
            return _.map(this.getPercentageAssessmentWritten, assessment => {
                let {assessment : label, color} = assessment;
                return {label, color}
            })
        },
        session(){
            return this.getSessionDuration;
        }

    },
}
</script>
<style lang="stylus">
#apie
    .pie-holder
        max-width 100vw
        overflow-x auto
</style>

