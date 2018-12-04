import http from "../../../http"
import {STUDENT_RESULTS, STUDENT_TERM_POSITIONS} from "../../../urls"


fetchStudentResults = ({commit,dispatch, getters}, id) ->
    resultSet = getters.getResultsByStudentId(id)
    
    if resultSet.length > 0
        commit 'setResultSet', resultSet
        return  resultSet

    Promise.all([http.get(STUDENT_RESULTS(id)), http.get(STUDENT_TERM_POSITIONS(id))]).then (responses) ->
        resultSet = responses[0].data
        if resultSet?[0]
            # TODO:
            # What if the student has more than one school and each have
            # different grade systems?
            # Use the grade of the current school. But how do you know the current school.
            # By the last current session (or session within the current year)
            school = resultSet[0].assessment.assessment_type.school
            dispatch('grade/fetchGradeSystem',school, {root : true}).then (gradeSystem) ->
                resultSet = _.map resultSet, (result) ->
                    {assessment, enrollment, assessment:{assessment_type:assessmentType}, enrollment:{subject}} = result

                    termPosition = _.find(responses[1].data, (p) -> p.term_id == assessment.term.id)
                    
                    _result = _.omit result, ['enrollment', 'assessment']
                    _result.assessmentType = assessmentType.name
                    _result.assessmentColor = assessmentType.color
                    _result.assessmentMaxScore = assessment.max_score
                    _result.assessmentTermName = assessment.term.fullName
                    _result.assessmentTerm = assessment.term.id
                    _result.assessmentTermStart = assessment.term.start_date
                    _result.assessmentTermEnd = assessment.term.end_date
                    _result.assessmentTermPosition = termPosition?.position
                    _result.assessmentTermStudentTotal = termPosition?.total_count
                    _result.assessmentSessionYear = assessment.term.session.year
                    _result.assessmentSessionId = assessment.term.session.id
                    _result.assessmentSessionStart = assessment.term.session.start_date
                    _result.assessmentSessionEnd = assessment.term.session.end_date
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
