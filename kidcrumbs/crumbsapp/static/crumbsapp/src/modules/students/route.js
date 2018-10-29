import StudentList from "./views/StudentList.vue";
import StudentDetail from "./views/StudentDetail.vue";
import Student from "./views/Student.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const studentRoute = {
    path : 'children/',
    component : Student,
    meta : { page : "children", menuPage:true }, // if this is the first page of the sites menu navigation
    beforeEnter(to, from , next){
        // ensuring that this routes is only accessible by parents and students
        let profile = store.getters["profile/getProfile"];
        let roles = profile.roles;
        if(roles.indexOf(ROLES.EXTERNAL) > -1 || roles.indexOf(ROLES.STUDENT) > -1 ){
            next();        
        }
        else{
            next({name:"app"});
        }
    },
    children : [
        {
            path : "",
            component : StudentList,
            name : 'children',
            beforeEnter(to, from , next){
                // ensuring that this routes is only accessible by parents and students
                let profile = store.getters["profile/getProfile"];
                let roles = profile.roles;
                if(roles.indexOf(ROLES.STUDENT) > -1){
                    next({name:'child'});        
                }
                else if(roles.indexOf(ROLES.EXTERNAL) > -1 ){
                    next();        
                }
                else{
                    next({name:"app"});
                }
            },
        },
        {
            path : ":username",
            component : StudentDetail,
            name : 'child'
        },

    ]
}

export {studentRoute as default}
