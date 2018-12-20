<template>
        <transicion :isLoading="loading">
        <div id="ClassroomList" class="">
            <page>
            <div slot="header">
                <page-header class="primary-bg border-bottom border_0 py-2">
                    <div slot="pageTitle" >
                        <h4 class="m-0 color_white">Select Classroom</h4>
                        <p class="m-0" style="margin-top : -5px !important"><small class="color_white">{{school.name}}</small></p>
                    </div>
                    <div slot="pageMenu"></div>
                </page-header>
            </div>
            <div class="list-content">
                <section>
                <div class="p-3 d-flex align-items-center justify-content-between">
                    <div class="col-auto p-0">
                        <h3 class="font-weight-bold text-uppercase m-0 color_4">Classrooms</h3>
                        <p class="m-0" v-if="sessions.length > 0"><a class="primary-color-light clickable" @click="show">change session</a> {{session.year}}</p>
                    </div>
                    <div class="col-auto p-0">
                        <h1 class="m-0 font-weight-bold color_5 display-3 text-right" style="margin-bottom : -15px
                        !important; margin-top:-15px !important;">{{classroomCount}}</h1>
                        <p class="m-0 color_3" style="margin-top:-5px !important">{{classroomCount |
                        pluralize('classroom')}}</p>
                    </div>
                </div>
                </section>
                <section class="px-2">
                    <div class="classroom-list">
                        <classrooms :classrooms="classrooms" @classroom-click="classroomClicked($event)"></classrooms> 
                    </div>
                </section>
                <section>
                    <modal ref="modal" :enable-mobile-fullscreen="true" :modal-theme="getTheme" :overlay-theme="getTheme">
                    <div>
                        <md-list>
                            <md-list-item v-for="_session in sessions" :key="_session.id" @click="changeSession(_session)">
                                <span class="md-list-item-text" :class="{'primary-color' : _session.id == session.id }">{{_session.year}}</span>
                            </md-list-item>
                        </md-list>
                    </div>
                    </modal>
                </section>
            </div>
            </page>
        </div>
        </transicion>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import { SweetModal } from 'sweet-modal-vue';
import transicion from '../../../components/transicion.vue';
import pageHeader from '../../../components/pageHeader.vue';
import page from '../../../components/page.vue';
import classrooms from '../components/classrooms.vue';
export default {
    name: "ClassroomList",
    created(){
        this.fetchData();
    },
    computed :{
        ...mapGetters('profile', {profile : 'getProfile'}),
        ...mapGetters('session', {session : 'getSession'}),
        ...mapGetters([ 'getTheme' ]),
        classroomCount(){
            return this.classrooms.length;
        },
        classrooms(){
            return _.sortBy(_.filter(this.classroomList, classroom => classroom.session.id == this.session.id), 'className');
        }
    },
    components:{
        transicion,
        classrooms,
        pageHeader,
        page,
        modal:SweetModal,
    },
    data(){
        return {
            classroomList : [],
            school: {},
            sessions : [],
            loading : true
        }
    },
    methods :{
        ...mapActions('school', ['fetchSchool']),
        ...mapActions('session', ['fetchSessions']),
        ...mapMutations('session', ['setSession']),
        ...mapActions('classroom', ['fetchClassrooms']),
        fetchData(){
            let schoolId = this.$route.params.id;
            Promise.all([this.fetchSchool(schoolId),this.fetchClassrooms(schoolId),this.fetchSessions(schoolId)])
            .then( props => {
                this.classroomList = props[1];
                this.school = props[0];
                this.sessions = props[2];

                let session = _.find(this.sessions, 'is_current');
                if(session == null || session == undefined ){
                    if(this.sessions.length > 0){
                        session = _.last(this.sessions)
                    }
                    else{
                        session = {}
                    }
                }
                this.setSession(session);
                this.loading = false;
            });
        },
        classroomClicked(classroom){
            this.$router.push({name : 'classroomDetail', params : {id : classroom.id}});
        },
        show () {
            this.$refs.modal.open(); 
        },
        hide () {
            this.$refs.modal.close(); 
        },
        changeSession(session){
            this.setSession(session); 
            this.hide();
        }
    }
};
</script>
<style lang="stylus">
#ClassroomList
    .list-content
        min-height 85vh
        padding-bottom 20px
        margin-bottom 20px
</style>
