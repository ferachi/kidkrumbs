<template>
    <div id="selectSchool" class="d-flex">
        <div class="col-lg-8 col-xl-6">
            <h4 class="font-weight- p-2 mt-4 text-uppercase">Select a school</h4>
            <div class="d-flex align-items-center flex-wrap">
                <div class="col-sm-6 col-12 p-2" v-for="school in schools" :key="school.id">
                    <div class="p-4 clickable" :style="{background:school.color}" @click="viewSchoolResults(school)">
                        <div class="d-flex align-items-center">
                            <div class="col-auto px-1">
                                <md-avatar class="md-small">
                                    <img :src="school.logo" :alt="school.name">
                                </md-avatar>
                            </div>
                            <div class="col px-3 py-4">
                                <h6 class="font-weight- color_white ">
                                    {{school.name}} 
                                </h6>
                            </div>
                        </div>
                        <p class="color_white"> {{school.motto}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapMutations} from 'vuex';
import ROLES from "../../../data_models/permissions";
export default {
    name : "SelectSchool",
    computed : {
        ...mapGetters('profile',{
            profile : 'getProfile'
        }),
        schools(){
            // administrative roles only
            let administrativeRoles = [ROLES.KIDKRUMBEE, ROLES.ADMINISTRATIVE ]

            // schools for which user has administrative roles
            let rolesFilter = _.filter( this.profile.schoolRoles, (sr) =>{
                                     return _.find(sr.roles, (role) => {
                                         return _.some(administrativeRoles, (ar) => role ==  ar);
                                     });
                                 });
            let schools = _.map(rolesFilter, (role) => {
                let school = _.find(this.profile.schools, (_school) => _school.slug == role.school);
                return school;
            });
            return schools;
        }
    },
    methods : {
        ...mapMutations('school',['setSchool']),
        viewSchoolResults(school){
            this.setSchool(school);
            this.$router.push({name : 'resultList', params:{schoolId:school.id}});
        }
    }
}
</script>
<style lang="stylus">
#selectSchool
    .school 
        width 250px
        height 150px
</style>
