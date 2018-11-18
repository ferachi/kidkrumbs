import Routine from "./views/Routine.vue";
import RoutineList from "./views/RoutineList.vue";
import RoutineDetail from "./views/RoutineDetail.vue";
import StudentRoutine from "./views/StudentRoutine.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const routinesRoute = {
    path : '/routines',
    component : Routine,
    children : [
        {
            path : "list",
            component : RoutineList,
            name : 'routines',
        },
        {
            path : "student/:routineId",
            component : StudentRoutine,
            name : 'studentRoutine'
        },
        {
            path : ":id",
            component : RoutineDetail,
            name : 'routine',
        },

    ]
}

export {routinesRoute as default}
