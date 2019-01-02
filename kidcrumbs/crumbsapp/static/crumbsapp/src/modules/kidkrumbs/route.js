import KidKrumbs from "./views/KidKrumbs.vue";
import Krumbs from "./views/Krumbs.vue";
import Home from "./views/Home.vue";
import About from "./views/About.vue";
import Contact from "./views/Contact.vue";
// import Schools from "./views/Schools.vue";

import announcementRoute from "../announcement/route";
import childRoute from "../child/route";
import resultRoute from "../result/route";
import childrenRoute from "../children/route";
import classroomRoute from "../classroom/route";
import profileRoute from "../profile/route";
import moreRoute from "../more/route";
import homeworkProfile from "../homework/route";
import subjectRoute from "../subject/route";
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
        schoolRoute
        // {
        //     path : 'schools',
        //     component : Schools,
        //     name : 'kidkrumbsSchools',
        //     meta : { page : "kidkrumbsSchools", krumbMenu:true },
        // },
    ]
}

const krumbsRoute = {
    path : 'krumbs',
    component : Krumbs,
    name : 'krumbs',
    children : [
        playRoute, 
        childRoute, 
        classroomRoute, 
        resultRoute, 
        profileRoute, 
        subjectRoute, 
        homeworkProfile, 
        routineRoute, 
        moreRoute, 
        habitRoute, 
        activitiesRoute, 
        announcementRoute, 
        childrenRoute, 
    ]
}

export {kidkrumbsRoute,krumbsRoute}
