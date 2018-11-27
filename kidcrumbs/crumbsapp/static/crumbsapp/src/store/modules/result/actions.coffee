import http from "../../../http";
import {STUDENT_RESULTS} from "../../../urls";


fetchStudentResults = ({commit,dispatch, getters}, id) ->
    resultSet = getters.getResultsByStudentId(id)
    
    if resultSet.length > 0
        commit 'setResultSet', resultSet
        return  resultSet

    http.get(STUDENT_RESULTS(id)).then (response) ->
        resultSet = response.data
        if resultSet?[0]
            school = resultSet[0].assessment.assessment_type.school
            dispatch('grade/fetchGradeSystem',school, {root : true}).then (gradeSystem) ->
                commit 'setResultSet', resultSet
                commit 'addResults', resultSet
                resultSet

export {fetchStudentResults}
