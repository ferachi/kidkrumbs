<template>
    <div id="SchoolList" class="">
        <div class="d-flex">
            <div class="col-lg-6">
                <h4 class="font-weight- p-2 mt-4 text-uppercase">Select a school</h4>
                <school-list :schools="schools" @school-click="schoolClicked($event)"></school-list>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import schoolList from '../../../components/school-list.vue';
import ROLES from "../../../data_models/permissions";
export default {
    name: "SchoolList",
    components:{
        schoolList
    },
    computed : {
        ...mapGetters('profile', {profile : 'getProfile'}),
        schools(){
            // administrative roles only
            let administrativeRoles = [ROLES.KIDKRUMBEE, ROLES.ADMINISTRATIVE ]

            // schools for which user has administrative roles
            let rolesFilter = _.filter( this.profile.schoolRoles, (sr) =>{
                                return _.some(administrativeRoles, (ar) =>  _.includes(sr.roles, ar));
                            });
            let schools = _.map(rolesFilter, (role) => {
                let school = _.find(this.profile.schools, (_school) => _school.slug == role.school);
                return school;
            });
            return schools;
        }
    },
    methods : {
        schoolClicked(school){
            this.$router.push({name:'classroomList', params : { id : school.id }}); 
        }
    }
};
</script>
<style lang="stylus">
</style>
