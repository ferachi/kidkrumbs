import http from "../../../http";
import {STUDENT, STUDENTS, STUDENT_MEMBERSHIPS, STUDENT_GROUPS} from "../../../urls";


fetchStudent = ({commit}, username) ->
    student = getters.getStudent
    if student?.username == username
        student
    else
        http.get(STUDENT(username)).then (response)->
            student = response.data
            commit 'addStudent', student
            student
    

# Fetches a students' memberships
fetchStudentMemberships = ({commit} , username) ->
    http.get(STUDENT_MEMBERSHIPS(username)).then (response)->
        memberships = response.data
        commit 'setStudentMemberships', memberships
        memberships


# Fetches a students' groups
fetchStudentGroups = ({commit} , username) ->
    http.get(STUDENT_GROUPS(username)).then (response)->
        groups = response.data
        commit 'setStudentGroups', groups
        groups



# Fetches a students' current groups
fetchStudentCurrentGroups = ({commit} , username) ->
    http.get(STUDENT_CURRENT_GROUPS(username)).then (response)->
        groups = response.data
        commit 'setStudentCurrentGroups', groups
        groups



# fetches a students' results
fetchStudentResults = ({commit, getters, dispatch}, username) ->
    dispatch('fetchStudent', username).then (student) ->
        dispatch("result/fetchStudentResults", username, {root:true}).then (results) ->
            commit 'setStudentResults', results
            results


export {fetchStudent, fetchStudentResults}
