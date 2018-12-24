import Activity from "./views/Activity.vue";
import Activities from "./views/Activities.vue";
import ActivityDetail from "./views/ActivityDetail.vue";
import ActivityDateDetail from "./views/ActivityDateDetail.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const activitiesRoute = {
    path : '/activities',
    component : Activity,
    meta : { page : "activities", menuPage:false },
    children : [
        {
            path : "",
            component : Activities,
            name : 'activities',
            props : { groupId : "944e18be-0b51-4ab5-a584-a87811cf1886", schoolSlug : "blue-international-primary-secondary-school" }
        },
        {
            path : "date/:date",
            component : ActivityDateDetail,
            name : 'activityDetailByDate',
            props : { groupId : "944e18be-0b51-4ab5-a584-a87811cf1886"}
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
