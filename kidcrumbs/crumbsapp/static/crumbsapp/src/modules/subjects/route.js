import Subject from "./views/Subject.vue";
import SubjectDetail from "./views/SubjectDetail.vue";
import SubjectList from "./views/SubjectList.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const subjectRoute = {
    path : 'subjects',
    component : Subject,
    children : [
        {
            path : "",
            component : SubjectList,
            name : 'subjects'
        },
        {
            path : ":id",
            component : SubjectDetail,
            name : "subjectDetail"
        }
    ]
}


export {subjectRoute as default}
