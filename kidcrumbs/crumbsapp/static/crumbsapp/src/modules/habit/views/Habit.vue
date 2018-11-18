<template>
    <div id="habit">
        <div v-if="isLoading">
        </div>
        <div v-else>
            <page>
            <router-view>
            </router-view>        
            </page>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import page from '../../../components/page.vue';
export default {
    name : 'habit',
    created(){
        // TODO: this is a test only
        // this should be this.getGroupStudents & getGroupHabits
        // as this method should only be called in a
        // groups' module by which before it is called
        // the groups and its props should be in the store
        this.fetchGroupWithProps(this.groupId).then( group => {
            this.isLoading = false;
        })
    },
    data(){
        return {
            groupId : "944e18be-0b51-4ab5-a584-a87811cf1886", // test group
            isLoading: true
        }

    },
    methods:{
        ...mapActions('group',[
            'fetchGroupWithProps'
        ]),
    },
    components:{
        page
    }
}
</script>
<style lang="stylus">
</style>
