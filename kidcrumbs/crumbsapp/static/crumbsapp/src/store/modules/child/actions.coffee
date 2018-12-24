import http from "../../../http"
import {STUDENT, STUDENTS, STUDENT_MEMBERSHIPS, STUDENT_GROUPS, STUDENT_CURRENT_GROUPS, STUDENT_HABITS, STUDENT_HABITS_BY_GROUP, STUDENT_SUBJECTS, STUDENT_ENROLLMENTS, STUDENT_CLASSROOMS, PERSON_RELATIONSHIPS, PERSON_RELATIVES} from "../../../urls";


fetchChild = ({commit, getters}, username) ->
    child = getters.getChildByUsername(username)

    if child
        return child

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
    

fetchChildRelationships = ({commit, getters}) ->
    child = getters.getChild

    return null unless child

    http.get(PERSON_RELATIONSHIPS(child.username)).then (response)->
        relationships = response.data
        commit 'setChildRelationships', relationships
        relationships

fetchChildRelatives = ({commit, getters, dispatch}) ->
    child = getters.getChild

    return null unless child

    Promise.all([http.get(PERSON_RELATIVES(child.username)), dispatch('fetchChildRelationships')]).then (response)->
        relatives = _.map response[0].data, (relative) ->
            relative.relation = _.find response[1],(relationship) ->
                relationship.relative == relative.user
            relative
        relatives = _.sortBy relatives, 'names'
        commit 'setChildRelatives', relatives
        relatives

# Fetches the currently selected childs' subjects
fetchChildSubjects = ({commit, getters}) ->
    child = getters.getChild

    return null unless child

    http.get(STUDENT_SUBJECTS(child.username)).then (response)->
        subjects = response.data
        commit 'setChildSubjects', subjects
        commit 'subject/addSubjects', subjects, {root:true}
        subjects
    

# Fetches the currently selected childs' enrollments
fetchChildEnrollments = ({commit, getters}) ->
    child = getters.getChild

    return null unless child

    http.get(STUDENT_ENROLLMENTS(child.username)).then (response)->
        enrollments = response.data
        commit 'setChildEnrollments', enrollments
        enrollments
    

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

# Fetches the currently selected childs' classrooms
fetchChildClassrooms = ({commit, getters}) ->
    child = getters.getChild

    return null unless child

    http.get(STUDENT_CLASSROOMS(child.username)).then (response)->
        classrooms = response.data
        commit 'setChildClassrooms', classrooms
        classrooms

# Fetches the currently selected childs' classrooms
fetchChildResults = ({commit, getters, dispatch}) ->
    child = getters.getChild

    return null unless child

    dispatch("result/fetchStudentResults", child.username, {root:true}).then (results) ->
        commit 'setChildResults', results
        results


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
        subjects = dispatch('fetchChildSubjects')
        relatives = dispatch('fetchChildRelatives')
        classrooms = dispatch('fetchChildClassrooms')
        results = dispatch('fetchChildResults')


        Promise.all([currentGroups, groups, memberships, habits, subjects, classrooms, results, relatives]).then (props) ->
            commit 'updateChildren', state.child
            state.child


export {fetchChild, fetchChildGroups, fetchChildCurrentGroups, fetchChildClassrooms, fetchChildMemberships ,fetchChildHabitsByGroup, fetchChildHabits, fetchChildWithProps, fetchChildSubjects, fetchChildResults, fetchChildRelationships, fetchChildRelatives}
