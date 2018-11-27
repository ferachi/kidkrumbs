import Main from "./views/Main.vue";
import Home from "./views/Home.vue";
import DThree from "./views/DThree.vue";

const playRoute = {
    path : 'play',
    component : Main,
    children : [
        {
            path : "",
            component : Home,
            name : 'playHome'
        },
        {
            path : "d3",
            component :DThree ,
            name : "d3"
        }
    ]
}


export {playRoute as default}
