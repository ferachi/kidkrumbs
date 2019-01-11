<template>
    <div id="resultInput" >
        <form >
            <div class="d-flex  align-items-center py-2">
                <div class="col">

                    <md-field>
                        <label >{{label}}</label>
                        <md-input v-model="assessmentResult.score" :name="fieldLabel" type="number"
                            v-validate="{max_value:maxScore}" :data-vv-as="label"></md-input>
        <span class="md-helper-text">{{label}} score should not be greater than {{maxScore}} </span>
                    </md-field>
                    <span v-show="errors.has(fieldLabel)" class="text-danger">{{ errors.first(fieldLabel) }}</span>
                </div>
                <div class="col">
                    <dtpicker v-model="assessmentResult.date_taken" :dark="theme" format="YYYY-MM-DD"
                    formatted="DD/MM/YYYY" label="date taken" :without-header="true" :auto-close="true" disable-time />
                    <input type="hidden" v-model="assessmentResult.date_taken"
                     v-validate="{dateTaken:true ,required :dateRequired}"
                    data-vv-as="date taken" :name="dateWritten" >
                    <span v-show="errors.has(dateWritten)" class="text-danger" >{{ errors.first(dateWritten) }}</span>
                </div>
        </div></form>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import { Validator } from 'vee-validate';
export default{
    name : 'resultInput',
    inject : ['$validator'],
    created(){
        let startDate = moment(this.term.start_date).format("Do MMMM YYYY"),
            endDate = moment(this.term.end_date).format("Do MMMM YYYY");
        Validator.extend('dateTaken', {
            getMessage: field => `The ${field} value should fall within ${startDate} - ${endDate}`,
            validate: value => {
                let isValid = moment(value, "YYYY-MM-DD").isBetween(moment(this.term.start_date, "YYYY-MM-DD"), moment(this.term.end_date,"YYYY-MM-DD") );
                return isValid;
            }
        });
        this.assessmentResult = this.result;
    },
    props:['result', 'label', 'maxScore', 'term', 'index'],
    data(){
        return {
            assessmentResult : null
        }
    },
    computed : {
        ...mapGetters(['getTheme']),
        theme(){
            return this.getTheme == 'dark';
        },
        dateWritten(){
            return `dateTaken${this.index}`;
        },
        fieldLabel(){
            return `${this.label}${this.index}`;
        },
        dateRequired(){
            return !_.isEmpty(this.assessmentResult.score) && _.isEmpty(this.assessmentResult.date_taken)
        }
    },
    components : {
    },
    methods:{
    }
}
</script>
<style lang='stylus'>
</style>

