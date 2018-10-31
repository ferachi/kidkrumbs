<template>
    <div>
        <h2 class="primary-color text-center">My Children</h2>
        <person-list :people='children' @person-click="personClicked($event)"></person-list>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
import ROLES from '../../../data_models/permissions';
import PersonList from '../../../components/PersonList.vue';
export default{
    name : "Children",
    created(){
    },
    computed : {
        ...mapGetters("profile", {
            profile : "getProfile"
        }),
        children(){
            // still confirming that this person has an external role
            if(this.profile.roles.indexOf(ROLES.EXTERNAL) > -1){
                // get all relatives that are children
                return _.filter(this.profile.relatives, relative => {
                    return relative.relationship_type == "child";
                });
            }
        }
    },
    components:{
        PersonList
    },
    methods:{
        personClicked(child){
            this.$router.push({name:'child', params:{username: child.username}});
        }
    }
}
</script>
<style lang="stylus">
</style>
