<template>
    <div id="activityDateDetail">
        <section class="date-filter">
            <dtpicker :disable-time="true" :dark="isDark" :without-header="true" v-model="date" format="YYYY-MM-DD" :auto-close="true" formatted="dddd, MMMM DD, YYYY" label="Select date"></dtpicker>
        </section>
        <section class="activity-detail" v-if="activity">
            <activity-detail :id="activity.id"></activity-detail>
        </section>
        <section class="detail-not-found" v-else>
           <h1 class="display-3">Not Found</h1>  
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
        console.log(this.group)
        this.activities = this.getActivitiesByGroup(this.group.id);
        this.init();
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
        }
    },
    watch : {
        '$route'(to, from) {
            this.init();
        },
        date(){
            this.$router.push({name : 'activityDetailByDate', params:{date: this.date}})
        }
    }
}
</script>
<style lang="stylus">
</style>

