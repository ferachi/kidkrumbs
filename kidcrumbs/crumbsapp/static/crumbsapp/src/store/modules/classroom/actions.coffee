import http from "../../../http"
import {CLASSROOM, SCHOOL_CLASSROOMS, CLASSROOM_SUBJECTS, GROUP_STUDENTS, GROUP_HABITS, GROUP_ROUTINES, GROUP_ACTIVITIES, CLASSROOM_HOMEWORKS} from "../../../urls";


fetchClassroom = ({dispatch,commit, getters}, id) ->
    classroom = getters.getClassroomById(id)
    if classroom
        commit('setClassroom', classroom)
        commit('group/setGroup', classroom, {root : true})
        return classroom
    dispatch("pullClassroom", id).then (classroom) ->
        commit('setClassroom', classroom)
        commit('group/setGroup', classroom, {root : true})
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
            homeWorks = _.map response.data, (homework) ->
                homework.isExpired = moment(homework.submission_date, "YYYY-MM-DD").isBefore(moment().format("YYYY-MM-DD"));
                homework._name = homework.subject.name
                homework
            commit "setClassroomHomeworks", homeWorks
            homeWorks


fetchClassroomSubjects = ({dispatch, getters, commit}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        subjects = getters.getClassroomSubjects

        if subjects?[0] and typeof subjects?[0] isnt 'string'
            return subjects

        http.get(CLASSROOM_SUBJECTS(id)).then (response)->
            subjects = response.data
            commit "setClassroomSubjects", subjects
            subjects


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
        subjects = dispatch('fetchClassroomSubjects',id)
        group = dispatch('group/fetchGroupWithProps', id, {root : true})

        Promise.all([activities,homeworks, subjects]).then (props) ->
            commit 'updateClassrooms', classroom
            classroom




export {pullClassroom, fetchClassroom, fetchClassrooms,fetchClassroomActivities, fetchClassroomWithProps, pullClassrooms, fetchClassroomHomeworks, fetchClassroomSubjects}
