<template>
    <div id="assessmentDetail" >
        <transicion :isLoading="loading">
        <div class="d-flex flex-wrap">
            <div class="col-lg-4 col-xl-3 px-0 bg_0 order-lg-2">
                <div class="p-3 d-lg-none">
                    <button @click="show" class="btn btn-block btn-primary">show filters</button>
                </div>
               <div class="py-3 d-none d-lg-block">
                    <div class="p-3">
                        <h4 class="font-weight-bold ">Filters</h4>
                        <hr >
                    </div>
                    <div class="col-lg">
                        <div class="form-group">
                            <label for="session" class="color_5">Session</label>
                            <select v-model="session" name="session" id="session" class="form-control form-control-sm">
                                <option v-for="session in sessions" :value="session.id" :key="session.id">{{session.name}}</option>
                            </select>
                        </div>
                    </div>
                    <div class="col-lg">
                        <div class="form-group">
                            <label for="classrooms" class="color_5">Classroom</label>
                            <select v-model="classroom" name="classroom" id="classroom" class="form-control form-control-sm">
                                <option v-for="classroom in classrooms" :value="classroom.id"
                                        :key="classroom.id">{{classroom.className}}</option>
                            </select>
                        </div>
                    </div>
                    <div class="col-lg">
                        <div class="form-group">
                            <label for="terms">Term</label>
                            <select v-model="term" name="term" id="term" class="form-control form-control-sm">
                                <option v-for="term in terms" :value="term.id"
                                        :key="term.id">{{term.fullName}}</option>
                            </select>
                        </div>
                    </div>
                    <div class="col-lg">
                        <div class="form-group">
                            <label for="baseSubjects">Base Subject</label>
                            <select v-model="baseSubject" name="baseSubjects" id="baseSubjects" class="form-control
                            form-control-sm">
                                <option v-for="subject in baseSubjects" :value="subject.id"
                                        :key="subject.id">{{subject.name}}</option>
                            </select>
                        </div>
                    </div>
                    <div class="col-lg">
                        <div class="form-group">
                            <label for="subjects">Subject</label>
                            <select v-model="subject" name="subjects" id="subjects" class="form-control form-control-sm">
                                <option v-for="subject in subjects" :value="subject.id"
                                        :key="subject.id">{{subject.name}}</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg order-lg-1 bg_0 table-pane py-2">
                <vue-good-table :columns="columns" :rows="rows" @on-row-click="onRowClick" :search-options="{enabled:true}" :skipDiacritics="true"/>
            </div>
            <section>
                <modal ref="modal" @close="onClose" :enable-mobile-fullscreen="true" :modal-theme="getTheme" :overlay-theme="getTheme"
                       class="full-height" >
                       <div v-if="enrollment">
                           <enrollment-result :enrollment="enrollment" @update="updated"></enrollment-result>
                       </div>
                       <div v-else>
                           <div class="py-3">
                               <div class="col-lg">
                                   <div class="form-group">
                                       <label for="session" class="color_5">Session</label>
                                       <select v-model="session" name="session" id="session" class="form-control form-control-sm">
                                           <option v-for="session in sessions" :value="session.id" :key="session.id">{{session.name}}</option>
                                       </select>
                                   </div>
                               </div>
                               <div class="col-lg">
                                   <div class="form-group">
                                       <label for="classrooms" class="color_5">Classroom</label>
                                       <select v-model="classroom" name="classroom" id="classroom" class="form-control form-control-sm">
                                           <option v-for="classroom in classrooms" :value="classroom.id"
                                                   :key="classroom.id">{{classroom.className}}</option>
                                       </select>
                                   </div>
                               </div>
                               <div class="col-lg">
                                   <div class="form-group">
                                       <label for="terms">Term</label>
                                       <select v-model="term" name="term" id="term" class="form-control form-control-sm">
                                           <option v-for="term in terms" :value="term.id"
                                                   :key="term.id">{{term.fullName}}</option>
                                       </select>
                                   </div>
                               </div>
                               <div class="col-lg">
                                   <div class="form-group">
                                       <label for="baseSubjects">Base Subject</label>
                                       <select v-model="baseSubject" name="baseSubjects" id="baseSubjects" class="form-control
                                       form-control-sm">
                                           <option v-for="subject in baseSubjects" :value="subject.id"
                                                   :key="subject.id">{{subject.name}}</option>
                                       </select>
                                   </div>
                               </div>
                               <div class="col-lg">
                                   <div class="form-group">
                                       <label for="subjects">Subject</label>
                                       <select v-model="subject" name="subjects" id="subjects" class="form-control form-control-sm">
                                           <option v-for="subject in subjects" :value="subject.id"
                                                   :key="subject.id">{{subject.name}}</option>
                                       </select>
                                   </div>
                               </div>
                           </div>
                       </div>
                </modal>
            </section>
        </div>
        </transicion>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import { SweetModal } from 'sweet-modal-vue';
import transicion from '../../../components/transicion.vue';
import enrollmentResult from '../components/enrollment-result.vue';
export default{
    name : 'assessmentDetail',
    created(){
        this.fetchData();
    },
    data(){
        return {
            session : '',
            classroom:'', 
            term : '',
            baseSubject : '',
            subject : '',
            enrollmentId : '',
            loading : true
        }
    },
    computed : {
        ...mapGetters(['getTheme']),
        ...mapGetters('assessment', {
            enrollments:'getEnrollmentsBySubject',
            sessions : 'getSessions',
            classrooms : 'getClassroomsBySession',
            terms : 'getTermsBySession',
            baseSubjects : 'getBaseSubjects',
            subjects : 'getSubjectsByBaseNSession',
            'rows' : 'getResultSheet',
            'columns' : 'getResultColumn'
        }),
        enrollment(){
            return _.find(this.enrollments, {id : this.enrollmentId})
        }
    },
    components : {
        modal : SweetModal,
        enrollmentResult,
        transicion
    },
    methods:{
        ...mapActions('assessment',['fetchEnrollments','fetchEnrollmentResults']),
        ...mapActions('term',['fetchTerms']),
        ...mapMutations('assessment',['setSession', 'setClassroom','setTerm', 'setBaseSubject', 'setSubject']),
        fetchData(){
            let schoolId = this.$route.params.schoolId;
            Promise.all([this.fetchEnrollmentResults(schoolId),this.fetchTerms(schoolId)]).then(enrollments => {
                // set up session
                let session = _.find(this.sessions , {'is_current':true})
                if( !session && this.sessions.length  > 0) session = this.sessions[0];
                if(session){
                    this.session = session.id;
                    this.setSession(this.session);
                }
                // set classroom
                if(this.classrooms.length > 0){
                    this.classroom = this.classrooms[0].id;
                    this.setClassroom(this.classroom);
                }

                // set term
                let term = _.find(this.terms , {'is_current':true})
                if( !term && this.terms.length  > 0) term = this.terms[0];
                if(term){
                    this.term = term.id;
                    this.setTerm(this.term);
                }

                //set subject
                if(this.baseSubjects.length > 0){
                    this.baseSubject = this.baseSubjects[0].id;
                    this.setBaseSubject(this.baseSubject);
                }

                //set subject
                if(this.subjects.length > 0){
                    this.subject = this.subjects[0].id;
                    this.setSubject(this.subject);
                }        
                this.loading = false;
            });
        },
    show (){
        this.$refs.modal.open();
    },
    hide (){
        this.$refs.modal.close();
    },
    onRowClick(params){
        this.enrollmentId = params.row.enrollment;
        this.show();
    },
    onClose(){
        this.enrollmentId = '';
    },
    updated(){
        this.hide();
    }
    },
    watch:{
        session(val){
            this.setSession(val);
        },
            classroom(val){
                this.setClassroom(val);
            },
            term(val){
                this.setTerm(val);
            },
            baseSubject(val){
                this.setBaseSubject(val);
            },
            subject(val){
                this.setSubject(val);
            },
    }
}
</script>
<style lang='stylus'>
#assessmentDetail
    .full-height
        .sweet-modal
            height 100vh
    .table-pane
        max-height 90vh
        overflow-y auto
</style>

