import Profile from "./views/Profile.vue";
import ProfileDetail from "./views/ProfileDetail.vue";
import ProfileEdit from "./views/ProfileEdit.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const childRoute = {
    path : 'profile/',
    component : Profile,
    meta : { page : "profile", menuPage:true },
    children : [
        {
            path : '',
            component : ProfileDetail,
            name : 'profile'
        },
        {
            path : 'edit',
            component : ProfileEdit,
            name : 'profileEdit'
        },
    ]
}

export {childRoute as default}
