<template>
    <div id="summaryLine" class="">
        <div class="p-1 d-flex align-items-center flex-wrap">
            <div class="col-lg-2 col-10 px-0">
                <small class="m-0 color_3">Minimum Score</small>
            </div>
            <div class="col-10 px-0">
                <grade-bar :width="width" :height="height" :score="minResult.score" title="min scores" :grading="grades">
                    <p slot-scope="{color}" class="m-0"><span class="font-weight-bold " :style="{color : `${color} !important`}">{{minResult.score}}</span></p>
                </grade-bar>
            </div>
        </div>
        <div class="p-1 d-flex align-items-center flex-wrap">
            <div class="col-lg-2 col-10 px-0">
                <small class="m-0 color_3">Maximum Score</small>
            </div>
            <div class="col-10 px-0">
                <grade-bar :width="width" :height="height" :score="maxResult.score" title="max scores" :grading="grades">
                    <p slot-scope="{color}" class="m-0"><span class="font-weight-bold " :style="{color : `${color} !important`}">{{maxResult.score}}</span></p>
                </grade-bar>
            </div>
        </div>
        <div class="p-1 d-flex flex-wrap align-items-center">
            <div class="col-lg-2 col-10 px-0">
                <small class="m-0 color_3">Total Score</small>
            </div>
            <div class="col-10 px-0">
                <grade-bar :width="width" :height="height" :score="averageScore"
                    title="total scores" :grading="grades">
                    <p class="color_3 m-0" slot-scope="{color}"><span class="font-weight-bold" :style="{color : `${color} !important`}">{{totalScore}}</span>/{{totalAssessment}}</p>
                </grade-bar>
            </div>
        </div>
        <div class="mt-3">
            <p style="line-height : 1.3;"><small><span class="font-weight-bold">Displaying </span><br>
                - Minimum and maximum scores ever obtained in any term by this student. <br>
                - Total scores obtained by this student.
                </small></p>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import gradeBar from '../../../components/grade_bar.vue'
export default{
    name : "resultSummaryBar",
    created(){
    },
    data(){
        return {
            gradeScale : null,
            width : 210,
            height : 6
        }
    },
    components : {
        gradeBar
    },
    computed : {
        ...mapGetters('result', {
            averageScore:'getTotalAverageScore',
            totalScore:'getTotalScores',
            totalAssessment:'getTotalAssessmentScores',
            minResult : 'getMinResult',
            maxResult : 'getMaxResult'
        }),
        ...mapGetters('grade', [ 'getGrades']),
        grades(){
            let _grades = _.cloneDeep(this.getGrades),
            minGrade = _.minBy(_grades, 'minScore'),
            maxGrade = _.maxBy(_grades, 'maxScore'),
            colorScale = d3.scaleLinear().domain([minGrade.minScore, maxGrade.maxScore]).range([minGrade.color, maxGrade.color])
            return _.map(_grades, grade => {
                grade.color = colorScale(grade.maxScore)
                return grade;
            })
        }
    },
}
</script>
<style lang="stylus">
</style>

