import Child from "./views/Child.vue";
import ChildActivity from "./views/ChildActivity.vue";
import ChildInit from "./views/ChildInit.vue";
import ChildBehaviour from "./views/ChildBehaviour.vue";
import ChildHomework from "./views/ChildHomework.vue";
import ActivityDetail from "../activities/views/ActivityDetail.vue";
import ChildHabits from "../habit/views/StudentAttitude.vue";
import HabitNotFound from "../habit/views/HabitNotFound.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


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
            component : ChildActivity,
            name : 'childActivity',
            children:[
                {
                    path : ":id",
                    component : ActivityDetail,
                    name : 'childActivityDetail',
                }
            ]
        },
        {
            path : "behaviours",
            component : ChildBehaviour,
            name : 'childBehaviour',
            children : [
                {
                    path : "no-habits",
                    component : HabitNotFound,
                    name : 'noChildHabits',
                    props:{editable : false}
                },
                {
                    path : ":id",
                    component : ChildHabits,
                    name : 'childHabits',
                    props : {editable : false}
                },
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
