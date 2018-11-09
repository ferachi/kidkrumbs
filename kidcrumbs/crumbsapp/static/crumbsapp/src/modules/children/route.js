import ChildList from "./views/ChildList.vue";
import ChildDetail from "./views/ChildDetail.vue";
import Child from "./views/Child.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const childrenRoute = {
    path : 'children/',
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
            path : "",
            component : ChildList,
            name : 'children',
            meta : { page : "children", menuPage:true }, // if this is the first page of the sites menu navigation
            beforeEnter(to, from , next){
                // ensuring that this routes is only accessible by parents and students
                let profile = store.getters["profile/getProfile"];
                let roles = profile.roles;
                if(roles.indexOf(ROLES.STUDENT) > -1){
                    next({name:'child'});        
                }
                else if(roles.indexOf(ROLES.EXTERNAL) > -1 ){
                    next();        
                }
                else{
                    next({name:"app"});
                }
            },
        },
        {
            path : ":username",
            component : ChildDetail,
            name : 'childDetail'
        },

    ]
}

export {childrenRoute as default}
