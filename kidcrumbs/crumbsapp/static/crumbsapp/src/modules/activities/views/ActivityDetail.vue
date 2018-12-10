<template>
    <div v-if="isLoading"  key="loading"></div>
    <div v-else id="activityDetail" key="loaded" class="mx-2">
        <div class="d-flex">
            <tab-head class="col" :tabTitles="['activity', 'comment']" justify="justify-content-end" @tab-click="tabClicked($event)"></tab-head>
        </div>
        <div class="tabs">
            <div v-if="selectedTab == tabTitles[0]">
                <section class="activity-head">
                    <h5>Teachers' Comment</h5>
                    <p>{{activity.note}}</p>
                </section>
                <section class="activities-pane">
                    <activityItems :canEdit="editable" :activityId='activity.id' :activities="activity.activities"
                    :school="activity.school" ></activityItems>
                </section>
            </div>
            <div v-else-if="selectedTab == tabTitles[1]">
                <section class="activity-head">
                    <h5>Teachers' Comment</h5>
                    <p>{{activity.note}}</p>
                </section>
                <section class="comments-pane">
                <comment :comments="comments" @add-comment="addComment($event)" @reply-comment="replyComment($event)"></comment>
                </section>
            </div>
            <div v-else></div>
        </div>
    </div>
</template>
<script>
import tabHead from '../../../components/tabHead.vue';
import comment from '../../../components/Comment.vue';
import activityItems from '../components/ActivityItems.vue';
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "ActivityDetail",
    created(){
        this.init();
    }, 
    props:{
        editable : {
            type : Boolean,
            default : false
        },
        id : {
            type : String,
            required : true
        }
    },
    components : {
        tabHead,
        activityItems,
        comment
    },
    computed:{
        ...mapGetters("activity",{
            activity : "getActivity"
        }),
        ...mapGetters("profile",{
            profile : "getProfile"
        }),
        comments(){
            return this.activity.comments;
        }
    },
    data: () => ({
        tabTitles : [ 'activity', 'comment'],
        selectedTab : 'activity',
        isLoading : true
    }),
    methods:{
        ...mapActions('activity', [
            'saveComment',
            'saveReplyComment',
            'pullActivity'
        ]),
        tabClicked(tab){
            this.selectedTab = tab;
        },
        addComment(_comment){
            let data = {activity : this.activity.id, person : this.profile.user, comment : _comment}
            this.saveComment(data);
        },
        replyComment(reply){
            let data = {activity_comment : reply.comment.id, person: this.profile.user, comment:reply.data}; 
            this.saveReplyComment(data);
        },
        init(){
            this.pullActivity(this.id).then(activity =>{
                this.isLoading = false;
            });
        }, 
    },
    watch:{
        '$route'(to ,from ){
            this.init();
        }
    }
}
</script>
<style lang="stylus">
</style>

