<template>
    <div id="ClassroomActivity" class="">
        <transition :name="anim" mode="out-in">
            <div v-if="isList" key="list">
                <activities :schoolSlug="schoolSlug" :groupId="classroom.id" @view-click="viewActivity($event)"></activities>
            </div>
            <div v-else key="detail">
                <div>
                    <button class="btn btn-primary" @click="backBtnClicked">Back to activities</button>
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
        ...mapGetters('profile', {profile : 'getProfile' }),
        schoolSlug(){
            let school = this.profile.schools.find(school => school.id == this.classroom.group_base.school);
            return school.slug;
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
