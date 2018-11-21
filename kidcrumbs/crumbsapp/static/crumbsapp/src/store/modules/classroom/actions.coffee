import http from "../../../http";
import {CLASSROOM, CLASSROOMS, GROUP_STUDENTS, GROUP_HABITS, GROUP_ROUTINES, GROUP_ACTIVITIES, GROUP_HOME_WORKS} from "../../../urls";


fetchClassroom = ({dispatch,commit, getters}, id) ->
    classroom = getters.getClassroomById(id)
    if classroom 
        commit('setClassroom', classroom)
        return classroom
    dispatch("pullClassroom", id).then (classroom) ->
        commit('setClassroom', classroom)
        commit('updateClassrooms', classroom)
        classroom


fetchClassrooms = ({dispatch, getters}, schoolId) ->
    classrooms = getters.getClassroomsBySchool(schoolId)
    if classrooms[0]?
        return classrooms
    dispatch("pullClassrooms", schoolId).then (classrooms) ->
        commit 'addClassrooms', classrooms
        classrooms


pullClassrooms = ({commit}, schoolId) ->
    http.get(CLASSROOMS).then (response)->
        response.data

pullClassroom = ({commit}, id) ->
    http.get(CLASSROOM(id)).then (response)->
        response.data



# This fetches a classrooms' routines
fetchClassroomRoutines = ({dispatch,commit,getters}, id) -> 
    dispatch('fetchClassroom', id).then (classroom) ->
        routines = getters.getClassroomRoutines

        if routines
            return routines

        http.get(GROUP_ROUTINES(id)).then (response)->
            routines = response.data
            commit "setClassroomRoutines", routines
            commit "routine/addRoutines", routines, {root : true}
            routines

fetchClassroomStudents = ({dispatch, getters, commit}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        students = getters.getClassroomStudents

        if students
            return students

        http.get(GROUP_STUDENTS(id)).then (response)->
            students = response.data
            commit "setClassroomStudents", students
            students
    
fetchClassroomHabits = ({dispatch, getters, commit}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        habits = getters.getClassroomHabits

        if habits
            return habits

        http.get(GROUP_HABITS(id)).then (response)->
            habits = response.data
            commit "setClassroomHabits", habits
            habits

fetchClassroomHomeworks = ({dispatch, getters, commit}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        homeWorks = getters.getClassroomHomeworks

        if homeWorks
            return homeWorks

        http.get(GROUP_HOME_WORKS(id)).then (response)->
            homeWorks = response.data
            commit "setClassroomHomeworks", homeWorks
            homeWorks

fetchClassroomActivities = ({dispatch, getters, commit}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        activities = getters.getClassroomActivities

        if activities
            return activities

        http.get(GROUP_ACTIVITIES(id)).then (response)->
            activities = response.data
            commit "setClassroomActivities", activities
            commit "activity/addActivities", activities, {root:true}
            activities


fetchClassroomWithProps = ({dispatch, commit, state}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        students = dispatch('fetchClassroomStudents', id)
        habits = dispatch('fetchClassroomHabits', id)
        routines = dispatch('fetchClassroomRoutines', id)
        activities = dispatch('fetchClassroomActivities', id)
        homeWorks = dispatch('fetchClassroomHomeworks', id)

        Promise.all([students, habits, routines, activities]).then (props) ->
            commit 'updateClassrooms', state.classroom
            state.classroom




export {pullClassroom, fetchClassroom, fetchClassrooms, pullClassrooms, fetchClassroomStudents, fetchClassroomHabits,fetchClassroomRoutines, fetchClassroomWithProps, fetchClassroomActivities, fetchClassroomHomeworks}
