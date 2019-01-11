<template>
    <div id="enrollmentResults" >
        <div class="">
                <avatar :image="student.avatar"></avatar>
                <h5 class="m-0 mb-3 font-weight-bold">{{student.names}}</h5>
                <h6 class="color_4 m-0 font-weight-bold">{{subject}}</h6>
                <p class="color_3 m-0" v-if="term">{{term.fullName}} {{term.session.year}}</p>
                <form @submit.prevent="validateBeforeSubmit" novalidate>
                <div v-for="(assessment,index) in assessments" >
                    <result-input :index="index" :result="assessment.result" :label="assessment.type" :maxScore="assessment.maxScore" :term="term"></result-input>
                </div>
                <div class="text-right">
                    <button class="btn btn-primary" >update</button>
                </div>
                </form>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import resultInput from './result-input.vue';
import avatar from '../../../components/avatar.vue';
export default{
    name : 'enrollmentResults',
    created(){
        this.assessmentResult = this.result;
    },
    props:['enrollment'],
    data(){
        return {
        }
    },
    computed : {
        ...mapGetters('assessment', {termId : 'getTerm'}),
        ...mapGetters('term', {terms : 'getTerms'}),
        enrollmentAssessments(){
            return this.enrollment.assessments;
        },
        subject(){
            return this.enrollment.subject.name;
        },
        student(){
            return this.enrollment.student;
        },
        term(){
            return _.find(this.terms, {id : this.termId});
        },
        assessments(){
            let assessments;
            if(_.isEmpty(this.termId)) 
                assessments = this.enrollmentAssessments;
            else
                assessments = _.filter(this.enrollmentAssessments, (assessment) =>{
                    return assessment.term.id == this.termId;
                })
            return _.map(assessments, (assessment) => {
                
                let result= _.find(assessment.assessment_results, _res =>{
                    return _res.enrollment == this.enrollment.id && _res.assessment == assessment.id;    
                });
            
                if(!result) {
                    let date = moment().format("YYYY-MM-DD");
                    result = { assessment : assessment.id, enrollment : this.enrollment.id, score : ''}
                }
                return {
                    type : assessment.assessment_type.name,
                    maxScore : assessment.max_score,
                    result : result
                }
            });
        },
        results(){
            let _results = _.map(this.assessments, assessment => assessment.result);  
            return _.filter(_results , result =>  !_.isEmpty(result.score));
        }
    },
    components : {
        resultInput,
        avatar
    },
    methods:{
        ...mapActions('assessment', ['saveResults']),
        validateBeforeSubmit(){
            this.$validator.validateAll().then(result =>{
                if(result){
                    this.saveResults(this.results).then(results => {
                        this.$emit('update');
                    });
                }
                else{
                    console.log(this.errors, this.fields)
                    alert('Correct them errors!');
                }
            })
        },
    },
}
</script>
<style lang='stylus'>
</style>

