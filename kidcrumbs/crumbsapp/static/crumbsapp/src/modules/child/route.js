import Child from "./views/Child.vue";
import ChildActivity from "./views/ChildActivity.vue";
import ChildActivities from "./views/ChildActivities.vue";
import ChildActivityList from "./views/ChildActivityList.vue";
import ChildBehaviours from "./views/ChildBehaviours.vue";
import ChildBehaviourList from "./views/ChildBehaviourList.vue";
import ChildInit from "./views/ChildInit.vue";
import ChildProfile from "./views/ChildProfile.vue";
import ChildResult from "./views/ChildResult.vue";
import More from "./views/More.vue";
import ChildBehaviour from "./views/ChildBehaviour.vue";
import ChildHomework from "./views/ChildHomework.vue";
import ActivityDetail from "../activities/views/ActivityDetail.vue";
import ChildSubjects from "./views/ChildSubjects.vue";
import ChildClassrooms from "./views/ChildClassrooms.vue";
import ChildHabits from "../habit/views/StudentAttitude.vue";
import HabitNotFound from "../habit/views/HabitNotFound.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";

let date = new Date(),
    today = `${date.getUTCFullYear()}-${date.getUTCMonth() + 1} - ${date.getUTCDate()}`
const childRoute = {
    path : '/child/:username',
    component : Child,
    meta : { page : "children", menuPage:true }, // if this is the first page of the sites menu navigation
    beforeEnter(to, from , next){
        //TODO:
        //  Should only allow parents of the browsed child, the child himself or teachers/admin in the childs 
        //  'present' school to view the child.
        
        // get the users profile
        let profile = store.getters["profile/getProfile"];

        // check if this profile belongs to the child
        if(profile.username == to.params.username){
            next();
            return ;
        }

        // check if it is a parent of the child
        // find the child within users relatives
        let child = _.find(profile.relatives, relative => {
            return relative.username == to.params.username;
        });
        if(child && child.relationship_type == 'child'){
            next();
            return;
        }
        if(_.includes(profile.roles, 'kidkrumbee')){
            next();
            return ;
        }

        // if this user is an administrative user
        if( _.includes(profile.roles,'administrative')){
            // HACK:
            // this will delay fetching of child view for teachers.
            // there must be some better way to do this
            store.dispatch('child/fetchChild', to.params.username).then( child => {
                // HACK
                // this assumes that a childs current group should be found in the 
                // childs current school. There is no current way to find a childs
                // current school
                store.dispatch('child/fetchChildCurrentGroups').then(groups => {
                    // HACK
                    // Another assumption. the groups list contains homogenous groups.
                    // homogenuity based on the school. i.e all the groups have the same school
                    if(groups.length > 0){
                        // if the user has a school role in the childs current school
                        let school  = groups[0].school,
                            role = _.find(profile.schoolRoles, _role => _role.school == school);

                        // if this role is administrative
                        if(!!role && _.includes(role.roles,'administrative')){
                            next();
                        }
                        else{
                            next({name:'noPermissions'});
                        }
                    }
                    else{
                        next({name:"noPermissions"});
                    }
                });
            })
            .catch(err => {
                next({name:"noPermissions"});
            });
        }
        else{
            next({name:"noPermissions"});
        }
    },
    children : [
        {
            path : '',
            component : ChildInit,
            name : 'child'
        },
        {
            path : "activities",
            component : ChildActivities,
            children:[
                {
                    path : "",
                    component : ChildActivityList,
                    name : 'childActivities',

                },
                {
                    path : ":date",
                    component : ChildActivity,
                    name : 'activityDetailByDate',
                }

            ]
        },
        {
            path : "behaviours",
            component : ChildBehaviours,
            children:[
                {
                    path : "",
                    component : ChildBehaviourList,
                    name : 'childBehaviours',

                },
                {
                    path : ":date",
                    component : ChildBehaviour,
                    name : 'childBehaviour',
                }
            ]
        },
        {
            path : "homeworks",
            component : ChildHomework,
            name : 'childHomework',
        },
        {
            path : "menu",
            component : More,
            name : 'more',
        },
        {
            path : "subjects",
            component : ChildSubjects,
            name : "childSubjects"
        },
        {
            path : "classrooms",
            component : ChildClassrooms,
            name : "childClassrooms"
        },
        {
            path : "profile",
            component : ChildProfile,
            name : "childProfile"
        },
        {
            path : "result",
            component : ChildResult,
            name : "childResult"
        }

    ]
}

export {childRoute as default}
