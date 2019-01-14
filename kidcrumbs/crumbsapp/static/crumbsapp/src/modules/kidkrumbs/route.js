import KidKrumbs from "./views/KidKrumbs.vue";
import Krumbs from "./views/Krumbs.vue";
import Home from "./views/Home.vue";
import About from "./views/About.vue";
import Contact from "./views/Contact.vue";
import Login from "./views/Login.vue";
// import Schools from "./views/Schools.vue";

import announcementRoute from "../announcement/route";
import childRoute from "../child/route";
import resultRoute from "../result/route";
import assessmentRoute from "../assessment/route";
import childrenRoute from "../children/route";
import classroomRoute from "../classroom/route";
import profileRoute from "../profile/route";
import moreRoute from "../more/route";
import homeworkProfile from "../homework/route";
import subjectRoute from "../subject/route";
import studentRoute from "../student/route";
import routineRoute from "../routine/route";
import habitRoute from "../habit/route";
import playRoute from "../play/route";
import activitiesRoute from "../activities/route";
import schoolRoute from "../school/route";

import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const kidkrumbsRoute  = {
    path : '',
    component : KidKrumbs,
    beforeEnter(to, from , next){
        store.dispatch("auth/obtainToken").then(res => {
            next();
        })
        .catch(err => {
            next({name : 'app'});   
        });
    },
    children : [
        {
            path : '',
            component : Home,
            name : 'app',
            meta : { page : "app", krumbMenu:true },
        },
        {
            path : 'about',
            component : About,
            name : 'aboutKidkrumbs',
            meta : { page : "aboutKidkrumbs", krumbMenu:true },
        },
        {
            path : 'contact',
            component : Contact,
            name : 'contactKidkrumbs',
            meta : { page : "contactKidkrumbs", krumbMenu:true },
        },
        {
            path : 'login',
            component : Login,
            name : 'login',
            meta : { page : "login", krumbMenu:true },
        },
        schoolRoute
    ]
}

const krumbsRoute = {
    path : 'krumbs',
    component : Krumbs,
    name : 'krumbs',
    beforeEnter(to, from , next){
        store.dispatch("auth/obtainToken").then(res => {
            if(res)
                next();
            else
                next({name : 'app'});
        })
        .catch(err => {
            next({name : 'app'});   
        });
    },
    children : [
        playRoute, 
        childRoute, 
        classroomRoute, 
        assessmentRoute, 
        resultRoute, 
        profileRoute, 
        subjectRoute, 
        homeworkProfile, 
        routineRoute, 
        moreRoute, 
        studentRoute, 
        habitRoute, 
        activitiesRoute, 
        announcementRoute, 
        childrenRoute, 
    ]
}

export {kidkrumbsRoute,krumbsRoute}
