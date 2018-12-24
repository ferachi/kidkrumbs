import http from "../../../http"
import {CLASSROOM, SCHOOL_CLASSROOMS, CLASSROOM_MEMBERS, CLASSROOM_SUBJECTS, GROUP_STUDENTS, GROUP_HABITS, GROUP_ROUTINES, GROUP_ACTIVITIES, CLASSROOM_HOMEWORKS } from "../../../urls"


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
                homework.isExpired = moment(homework.submission_date, "YYYY-MM-DD").isBefore(moment().format("YYYY-MM-DD"))
                homework._name = homework.subject.name
                homework
            commit "setClassroomHomeworks", homeWorks
            commit "homework/setHomeworks", homeWorks, {root:true}
            homeWorks

fetchClassroomHabits = ({dispatch, getters, commit}, id) ->
    dispatch('fetchClassroom', id).then (group) ->
        habits = getters.getClassroomHabits

        if habits
            return habits

        http.get(GROUP_HABITS(id)).then (response)->
            habits = response.data
            commit "setClassroomHabits", habits
            habits

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


fetchClassroomMembers = ({dispatch, getters, commit}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        members = getters.getClassroomMembers

        if members?[0] and typeof members[0] isnt 'string'
            return members

        http.get(CLASSROOM_MEMBERS(id)).then (response)->
            members = response.data
            commit "setClassroomMembers", members
            members

fetchClassroomWithProps = ({commit, dispatch, getters, state}, id) ->
    dispatch('fetchClassroom', id).then (classroom) ->
        activities = dispatch('fetchClassroomActivities', id)
        homeworks = dispatch('fetchClassroomHomeworks',id)
        habits = dispatch('fetchClassroomHabits',id)
        subjects = dispatch('fetchClassroomSubjects',id)
        members = dispatch('fetchClassroomMembers',id)
        group = dispatch('group/fetchGroupWithProps', id, {root : true})

        Promise.all([activities,homeworks, subjects, group, members]).then (props) ->
            commit 'updateClassrooms', classroom
            classroom




export {pullClassroom, fetchClassroom, fetchClassrooms,fetchClassroomHabits, fetchClassroomActivities, fetchClassroomWithProps, pullClassrooms, fetchClassroomHomeworks, fetchClassroomSubjects, fetchClassroomMembers}
