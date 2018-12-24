<template>
    <div id="activityDateDetail">
        <section class="date-filter">
            <dtpicker :disable-time="true" :dark="isDark" :without-header="true" v-model="date" format="YYYY-MM-DD" :auto-close="true" formatted="dddd, MMMM DD, YYYY" label="Select date"></dtpicker>
        </section>
        <hr>
        <section class="activity-detail" v-if="activity">
            <activity-detail :id="activity.id"></activity-detail>
        </section>
        <section class="detail-not-found d-flex justify-content-center align-items-center" v-else>
            <div class="text-center col-auto">
                <h1 class="display-2 color_2"><i class="fas fa-people-carry fa-fw"></i></h1>
                <h3 class="color_3 text-uppercase">No Activities Today</h3>
            </div>
        </section>
    </div>
</template>
<script>
import page from "../../../components/page.vue"
import {mapGetters} from 'vuex';
import activityDetail from "./ActivityDetail.vue"
export default{
    name : "ActivityDateDetail",
    created(){
        this.init();
    },
    props:{
        groupId : String,
        required : true
    },
    data(){
        return {
            date : moment().format("YYYY-MM-DD"),
            activities : [],
        }
    },
    components:{
        activityDetail
    },
    computed:{
        ...mapGetters('group', {
            group:'getGroup'
        }),
        ...mapGetters('activity',[
            'getActivitiesByGroup',
            'getActivityByDate'
        ]),
        ...mapGetters([
            'getTheme'
        ]),
        isDark(){
            return this.getTheme == 'dark';
        },
        activity(){
            return _.find(this.activities, _act => {
                return _act.date == this.date;
            });
        }
    },
    methods:{
        init(){
            this.date = this.$route.params.date;
            this.activities = this.getActivitiesByGroup(this.groupId);
        }
    },
    watch : {
        '$route'(to, from) {
            this.init();
        },
        date(){
            this.$router.push({name : 'activityDetailByDate', params:{date: this.date}})
        },
        groupId(){
            this.init();
        }
    }
}
</script>
<style lang="stylus">
#activityDateDetail
    .detail-not-found
        min-height 40vh
</style>

