<template>
    <div v-if="isLoading"  key="loading"></div>
    <div v-else id="activityDetail" key="loaded">
        <div class="d-flex">
            <p class="primary-color col-auto">Date</p>
            <tab-head class="col" :tabTitles="['activity', 'comment']" justify="justify-content-end" @tab-click="tabClicked($event)"></tab-head>
        </div>
        <div class="tabs">
            <div v-if="selectedTab == tabTitles[0]">
                <div>
                    <h5>Teachers' Comment</h5>
                    <p>{{activity.note}}</p>
                </div>
            </div>
            <div v-else-if="selectedTab == tabTitles[1]">
                <h4>Comments</h4>
            </div>
            <div v-else></div>
        </div>

    </div>
</template>
<script>
import tabHead from '../../../components/tabHead.vue';
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "ActivityDetail",
    created(){
        this.pullActivity(this.$route.params.id).then(activity =>{
            this.activity = activity;
            this.isLoading = false;
        });
    }, 
    components : {
        tabHead
    },
    data: () => ({
        tabTitles : [ 'activity', 'comment'],
        selectedTab : 'activity',
        activity : null,
        isLoading : true
    }),
    methods:{
        ...mapActions('activity', [
            'pullActivity'
        ]),
        tabClicked(tab){
            this.selectedTab = tab;
        },
    }
}
</script>
<style lang="stylus">
</style>

