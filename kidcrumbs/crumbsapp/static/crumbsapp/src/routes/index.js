import App from "../components/Application.vue";
import Test from "../components/Test.vue";
import NotFound from "../components/NotFound.vue";
import NoPermissions from "../components/NoPermissions.vue";
import announcementRoute from "../modules/announcement/route";
import childRoute from "../modules/child/route";
import resultRoute from "../modules/result/route";
import childrenRoute from "../modules/children/route";
import profileRoute from "../modules/profile/route";
import homeworkProfile from "../modules/homework/route";
import subjectRoute from "../modules/subject/route";
import routineRoute from "../modules/routine/route";
import habitRoute from "../modules/habit/route";
import playRoute from "../modules/play/route";
import activitiesRoute from "../modules/activities/route";
import {store} from "../appbootstrap";

const routes = [
    {
        path : '/',
        component : App,
        name : 'app',
        beforeEnter(to, from , next){
            // before entering the application obtain the token
            store.dispatch("auth/obtainToken").then(res => {
                next();
            });
        },
        children : [
            playRoute, 
            childRoute, 
            resultRoute, 
            profileRoute, 
            subjectRoute, 
            homeworkProfile, 
            routineRoute, 
            habitRoute, 
            activitiesRoute, 
            announcementRoute, 
            childrenRoute, 
            {
                path:'test',
                component: Test,
                name:'test'
            },
            {
                path:'403',
                component: NoPermissions,
                name:'noPermissions'
            },
            {
                path : '*',
                component : NotFound,
                name  :'notFound'
            }
        ]
    }
]
export default routes;
