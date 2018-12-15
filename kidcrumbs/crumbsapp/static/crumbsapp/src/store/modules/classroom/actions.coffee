import http from "../../../http"
import {CLASSROOM, SCHOOL_CLASSROOMS, GROUP_STUDENTS, GROUP_HABITS, GROUP_ROUTINES, GROUP_ACTIVITIES, CLASSROOM_HOMEWORKS} from "../../../urls";


fetchClassroom = ({dispatch,commit, getters}, id) ->
    classroom = getters.getClassroomById(id)
    if classroom
        commit('setClassroom', classroom)
        return classroom
    dispatch("pullClassroom", id).then (classroom) ->
        commit('setClassroom', classroom)
        commit('updateClassrooms', classroom)
        classroom


fetchClassrooms = ({commit,dispatch, getters}, schoolId) ->
    classrooms = getters.getClassroomsBySchool(schoolId)
    if classrooms[0]?
        return classrooms
    dispatch("pullClassrooms", schoolId).then (classrooms) ->
        commit 'addClassrooms', classrooms
        classrooms


pullClassrooms = ({commit}, schoolId) ->
    http.get(SCHOOL_CLASSROOMS(schoolId)).then (response)->
        response.data


pullClassroom = ({commit}, id) ->
    http.get(CLASSROOM(id)).then (response)->
        response.data


fetchClassroomHomeworks = ({dispatch, getters, commit}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        homeWorks = getters.getClassroomHomeworks

        if homeWorks
            return homeWorks

        http.get(CLASSROOM_HOMEWORKS(id)).then (response)->
            homeWorks = response.data
            commit "setClassroomHomeworks", homeWorks
            homeWorks


fetchClassroomActivities = ({dispatch, getters, commit}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        activities = getters.getClassroomActivities

        if activities
            return activities

        dispatch('activity/pullActivities', id, {root : true}).then (activities) ->
            commit "setClassroomActivities", activities
            activities


fetchClassroomWithProps = ({commit, dispatch, getters, state}, id) ->

    dispatch('fetchClassroom', id).then (classroom) ->
        activities = dispatch('fetchClassroomActivities', id)
        homeworks = dispatch('fetchClassroomHomeworks',id)

        Promise.all([activities]).then (props) ->
            commit 'updateClassrooms', classroom
            classroom




export {pullClassroom, fetchClassroom, fetchClassrooms,fetchClassroomActivities, fetchClassroomWithProps, pullClassrooms, fetchClassroomHomeworks}
