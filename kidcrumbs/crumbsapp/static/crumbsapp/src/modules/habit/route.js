import Habit from "./views/Habit.vue";
import HabitList from "./views/HabitList.vue";
import HabitByDate from "./views/HabitSelect.vue";
import HabitForToday from "./views/HabitToday.vue";
import HabitWithDate from "./views/HabitWithDate.vue";
import HabitNotFound from "./views/HabitNotFound.vue";
import StudentRoutineList from "./views/StudentRoutineList.vue";
import StudentAttitude from "./views/StudentAttitude.vue";
import {store} from "../../appbootstrap";
import ROLES from "../../data_models/permissions";


const habitRoute = {
    path : '/habits',
    component : Habit,
    children : [
        {
            path : "",
            component : HabitList,
            name : 'habits',
        },
        {
            path : "date",
            component : HabitByDate,
            children :[
                {
                    path : "",
                    component : HabitForToday,
                    name : 'habitForToday',
                },
                {
                    path : ":date",
                    component : HabitWithDate,
                    name : 'habitWithDate',
                    props : {editable : true}
                },
                {
                    path:'attitude/:id',
                    component : StudentAttitude,
                    name : 'studentsAttitude',
                    props : (route) => ( {id:route.params.id, editable : true} )
                },

            ]
        },
        {
            path : ":id",
            component : StudentRoutineList,
            name : 'habit',
            props:true
        },
        {
            path:'attitude/:id',
            component : StudentAttitude,
            name : 'studentAttitude',
            props : {editable : true}
        },
    ]
}
export {habitRoute as default}
