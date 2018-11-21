<template>
    <div class="homework-form">
        <form @submit.prevent="validateBeforeSubmit">
            <div class="form-group">
                <dtpicker :disable-time="true" :dark="isDark" :without-header="true" v-model="assignment.submission_date" format="YYYY-MM-DD" :auto-close="true" formatted="dddd, MMMM DD, YYYY" label="Submission date"></dtpicker>
                <div>
                    <input type="hidden" v-model="assignment.submission_date" name="submission_date" v-validate="requiredDate" >
                    <div class="md-error" v-show="errors.has('submission_date')">
                        <span class="text-danger">{{ errors.first('submission_date') }}</span>
                    </div>
                </div>
                <hr>
            </div>
            <md-field :md-theme="getTheme">
                <label for="subject">Subject</label>
                <md-select v-model="assignment.subject" name="subject" id="subject">
                    <md-option v-for="subject in subjects" :value="subject.id" :key="subject.id">{{subject.name}}</md-option>
                </md-select>
            </md-field>
            <md-field class="md-invalid">
                <label>description</label>
                <md-textarea v-model="assignment.description" md-autogrow v-validate="'required|min:10|max:200'" name="description" ></md-textarea>
                <div class="md-error" v-show="errors.has('description')">
                    <span class="text-danger">{{ errors.first('description') }}</span> 
                </div>
            </md-field>
            <div class="form-group clearfix">
                <button type="submit" class="btn btn-primary float-right">Submit</button>
            </div>
        </form>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
export default {
    name : "HomeworkForm",
    created(){
       this.init(); 
    },
    props:{
        subjects : {
            type : Array,
            required : true,
        },
        homework : {
            type : Object,
            default : ()=>{
                return {}
            }
        },
        session:{
            type : Object,
            required : true
        }
    },
    data: () =>({
        assignment : {}
    }),
    computed:{
        ...mapGetters([
            'getTheme'
        ]),
        isDark(){
            return this.getTheme == 'dark';
        },
        requiredDate(){
            let today = moment().format("YYYY-MM-DD"),
                sessionEnd = moment(this.session.end_date, "YYYY-MM-DD").format("YYYY-MM-DD");
            return `date_format:YYYY-MM-DD|date_between:${today},${sessionEnd}`;
        }
    },
    methods:{
        init(){
            if(!this.homework.id){
                this.$validator.reset();
                this.$validator.resume();
                this.assignment = {
                    description: '',
                    subject: '',
                    assigned_date:moment().format("YYYY-MM-DD"),
                    submission_date:moment().add(1,'d').format("YYYY-MM-DD")
                }
            }
            else{
                this.assignment = _.cloneDeep(this.homework);
                this.assignment.subject = this.homework.subject.id;
            }
        },
        validateBeforeSubmit() {
            this.$validator.validateAll().then((result) => {
                if (result) {
                    let assignment = _.cloneDeep(this.assignment);
                    this.$emit("form-submit",assignment);
                    this.$nextTick(() => {
                        this.$validator.reset();
                        this.$validator.resume();
                        
                    });
                    return;
                }
            });
        }
    },
    watch:{
        homework(val){
            this.init();
        }
    }

}
</script>
<style lang="stylus">

</style>
