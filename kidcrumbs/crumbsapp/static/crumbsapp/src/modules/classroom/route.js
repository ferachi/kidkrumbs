import Classroom from "./views/Classroom.vue";
import ClassroomGuard from "./views/ClassroomGuard.vue";
import ClassroomDetail from "./views/ClassroomDetail.vue";
import ClassroomList from "./views/ClassroomList.vue";
import School from "./views/School.vue";
import SchoolList from "./views/SchoolList.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";

const classroomRoute = {
    path : 'classrooms/',
    component : Classroom,
    beforeEnter(to, from , next){
        // who has permissions here?
        // Only Administrative users should be allowed to view anything here

        let administrativeRoles = [ROLES.KIDKRUMBEE, ROLES.ADMINISTRATIVE ]
        
        // get the users profile
        let profile = store.getters["profile/getProfile"];

        // check if user has any role
        if(profile.roles.length == 0) next({name : 'noPermissions'});

        // check if user has an administrative role
        if(profile.roles.findIndex((role) => _.some( administrativeRoles, (ar) => ar == role)) == -1){
            next({name:'noPermissions'});        
            return ;
        }
        next();
    },
    children : [
        {
            path : '',
            component : ClassroomGuard,
            name : 'classrooms',
            beforeEnter(to, from , next){
                // if this user has more than a single administrative role 
                // in application redirect user to choose a school first 
                // before he can view result list

                // note administrative covers teachers, super and other administratives
                let administrativeRoles = [ROLES.KIDKRUMBEE, ROLES.ADMINISTRATIVE ]

                // get the users profile
                let profile = store.getters["profile/getProfile"];

                // determine how many administrative roles a user has
                let userAdminRoles = _.filter( profile.schoolRoles, (sr) =>{
                                        return _.find(sr.roles, (role) => {
                                            return _.some(administrativeRoles, (ar) => role ==  ar);
                                        })
                                    })

                // if user has more than a single administrative role redirect to selecting a school for which they want
                // to view result else just show a list of results from his school
                if(userAdminRoles.length > 1) next({name  : 'selectSchoolClass'});
                else {
                    // get the users school where they have an administrative role
                    let schoolRole = profile.schoolRoles.find((role) => _.some( administrativeRoles, (ar) => _.includes(role.roles, ar))) 
                     
                    // if the user has a school role
                    if(!!schoolRole){
                        let school = _.find(profile.schools, {slug:schoolRole.school});
                        if(!!school){
                            next({name : 'classroomList', params : {id:school.id}});
                            return;
                        }
                    }
                    next({name : 'notFound'});
                }
            }
        },
        {
            path : 'schools',
            component : School,
            children : [

                {
                    path : '',
                    component : SchoolList,
                    name : 'selectSchoolClass'
                },
                {
                    path : ':id',
                    component : ClassroomList,
                    name : 'classroomList'
                }
            ]

        },
        {
            path : ":id",
            component : ClassroomDetail,
            name : 'classroomDetail'
        }
    ]
}

export {classroomRoute as default}
