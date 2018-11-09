import http from "../../../http";
import {STUDENT, STUDENTS, STUDENT_MEMBERSHIPS, STUDENT_GROUPS} from "../../../urls";


fetchStudent = ({commit}, username) ->
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


# Fetches a students' current groups
fetchStudentCurrentGroups = ({commit} , username) ->
    http.get(STUDENT_CURRENT_GROUPS(username)).then (response)->
        groups = response.data
        commit 'setStudentCurrentGroups', groups


export {fetchStudent}
