import Child from "./views/Child.vue";
import ActivityDetail from "../activities/views/ActivityDetail.vue";
import BehaviourDetail from "../behaviours/views/BehaviourDetail.vue";
import HomeworkDetail from "../homework/views/HomeworkDetail.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const childRoute = {
    path : '/child/:username',
    component : Child,
    name : "child",
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
            path : "activities/:id",
            component : ActivityDetail,
            name : 'childActivity',
        },
        {
            path : "behaviours/:id",
            component : BehaviourDetail,
            name : 'childBehaviour',
        },
        {
            path : "homework/:id",
            component : HomeworkDetail,
            name : 'childHomework',
        },

    ]
}

export {childRoute as default}
