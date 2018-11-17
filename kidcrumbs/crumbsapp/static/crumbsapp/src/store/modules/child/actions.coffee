import http from "../../../http";
import {STUDENT, STUDENTS, STUDENT_MEMBERSHIPS, STUDENT_GROUPS, STUDENT_CURRENT_GROUPS, STUDENT_HABITS, STUDENT_HABITS_BY_GROUP} from "../../../urls";


fetchChild = ({commit}, username) ->
    http.get(STUDENT(username)).then (response)->
        child = response.data
        commit 'setChild', child
        commit 'updateChildren', child
        child
    

# Fetches the currently selected childs' memberships
fetchChildMemberships = ({commit, getters}) ->
    child = getters.getChild

    return null unless child 

    http.get(STUDENT_MEMBERSHIPS(child.username)).then (response)->
        memberships = response.data
        commit 'setChildMemberships', memberships
        memberships
    

# Fetches the currently selected childs' habits
fetchChildHabits = ({commit, getters}) ->
    child = getters.getChild

    return null unless child 

    http.get(STUDENT_HABITS(child.username)).then (response)->
        habits = response.data
        commit 'setChildHabits', habits
        habits
    

# Fetches the currently selected childs' habits
fetchChildHabitsByGroup = ({commit, getters}, groupId) ->
    child = getters.getChild

    return null unless child 

    http.get(STUDENT_HABITS_BY_GROUP(child.username, groupId)).then (response)->
        habits = response.data
        commit 'setChildHabits', habits
        habits


# Fetches the currently selected childs' groups
fetchChildGroups = ({commit, getters}) ->
    child = getters.getChild

    return null unless child 

    http.get(STUDENT_GROUPS(child.username)).then (response)->
        groups = response.data
        commit 'setChildGroups', groups
        groups


# Fetches the currently selected childs' current groups
fetchChildCurrentGroups = ({commit, getters}) ->
    child = getters.getChild

    return null unless child 

    http.get(STUDENT_CURRENT_GROUPS(child.username)).then (response)->
        groups = response.data
        commit 'setChildCurrentGroups', groups
        groups


fetchChildWithProps = ({commit, dispatch, getters, state}, username) ->

    dispatch('fetchChild', username).then (child) ->
        currentGroups = dispatch('fetchChildCurrentGroups')
        groups = dispatch('fetchChildGroups')
        memberships = dispatch('fetchChildMemberships')
        habits = dispatch('fetchChildHabits')

        Promise.all([currentGroups, groups, memberships, habits]).then (props) ->
            commit 'updateChildren', child
            console.log getters.getChild, getters.getChildGroups
            child


export {fetchChild, fetchChildGroups, fetchChildCurrentGroups, fetchChildMemberships ,fetchChildHabitsByGroup, fetchChildHabits, fetchChildWithProps}
