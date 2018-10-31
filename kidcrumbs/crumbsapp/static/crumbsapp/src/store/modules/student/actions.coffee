import http from "../../../http";
import {STUDENT} from "../../../urls";


fetchStudent = ({commit}, username) ->
    http.get(STUDENT(username)).then (response)->
        student = response.data
        commit 'addStudent', student
        student
    

export {fetchStudent}
