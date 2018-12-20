import Classroom from "./views/Classroom.vue";
import ClassroomGuard from "./views/ClassroomGuard.vue";
import ClassroomProfile from "./views/ClassroomProfile.vue";
import ClassroomHomework from "./views/ClassroomHomework.vue";
import ClassroomMember from "./views/ClassroomMember.vue";
import ClassroomResult from "./views/ClassroomResult.vue";
import ClassroomSubject from "./views/ClassroomSubject.vue";
import ClassroomBehaviour from "./views/ClassroomBehaviour.vue";
import ClassroomActivity from "./views/ClassroomActivity.vue";
import ClassroomDetail from "./views/ClassroomDetail.vue";
import ClassroomList from "./views/ClassroomList.vue";
import School from "./views/School.vue";
import SchoolList from "./views/SchoolList.vue";
import HabitToday from "./components/habitToday.vue";
import HabitByDate from "./components/habitByDate.vue";
import HabitNotFound from "./components/habitNotFound.vue";
import StudentAttitude from "./components/studentAttitude.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";

const classroomRoute = {
    path : 'classrooms/',
    component : Classroom,
    meta : { page : "classrooms", menuPage:true },
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
            children : [
                {
                    path : '',
                    component : ClassroomProfile,
                    name : 'classroomDetail',
                    meta : {subMenu : true, subMenuName : 'classroomDetail'}
                },
                {
                    path : 'activity',
                    component : ClassroomActivity,
                    name : 'classroomActivity',
                    meta : {subMenu : true, subMenuName : 'classroomActivity'}
                },
                {
                    path : 'behaviour',
                    component : ClassroomBehaviour,
                    meta : {subMenu : true, subMenuName : 'classroomBehaviour'},
                    children :[
                        {
                            path : "",
                            component : HabitToday,
                            name : 'classroomBehaviour',
                        },
                        {
                            path:'attitude/:routineId',
                            component : StudentAttitude,
                            name : 'studentBehaviour',
                            props : (route) => ( {id:route.params.routineId, editable : true} )
                        },
                        {
                            path : ":date",
                            component : HabitByDate,
                            name : 'habitByDate',
                            props : {editable : true}
                        },

                    ]
                },
                {
                    path : 'homework',
                    component : ClassroomHomework,
                    name : 'classroomHomework',
                    meta : {subMenu : true, subMenuName : 'classroomHomework'}
                },
                {
                    path : 'members',
                    component : ClassroomMember,
                    name : 'classroomMember',
                    meta : {subMenu : false, subMenuName : 'classroomMember'}
                },
                {
                    path : 'subjects',
                    component : ClassroomSubject,
                    name : 'classroomSubject',
                    meta : {subMenu : false, subMenuName : 'classroomSubject'}
                },
                {
                    path : 'results',
                    component : ClassroomResult,
                    name : 'classroomResult',
                    meta : {subMenu : false, subMenuName : 'classroomResult'}
                },
            ],
        }
    ]
}

export {classroomRoute as default}
