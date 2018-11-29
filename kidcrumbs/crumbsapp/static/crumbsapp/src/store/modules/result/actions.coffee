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
                resultSet = _.map resultSet, (result) ->
                    {assessment, enrollment, assessment:{assessment_type:assessmentType}, enrollment:{subject}} = result
                    
                    _result = _.omit result, ['enrollment', 'assessment']
                    _result.assessmentType = assessmentType.name
                    _result.assessmentMaxScore = assessment.max_score
                    _result.assessmentTerm = assessment.term.fullName
                    _result.assessmentSession = assessment.term.session.year
                    _result.currentEnrollment = enrollment.is_current
                    _result.optionalEnrollment = enrollment.is_opt
                    _result.subject = subject.name
                    _result.subjectCode = subject.subject_code
                    _result.subjectBase = subject.core_subject.name
                    _result.subjectColor = subject.color
                    _result.subjectBaseColor = subject.core_subject.color
                    _result.school = assessmentType.school
                    _result
                commit 'setResultSet', resultSet
                commit 'addResults', resultSet
                resultSet

export {fetchStudentResults}
