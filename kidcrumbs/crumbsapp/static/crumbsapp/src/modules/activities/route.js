import Activity from "./views/Activity.vue";
import Activities from "./views/Activities.vue";
import ActivityDetail from "./views/ActivityDetail.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const activitiesRoute = {
    path : '/activities',
    component : Activity,
    children : [
        {
            path : "",
            component : Activities,
            name : 'activities',
        },
        {
            path : ":id",
            component : ActivityDetail,
            name : 'activityDetail',
            props : {editable : true}
        }

    ]
}

export {activitiesRoute as default}
