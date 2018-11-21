<template>
    <div id="activity" class="p-2" v-if="!isLoading">
        <h4>Activity</h4>
        <page>
            <router-view></router-view>
        </page>
    </div>
</template>
<script>
import page from "../../../components/page.vue"
import {mapActions} from "vuex";
export default{
    name : "Activity",
    created(){
        let groupId = "944e18be-0b51-4ab5-a584-a87811cf1886";
        this.fetchGroup(groupId).then( group =>{
            this.fetchActivities(group.id).then( activities => {
                this.isLoading = false;
            });
        });
    },
    components:{
        page,
    },
    data(){
        return {
            isLoading : true
        }
    },
    methods:{
        ...mapActions('activity',{
            fetchActivities : 'pullActivities'
        }),

        ...mapActions('group',[
            'fetchGroup'
        ])
    }
}
</script>
<style lang="stylus">
</style>

