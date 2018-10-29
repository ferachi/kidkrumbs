import App from "../components/Application.vue";
import NotFound from "../components/NotFound.vue";
import studentRoute from "../modules/students/route";
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
            studentRoute, 
            {
                path : '*',
                component : NotFound,
                name  :'notFound'
            }
        ]
    }
]
export default routes;
