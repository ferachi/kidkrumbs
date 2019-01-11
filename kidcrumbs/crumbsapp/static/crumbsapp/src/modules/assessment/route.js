import Assessment from "./views/Assessment.vue";
import AssessmentDetail from "./views/AssessmentDetail.vue";
import AssessmentRedirect from "./views/AssessmentRedirect.vue";
import AssessmentView from "./views/AssessmentView.vue";
import SelectSchool from "./views/SelectSchool.vue";
import SelectAssessment from "./views/SelectPage.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const studentRoute = {
    path : 'assessments/',
    component : Assessment,
    meta : { page : "assessments", menuPage:true },
    beforeEnter(to, from , next){
        // who has permissions here?
        next();
    },
    children : [
        {
            path : '',
            component : AssessmentRedirect,
            name : 'assessments',
            beforeEnter(to, from , next){
                // if this user has more than a single administrative role 
                // in application redirect user to choose a school first 
                // before he can view student list

                // not administrative covers teachers, super and other administratives
                let administrativeRoles = [ROLES.KIDKRUMBEE, ROLES.ADMINISTRATIVE ]

                let profile = store.getters["profile/getProfile"];

                if(profile.roles.length == 0) next({name : 'app'});

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
                if(userAdminRoles.length > 1) next({name  : 'selectAssessmentSchool'});
                else next({name : 'selectAssessmentView'});

            }
        },
        {
            path : 'schools',
            component : SelectSchool,
            name : 'selectAssessmentSchool'
        },
        {
            path : ':schoolId',
            component : AssessmentView,
            children : [
                {
                    path : '',
                    component : SelectAssessment,
                    name : 'selectAssessmentView'
                },
                {
                    path : 'table',
                    component : AssessmentDetail,
                    name : 'assessmentDetail'
                },
            ]
        },
    ]
}

export {studentRoute as default}
