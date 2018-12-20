<template>
    <div id="ClassroomMember" class="">
        <div>
            <div class="d-flex align-items-center justify-content-between">
                <div class="col-auto px-0">
                    <h4 class="font-weight-bold m-0 text-capitalize">{{displayedMembers}}</h4>
                </div>
                <div class="col-auto px-0">
                    <md-switch v-model="isStudents" class="md-primary m-0">Members</md-switch> 
                </div>
            </div>
            <hr>
            <transition :name="fader" mode="out-in">
                <div class="student-list" v-if="isStudents" key="students">
                    <people :people="students" @person-click="studentClicked($event)"></people>
                </div>
                <div class="teacher-list" v-else key="teachers">
                    <people :people="teachers"></people>
                </div>
            </transition>
        </div>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
import people from '../../../components/People.vue';
export default {
    name: "ClassroomMembers",
    components : {
        people,
    },
    computed : {
        ...mapGetters('classroom', {classroom : 'getClassroom',members : 'getClassroomMembers'}),
        ...mapGetters('group', {getStudents : 'getGroupStudents'}),
        ...mapGetters('profile', {profile : 'getProfile' }),
        students(){
            return _.sortBy(this.getStudents, 'names');
        },
        teachers(){
           return _.differenceBy(this.members, this.students, 'names'); 
        },
        displayedMembers(){
            return this.isStudents ? 'students' : 'teachers';
        },
        fader(){
            return !this.isStudents ? 'fade-right' : 'fade-left';
        }
    },
    data(){
        return {
            isStudents : true
        }
    },
    methods : {
        studentClicked(student){
            this.$router.push({name : 'child', params : { username : student.username} } );
        }
    }
};
</script>
<style lang="stylus">
</style>
