import Announcement from './views/Announcement.vue';
import AnnouncementList from './views/AnnouncementList.vue';
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const announcementRoute = {
    path : 'announcements/',
    component : Announcement,
    beforeEnter(to, from , next){
        // ensure that the user is logged in.
        // should be don in the parent route
        next();
    },
    children :[
        {
            path : '',
            component : AnnouncementList,
            name : 'news',
            meta : { page : "news", menuPage:true }, // if this is the first page of the sites menu navigation
        }
    ]
}

export {announcementRoute as default}
