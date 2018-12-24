<template>
    <div id="homeWorkEdit">
        <transicion :isLoading="isLoading">
            <section>
                <homework-list :classroomId="this.classroom.id" :editable="true" @add-homework="addHomework" @homework-click="homeworkClicked($event)"></homework-list>
                <div>
                    <modal ref="modal" :enable-mobile-fullscreen="true" :modal-theme="getTheme" :overlay-theme="getTheme">
                        <div class="d-flex justify-content-center">
                            <div class="col col-lg-10 py-2 text-left p-0">
                                <div class="new-homework" v-if ="isNew" key='new'>
                                    <h4>New Homework</h4>
                                </div>
                                <div class="edit-home d-flex align-items-center justify-content-between" v-else key='update'>
                                    <div class="col-auto p-0">
                                        <h4 class="m-0">Edit Homework</h4>
                                    </div>
                                    <div class="col-auto p-0" @click="confirmDelete"> 
                                        <p><span class="fas fa-trash fa-lg fa-fw"></span></p>
                                    </div>
                                </div>
                                <hr>
                                <homework-form :subjects="subjects" :session="session"
                                @form-submit="submitHomework($event)" :homework="homework"></homework-form>
                            </div>
                        </div>
                    </modal>
                    <modal ref="nestedChild">
                        <confirm-action @confirm="removeHomework" v-if="!isNew">
                            <h5 class="mb-4"> Are you sure you want to delete {{this.homework.subject.name}} homework </h5>
                     </confirm-action>
                    </modal>
                </div>
            </section>
        </transicion>
    </div>
</template>
<script>
import { SweetModal } from 'sweet-modal-vue';
import homeworkForm from '../components/homework-form.vue';
import loader from '../../../components/loader.vue';
import confirmAction from '../../../components/confirm-action.vue';
import transicion from '../../../components/transicion.vue';
import homeworkList from './HomeworkList.vue';
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "HomeWorkEdit",
    created(){
        this.fetchClassroomSubjects(this.classroom.id).then( subjects => {
            this.subjects = subjects;
            this.isLoading = false;
        });
    },
    data(){
        return {
            subjects : [],
            isLoading : true,
            homework:{}
        }
    },
    components:{
        modal : SweetModal,
        homeworkForm,
        homeworkList,
        loader,
        transicion,
        confirmAction
    },
    computed : {
        ...mapGetters([
            'getTheme'
        ]),
        ...mapGetters('classroom', {
            classroom : 'getClassroom'
        }),
        ...mapGetters('profile',{
            profile : 'getProfile'
        }),
        ession (){
            return this.classroom.session;
        },
        isNew(){
            return this.homework.id == undefined;
        }
    },
    methods : {
        ...mapActions('classroom', [
            'fetchClassroom',
            'fetchClassroomSubjects'
        ]),
        ...mapActions('homework',[
            'saveHomework',
            'updateHomework',
            'deleteHomework'
        ]),
        show () {
            this.$refs.modal.open(); 
        },
        hide () {
            this.$refs.modal.close(); 
        },
        addHomework(){
            this.homework = {};
            this.show();
        },
        homeworkClicked(_homework){
            this.homework = _homework;
            this.show();
        },
        confirmDelete(){
            this.$refs.nestedChild.open(); 
        },
        removeHomework(canDelete){
            this.$refs.nestedChild.close(); 
            if(canDelete)
            {
                this.deleteHomework(this.homework).then( response => {
                    console.log(response, 'deleted');
                });
                this.hide();
            }
        },
        submitHomework(_homework){
            this.hide();
            if(_homework.id){
                this.updateHomework(_homework).then( hw => {
                    console.log('updated');
                });
            }
            else{
                let homework = _homework;
                homework.teacher = this.profile.user;
                homework.classroom = this.classroom.id;
                this.saveHomework(homework).then( hw => {
                    console.log(hw, 'saved'); 
                });
            }
        }
    }
}
</script>

<style lang="stylus">
</style>

