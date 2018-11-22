import Child from "./views/Child.vue";
import ChildActivity from "./views/ChildActivity.vue";
import ChildActivities from "./views/ChildActivities.vue";
import ChildActivityList from "./views/ChildActivityList.vue";
import ChildBehaviours from "./views/ChildBehaviours.vue";
import ChildBehaviourList from "./views/ChildBehaviourList.vue";
import ChildInit from "./views/ChildInit.vue";
import ChildBehaviour from "./views/ChildBehaviour.vue";
import ChildHomework from "./views/ChildHomework.vue";
import ActivityDetail from "../activities/views/ActivityDetail.vue";
import ChildHabits from "../habit/views/StudentAttitude.vue";
import HabitNotFound from "../habit/views/HabitNotFound.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";

let date = new Date(),
    today = `${date.getUTCFullYear()}-${date.getUTCMonth() + 1} - ${date.getUTCDate()}`
const childRoute = {
    path : '/child/:username',
    component : Child,
    beforeEnter(to, from , next){
        // ensuring that this routes is only accessible by parents and students
        let profile = store.getters["profile/getProfile"];
        let roles = profile.roles;
        if(roles.indexOf(ROLES.EXTERNAL) > -1 || roles.indexOf(ROLES.STUDENT) > -1 ){
            next();        
        }
        else{
            next({name:"app"});
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

    ]
}

export {childRoute as default}
