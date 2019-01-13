<template>
    <div id="subjectResult">
        <div v-if="assessments.length > 0">

            <!-- <h5 class="font&#45;weight&#45;bold my&#45;3">Results</h5> -->
            <div class="">
                <div class="my-3">
                    <h4 class="font-weight-bold m-0">Results</h4>
                    <p class="color_4 m-0" v-html="resultDisplayed"></p>
                </div>
                <hr/>
                <div class="d-flex flex-wrap justify-content-md-center" v-if="terms.length > 1">
                    <div class="col-12 px-0 text-center">
                        <h6 class="mb-0 font-weight-bold">Select Term</h6>
                    </div>
                    <div class="col-md-auto px-0">
                        <md-radio v-model="term" value="" >All</md-radio>
                    </div>
                    <div class="col-md-auto px-0" v-for="_term in terms" :key="_term.id">
                        <md-radio v-model="term" :value="_term.id" >{{_term.fullName}}</md-radio>
                    </div>
                </div>
            </div>
            <hr/>
            <div class=" text-center py-3">
                <h5 class="font-weight-bold m-0 color_4" :style="{color:` ${subject.color}`}">Average Score</h5>
                <p class="color_3 m-0">{{subject.name}} average score summary</p>
                <div class="chart-holder py-3 text-center">
                    <arc-chart title="gradeChart" :width="300" :height="300" label="" :percentage="totalAverage"
                        :color="colors(totalAverage)" > </arc-chart>
                    <p> Percentage average score for <span class="text-capitalize">{{subject.name}}</span> </p>
                </div>
            </div>
            <hr/>
            <div class="d-flex flex-wrap justify-content-around py-3 text-center">
                <div class="col-12 pb-3">
                    <h5 class="font-weight-bold m-0" :style="{color:` ${subject.color}`}">Result Summary</h5>
                    <p class="color_3 m-0">{{subject.name}} minimum and maximum scores</p>
                </div>
                <div class="col-auto py-5">
                    <h5 class="font-weight-bold text-capitalize m-0 color_4"> Minimum Score</h5>
                    <h1 class="display-2 font-weight-bold m-0 color_4">{{summary.minScore}}</h1>
                    <p class="color_3">Minimum percentage score obtained in <br/> {{subject.name}}</p>
                </div>
                <div class="col-auto py-5">
                    <h5 class="font-weight-bold text-capitalize m-0 color_4">Maximum Score</h5>
                    <h1 class="display-2 font-weight-bold m-0 color_4">{{summary.maxScore}}</h1>
                    <p class="color_3">Maximum percentage score obtained in <br/> {{subject.name}}</p>
                </div>
            </div>
            <hr/>
            <div class="d-flex flex-wrap justify-content-center py-3">
                <div class="col-12 text-center">
                    <h5 class="font-weight-bold m-0 color_4" :style="{color:` ${subject.color}`}">Assessment Averages</h5>
                    <p class="color_3">{{subject.name}} assessments and their average scores</p>
                </div>
                <div class="col  " v-for="(average,key) in assessmentAverages">
                    <div class="chart-holder py-5 py-lg-3 text-center">
                        <h5 class="font-weight-bold mb-3 color_4">{{key}}</h5>
                        <arc-chart :title="key" :width="250" :height="250" label="" :percentage="average"
                            :color="colors(average)" > </arc-chart>
                        <p class="m-0 color_3"> <span clas="text-capitalize ">{{key}}</span> Percentage average scores </p>
                    </div>
                </div>
            </div>
            <hr/>
            <div class="text-center py-3">
                <h5 class="font-weight-bold m-0 color_4" :style="{color:` ${subject.color}`}">Score Distribution</h5>
                <p class="color_3 m-0">{{subject.name}} students average score distribution</p>
                <div class="histogram-holder txt-center">
                    <histogram title="frequency" :width="500" :height="400" :data="histogramData" class="" :padding="0.1" :showGuide="true"> </histogram>
                </div>
                <p class="m-0 color_3"> Students percentage average scores distribution </p>
            </div>
        </div>
        <div v-else class="d-flex justify-content-center align-items-center" > 
            <div class="text-center col-auto py-4">
                <h1 class="color_2 mb-5">
                    <span class="color_2 fa-layers fa-fw fa-3x" style="vertical-align: top;">
                        <i class="fas fa-ban" data-fa-transform="grow-7"></i>
                        <i class="fas fa-chart-bar" data-fa-transform="shrink-7"></i>
                    </span>
                </h1>
                <h3 class="color_3 text-uppercase">No Results</h3>
                <h6 class="color_3 text-upperase" style="line-height : 1.3em !important">{{subject.name}} does not have
                    any results yet</h6>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapMutations} from 'vuex';
import histogram from '../../../components/histogram.vue'
import arcChart from '../../../components/arc_chart.vue'
export default{
    name : "SubjectResult",
    computed : {
        ...mapGetters('subject', {
            subject : 'getSubject',
            histogramData : 'getHistogramData',
            assessments : 'getAssessments',
            assessmentAverages : 'getAssessmentAverageScore',
            totalAverage : 'getTotalAverageScore',
            terms : 'getTerms',
            summary : 'getResultSummary'
        }),
        ...mapGetters('grade', [ 'getGrader']),
        ...mapGetters({'color':'getColor'}),
        grade(){
            return this.getGrader.gradeScale(this.totalAverage);
        },
        // color(){
        //     return this.getGrader.gradeColors[this.grade];
        // },
        percentage(){
            return this.getTotalAverageScore;
        },
        resultDisplayed(){
            let term = _.find(this.terms , {id : this.term}),
                display = '';
            if(!!term)
                return `Displaying results for <span style="color: ${this.subject.color} !important; ">${_.startCase(term.fullName)}</span>`
            return `Displaying combined results for <span style="color: ${this.subject.color} !important; ">All terms</span>`
        }
    },
    data(){
        return {
            term : '',
        }
    },
    components : {
        histogram,
        arcChart
    },
    methods : {
        ...mapMutations('subject', ['setTerm']),
        colors(score){
            let grade = this.getGrader.gradeScale(score);
            return this.getGrader.gradeColors[grade];
        }
    },
    watch:{
        term(val){
            this.setTerm(val);
        }
    }

}
</script>
<style lang="stylus">
#subjectResult
    .histogram-holder
        max-width 100vw
        overflow-x auto

</style>
