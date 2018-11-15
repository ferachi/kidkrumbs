import http from "../../../http";
import {GROUP, GROUPS, GROUP_STUDENTS, GROUP_HABITS, GROUP_ROUTINES} from "../../../urls";


fetchGroup = ({dispatch,commit, getters}, id) ->
    group = getters.getGroupById(id)
    if group 
        commit('setGroup', group)
        return group
    dispatch("pullGroup", id).then (group) ->
        commit('setGroup', group)
        commit('updateGroups', group)
        group



# This fetches a groups' routines
fetchGroupRoutines = ({dispatch,commit,getters}, id) -> 
    dispatch('fetchGroup', id).then (group) ->
        routines = getters.getGroupRoutines

        if routines
            return routines

        http.get(GROUP_ROUTINES(id)).then (response)->
            routines = response.data
            commit "setGroupRoutines", routines
            commit "routine/addRoutines", routines, {root : true}
            routines

fetchGroupStudents = ({dispatch, getters, commit}, id) ->
    dispatch('fetchGroup', id).then (group) ->
        students = getters.getGroupStudents

        if students
            return students

        http.get(GROUP_STUDENTS(id)).then (response)->
            students = response.data
            commit "setGroupStudents", students
            students
    
fetchGroupHabits = ({dispatch, getters, commit}, id) ->
    dispatch('fetchGroup', id).then (group) ->
        habits = getters.getGroupHabits

        if habits
            return habits

        http.get(GROUP_HABITS(id)).then (response)->
            habits = response.data
            commit "setGroupHabits", habits
            habits

fetchGroupWithProps = ({dispatch, commit, state}, id) ->
    dispatch('fetchGroup', id).then (group) ->
        students = dispatch('fetchGroupStudents', id)
        habits = dispatch('fetchGroupHabits', id)
        habits = dispatch('fetchGroupRoutines', id)

        Promise.all([students, habits]).then (props) ->
            commit 'updateGroups', state.group
            state.group



fetchGroups = ({dispatch, getters}, schoolId) ->
    groups = getters.getGroupsBySchool(schoolId)
    if groups[0]?
        return groups
    dispatch("pullGroups", schoolId).then (groups) ->
        commit 'addGroups', groups
        groups


pullGroups = ({commit}, schoolId) ->
    http.get(GROUPS).then (response)->
        response.data

pullGroup = ({commit}, id) ->
    http.get(GROUP(id)).then (response)->
        response.data


export {pullGroup, fetchGroup, fetchGroups, pullGroups, fetchGroupStudents, fetchGroupHabits,fetchGroupRoutines, fetchGroupWithProps}
