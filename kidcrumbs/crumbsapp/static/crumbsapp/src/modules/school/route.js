import SchoolView from "./views/SchoolView.vue";
import School from "./views/School.vue";
import Schools from "./views/Schools.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const schoolRoute = {
    path : 'schools',
    component : SchoolView,
    meta : { page : "kidkrumbsSchools", krumbMenu:true },
    children:[
        {
            path : '',
            component : Schools,
            name : 'kidkrumbsSchools',
        },
        {
            path : ':id',
            component : School,
            name : 'kidkrumbsSchoolDetail'
        }

    ]
}

export {schoolRoute as default}
