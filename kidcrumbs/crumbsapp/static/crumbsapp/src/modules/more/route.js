import More from "./views/More.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const moreRoute = {
    path : '/my-menu/',
    component : More,
    name : 'moreMenu',
    meta : { page : "moreMenu", menuPage:true },
}

export {moreRoute as default}
