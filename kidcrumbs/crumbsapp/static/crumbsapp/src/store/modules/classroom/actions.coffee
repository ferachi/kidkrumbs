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

fetchClassroomHomeworks = ({dispatch, getters, commit}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        homeWorks = getters.getClassroomHomeworks

        if homeWorks
            return homeWorks

        http.get(GROUP_HOME_WORKS(id)).then (response)->
            homeWorks = response.data
            commit "setClassroomHomeworks", homeWorks
            homeWorks




export {pullClassroom, fetchClassroom, fetchClassrooms, pullClassrooms, fetchClassroomHomeworks}
