import Student from "./views/Student.vue";
import StudentInit from "./views/StudentInit.vue";
import SelectSchool from "./views/SelectSchool.vue";
import StudentList from "./views/StudentList.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const studentRoute = {
    path : 'students/',
    component : Student,
    meta : { page : "students", menuPage:true },
    beforeEnter(to, from , next){
        // who has permissions here?
        next();
    },
    children : [
        {
            path : '',
            component : StudentInit,
            name : 'students',
            beforeEnter(to, from , next){
                // if this user has more than a single administrative role 
                // in application redirect user to choose a school first 
                // before he can view student list

                // not administrative covers teachers, super and other administratives
                let administrativeRoles = [ROLES.KIDKRUMBEE, ROLES.ADMINISTRATIVE ]

                let profile = store.getters["profile/getProfile"];

                if(profile.roles.length == 0) next({name : 'noPermissions'});

                // if this user has no administrative role
                if(profile.roles.findIndex((role) => _.some( administrativeRoles, (ar) => ar == role)) == -1){
                    next({name:'noPermissions'});        
                    return ;
                }

                // determine how many administrative roles a user has
                let userAdminRoles = _.filter( profile.schoolRoles, (sr) =>{
                                            return _.find(sr.roles, (role) => {
                                                return _.some(administrativeRoles, (ar) => role ==  ar);
                                            })
                                        })

                // if user has more than a single administrative role redirect to selecting a school for which they want
                // to view student else just show a list of students from his school
                if(userAdminRoles.length > 1) next({name  : 'selectSchoolStudent'});
                else next({name : 'studentList'});

            }
        },
        {
            path : 'list/:schoolId',
            component : StudentList,
            name : 'studentList'
        },
        {
            path : 'schools',
            component : SelectSchool,
            name : 'selectSchoolStudent'
        },
    ]
}

export {studentRoute as default}
