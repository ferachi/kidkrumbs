import Activity from "./views/Activity.vue";
import Activities from "./views/Activities.vue";
import ActivityDetail from "./views/ActivityDetail.vue";
import ActivityDateDetail from "./views/ActivityDateDetail.vue";
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
            path : "date/:date",
            component : ActivityDateDetail,
            name : 'activityDetailByDate',
        },
        {
            path : ":id",
            component : ActivityDetail,
            name : 'activityDetail',
            props : (route) => ( {id:route.params.id, editable : true} )
        }

    ]
}

export {activitiesRoute as default}
