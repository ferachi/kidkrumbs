import Result from "./views/Result.vue";
import ResultDetail from "./views/ResultDetail.vue";
import ResultInit from "./views/ResultInit.vue";
import SelectSchool from "./views/SelectSchool.vue";
import ResultList from "./views/ResultList.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const resultRoute = {
    path : 'results/',
    component : Result,
    meta : { page : "results", menuPage:true },
    beforeEnter(to, from , next){
        // who has permissions here?
        next();
    },
    children : [
        {
            path : '',
            component : ResultInit,
            name : 'results',
            beforeEnter(to, from , next){
                // if this user has more than a single administrative role 
                // in application redirect user to choose a school first 
                // before he can view result list

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
                // to view result else just show a list of results from his school
                if(userAdminRoles.length > 1) next({name  : 'selectSchoolResult'});
                else next({name : 'resultList'});

            }
        },
        {
            path : 'list/:schoolId',
            component : ResultList,
            name : 'resultList'
        },
        {
            path : 'schools',
            component : SelectSchool,
            name : 'selectSchoolResult'
        },
        {
            path : ":username",
            component : ResultDetail,
            name : 'resultDetail'
        }
    ]
}

export {resultRoute as default}
