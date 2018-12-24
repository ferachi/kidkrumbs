import Homework from "./views/Homework.vue";
import HomeworkList from "./views/HomeworkList.vue";
import HomeworkEdit from "./views/HomeworkEdit.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const subjectRoute = {
    path : 'assignments',
    component : Homework,
    children : [
        {
            path : "",
            component : HomeworkList,
            name : 'homeworks',
            props : { classroomId : '944e18be-0b51-4ab5-a584-a87811cf1886', editable : false }
        },
        {
            path : "assignment",
            component : HomeworkEdit,
            name : 'homeworkEdit'
        },
    ]
}


export {subjectRoute as default}
