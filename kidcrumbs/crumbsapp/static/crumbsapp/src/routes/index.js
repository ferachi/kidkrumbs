import App from "../components/Application.vue";
import Test from "../components/Test.vue";
import NotFound from "../components/NotFound.vue";
import childrenRoute from "../modules/children/route";
import childRoute from "../modules/child/route";
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
            childRoute, 
            activitiesRoute, 
            childrenRoute, 
            {
                path:'test',
                component: Test,
                name:'test'
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
