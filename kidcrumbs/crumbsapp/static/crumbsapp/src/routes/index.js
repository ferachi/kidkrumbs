import App from "../components/Application.vue";
import Test from "../components/Test.vue";
import {kidkrumbsRoute, krumbsRoute} from '../modules/kidkrumbs/route';
import NotFound from "../components/NotFound.vue";
import NoPermissions from "../components/NoPermissions.vue";
import {store} from "../appbootstrap";

const routes = [
    {
        path : '/',
        component : App,
        beforeEnter(to, from , next){
            // before entering the application obtain the token
            store.dispatch("auth/obtainToken").then(res => {
                next();
            })
            .catch(err => {
                next();   
            });
        },
        children : [
            kidkrumbsRoute,
            krumbsRoute
        ]
    },
    {
        path:'test',
        component: Test,
        name:'test'
    },
    {
        path:'404',
        component: NoPermissions,
        name:'noPermissions'
    },
    {
        path:'/403',
        component: NoPermissions,
        name:'notAllowed'
    },
    {
        path : '*',
        component : NotFound,
        name  :'notFound'
    }
]
export default routes;
