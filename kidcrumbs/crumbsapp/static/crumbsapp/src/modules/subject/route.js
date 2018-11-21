import Subject from "./views/Subject.vue";
import SubjectDetail from "./views/SubjectDetail.vue";
import Overview from "./views/SubjectOverview.vue";
import Result from "./views/SubjectResult.vue";
import Teacher from "./views/SubjectTeacher.vue";
import Syllabus from "./views/SubjectSyllabus.vue";
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
            children:[
                {
                    path:'',
                    component:Overview,
                    name:'subjectDetail'
                },
                {
                    path:'syllabus',
                    component : Syllabus,
                    name : 'subjectSyllabus'
                },
                {
                    path:'results',
                    component : Result,
                    name : 'subjectResult'
                },
                {
                    path:'teachers',
                    component : Teacher,
                    name : 'subjectTeacher'
                }
            ]
        }
    ]
}


export {subjectRoute as default}
