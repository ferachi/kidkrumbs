import http from "../../../http"
import {SCHOOL, SCHOOLS, SCHOOL_STUDENTS, GROUP_HABITS, SCHOOL_SUBJECTS, GROUP_ACTIVITIES, GROUP_HOME_WORKS} from "../../../urls";


fetchSchool = ({dispatch,commit, getters}, id) ->
    school = getters.getSchoolById(id)
    if school
        commit('setSchool', school)
        return school
    dispatch("pullSchool", id).then (school) ->
        commit('setSchool', school)
        commit('updateSchools', school)
        school


fetchSchools = ({dispatch, getters, commit}) ->
    dispatch("pullSchools").then (schools) ->
        commit 'addSchools', schools
        schools


pullSchools = ({commit}) ->
    http.get(SCHOOLS).then (response)->
        response.data

pullSchool = ({commit}, id) ->
    http.get(SCHOOL(id)).then (response)->
        response.data



# This fetches a schools' routines
fetchSchoolSubjects = ({dispatch,commit,getters}, id) -> 
    dispatch('fetchSchool', id).then (school) ->
        subjects = getters.getSchoolSubjects

        if subjects
            return subjects

        http.get(SCHOOL_SUBJECTS(id)).then (response)->
            subjects = response.data
            commit "setSchoolSubjects", subjects
            commit "subject/addSubjects", subjects, {root : true}
            subjects

fetchSchoolStudents = ({dispatch, getters, commit}, id) ->
    dispatch('fetchSchool', id).then (school) ->
        students = getters.getSchoolStudents

        if students
            return students

        http.get(SCHOOL_STUDENTS(id)).then (response)->
            students = _.sortBy response.data, (student) -> [student.last_name, student.first_name]
            commit "setSchoolStudents", students
            students
    
fetchSchoolHabits = ({dispatch, getters, commit}, id) ->
    dispatch('fetchSchool', id).then (school) ->
        habits = getters.getSchoolHabits

        if habits
            return habits

        http.get(GROUP_HABITS(id)).then (response)->
            habits = response.data
            commit "setSchoolHabits", habits
            habits

fetchSchoolHomeworks = ({dispatch, getters, commit}, id) ->
    dispatch('fetchSchool', id).then (school) ->
        homeWorks = getters.getSchoolHomeworks

        if homeWorks
            return homeWorks

        http.get(GROUP_HOME_WORKS(id)).then (response)->
            homeWorks = response.data
            commit "setSchoolHomeworks", homeWorks
            homeWorks

fetchSchoolActivities = ({dispatch, getters, commit}, id) ->
    dispatch('fetchSchool', id).then (school) ->
        activities = getters.getSchoolActivities

        if activities
            return activities

        http.get(GROUP_ACTIVITIES(id)).then (response)->
            activities = response.data
            commit "setSchoolActivities", activities
            commit "activity/addActivities", activities, {root:true}
            activities


export {pullSchool, fetchSchool, fetchSchools, pullSchools, fetchSchoolStudents, fetchSchoolHabits,fetchSchoolSubjects,fetchSchoolActivities, fetchSchoolHomeworks}
