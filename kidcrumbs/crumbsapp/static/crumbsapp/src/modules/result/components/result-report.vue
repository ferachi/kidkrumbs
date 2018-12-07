<template>
    <div id="resultReport">
        <div class="d-flex flex-wrap">
            <div class="col-xl-9 px-2">
                <div class="report-header px-3 pt-4 pb-3 bg_0 mb-1">
                    <h5 class="font-weight-bold m-0 text-uppercase">Session {{session}}</h5>
                    <p class="m-0"><span class="font-weight-bold">{{term}}</span> of <span class="primary-color">{{session}}</span> session</p>
                </div>
                <div class="bg_0" style="min-height : 60vh">
                    <vue-good-table :columns="report.columns" :rows="report.rows"/>
                </div>
            </div>
            <div class="col-xl-3 p-3 bg_0">
                <div>
                    <h5 class="font-weight-bold m-0">Result Summary</h5>
                    <p class="m-0"><span class="font-weight-bold">{{term}}</span> of <span class="primary-color">{{session}}</span> session</p>
                </div>
                <div class="controls mt-3">
                    <div class="d-flex">
                        <div class="col-6 px-1">
                            <md-field :md-theme="getTheme">
                                <label for="sessions">Sessions</label>
                                <md-select v-model="session" name="sessions" id="sessions" md-dense >
                                    <md-option v-for="session in sessions" :value="session" :key="session"> {{session}}</md-option>
                                </md-select>
                            </md-field>
                        </div>
                        <div class="col-6 px-1">
                            <md-field :md-theme="getTheme">
                                <label for="terms">Terms</label>
                                <md-select v-model="term" name="terms" id="terms" md-dense>
                                    <md-option v-for="term in terms" :value="term" :key="term">{{term}}</md-option>
                                </md-select>
                            </md-field>
                        </div>
                    </div>
                </div>
                <div class="summary">
                    <div class="text-center mb-3">
                        <arc-sum title="reportSummary" :width="250" :height="250" :label="`Overall Grade : ${summary.grade}`"
                                 :percentage="summary.average" :color="summary.color" > </arc-sum>
                    </div>
                    <div class="text-center py-4"  v-if="term != 'All'">
                        <h6 class="primary-color m-0">Position : {{position}} of {{studentCount}} </h6>
                        <p class="m-0"><small>Total Score</small> <span class="font-weight-bold"> {{summary.total}} </span><small>Of {{summary.maximum}}</small> </p>
                    </div>
                    <div class="d-flex">
                        <div class="col px-1 text-center">
                            <div class="bg_aux p-2">
                                <h6><small class="">Maximum Score</small></h6>
                                <h4 class="font-weight-bold">{{summary.maxScore.totalScore}}</h4>
                                <p class="m-0"><small>{{summary.maxScore.subject}}</small></p>
                            </div>
                        </div>
                        <div class="col px-1 text-center">
                            <div class="bg_aux p-2">
                                <h6><small>Minimum Score</small></h6>
                                <h4 class="font-weight-bold">{{summary.minScore.totalScore}}</h4>
                                <p class="m-0"><small>{{summary.minScore.subject}}</small></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import arcSum from '../../../components/arc_chart.vue'
export default {
    name : "ResultReport",
    created(){
        this.session= this.sessions[0];
    },
    components:{
        arcSum
    },
    data(){
        return {
            term : 'All', 
            session:null
        }
    },
    computed :{
        ...mapGetters(['getTheme']),
        ...mapGetters('result', {
            report : 'getTableReport',
            sessions : 'getResultSessions',
            resultTerms : 'getResultTerms',
            sessionReport : 'getReportBySession',
            summary:'getReportSummary'
        }),
        terms(){
            let _terms = _.cloneDeep( this.resultTerms );
            _terms.unshift('All');
            return _terms;
        },
        position(){
            return this.report.rows[0]._position;
        },
        studentCount(){
            return this.report.rows[0]._studentCount;
        }
    },
    methods:{
        ...mapMutations('result',['setReport'])
    },
    watch : {
        session(val){
            let session = {name: this.session}
            if(this.term != 'All')
                session['term'] = this.term
            this.setReport(this.sessionReport(session));

        },
        term(val){
            let session = {name: this.session}
            if(this.term != 'All')
                session['term'] = this.term
            this.setReport(this.sessionReport(session));
        }
    }
}
</script>
<style lang="stylus">
</style>
