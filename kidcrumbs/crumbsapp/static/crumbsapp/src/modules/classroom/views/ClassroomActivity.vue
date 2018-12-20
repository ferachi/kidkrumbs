<template>
    <div id="ClassroomActivity" class="">
        <transition :name="anim" mode="out-in">
            <div v-if="isList" key="list">
                <section class="list-header">
                    <div class="d-flex justify-content-between align-items-center pb-3">
                        <div class="col-auto px-2">
                            <h4 class="m-0 font-weight-bold text-upperase"> Activities </h4>
                        </div>
                        <div class="col-auto px-2 d-none d-sm-block">
                            <h1 class="font-weight-bold m-0 text-right">{{activityCount}}</h1>
                            <p class="color_3 m-0 text-right">Total classroom activities</p>
                        </div>
                    </div>
                </section>
                <hr>
                <section>
                    <activities :schoolSlug="schoolSlug" :groupId="classroom.id" @view-click="viewActivity($event)"></activities>
                </section>
            </div>
            <div v-else key="detail">
                    <div class="">
                        <md-button class="md-primary" @click="backBtnClicked"><i class="fas fa-arrow-left fa-fw"></i> back to list</md-button>
                    </div>
                <activity-detail :id="activity.id" :editable="true"></activity-detail>
            </div>
        </transition>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
import activities from '../components/activities.vue';
import activityDetail from '../components/activityDetail.vue';
export default {
    name: "ClassroomActivity",
    components : {
        activities,
        activityDetail
    },
    computed : {
        ...mapGetters('classroom', {classroom : 'getClassroom'}),
        ...mapGetters('group', {activities : 'getGroupActivities'}),
        ...mapGetters('profile', {profile : 'getProfile' }),
        schoolSlug(){
            let school = this.profile.schools.find(school => school.id == this.classroom.group_base.school);
            return school.slug;
        },
        activityCount(){
           return this.activities.length; 
        }
    },
    data(){
        return {
            isList : true,
            activity : {},
            anim : 'fade-right'
        }
    },
    methods : {
        viewActivity(activity){
            this.activity = activity;
            this.anim='fade-right';
            this.isList=false;
        },
        backBtnClicked(){
            this.isList = true;
            this.anim='fade-left';
            this.activity = {};
        }
    }
};
</script>
<style lang="stylus">
</style>
