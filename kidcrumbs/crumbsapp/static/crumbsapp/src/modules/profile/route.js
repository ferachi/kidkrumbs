import Profile from "./views/Profile.vue";
import ProfileDetail from "./views/ProfileDetail.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const childRoute = {
    path : '/profile/:username',
    component : Profile,
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
            component : ProfileDetail,
            name : 'profile'
        },
    ]
}

export {childRoute as default}
