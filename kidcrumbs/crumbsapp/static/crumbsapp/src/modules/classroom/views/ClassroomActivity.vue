<template>
    <div id="ClassroomActivity" class="">
        <div v-if="isList">
            <activities :schoolSlug="schoolSlug" :groupId="classroom.id" @view-click="viewActivity($event)"></activities>
        </div>
        <div v-else>
            <div>
                <button class="btn btn-primary" @click="backBtnClicked">Back to activities</button>
            </div>
            <activity-detail :id="activity.id" :editable="true"></activity-detail>
        </div>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
import activities from '../../activities/views/Activities.vue';
import activityDetail from '../../activities/views/ActivityDetail.vue';
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
            activity : {}
        }
    },
    methods : {
        viewActivity(activity){
            this.activity = activity;
            this.isList=false;
        },
        backBtnClicked(){
            this.isList = true;
            this.activity = {};
        }
    }
};
</script>
<style lang="stylus">
</style>
