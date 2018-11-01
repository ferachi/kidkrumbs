import ActivityList from "./views/ActivityList.vue";
import ActivityDetail from "./views/ActivityDetail.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const activitiesRoute = {
    path : '/activities',
    component : Activity,
    },
    children : [
        {
            path : "",
            component : ActivityList,
            name : 'activities',
        },
        {
            path : ":id",
            component : ActivityDetail
            name : 'activitiesDetail',
        }

    ]
}

export {activitiesRoute as default}
