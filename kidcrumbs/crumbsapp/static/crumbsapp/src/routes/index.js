import App from "../components/Application.vue";
import Students from "../components/Students.vue";
import Student from "../components/Student.vue";
import NotFound from "../components/NotFound.vue";

const studentRoutes = {
    path : 'children/',
    component : Students,
    name : 'children',
    meta : { page : "children", menuPage:true }, // if this is the first page of the sites menu navigation
    children : [
        {
            path : "child/",
            component : Student,
            name : 'child'
        }
    ]
}
const routes = [
    {
        path : '/',
        component : App,
        name : 'app',
        children : [
            studentRoutes, 
            {
                path : '*',
                component : NotFound,
                name  :'notFound'
            }
        ]
    }
]
export default routes;
