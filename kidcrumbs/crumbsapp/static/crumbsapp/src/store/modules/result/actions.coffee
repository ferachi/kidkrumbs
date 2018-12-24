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

        else
            commit 'setResultSet', []
            return []

fetchReport = ({commit,getters,rootGetters}) ->
    # resultSet = getters.getResultsByStudentId(id)
    resultSet = getters.getResultSet

    reports = []

    # group by term
    groupedTermReport = _.groupBy resultSet , 'assessmentTerm'
    termReport = _.flatMap groupedTermReport, (_termReports) ->
        subjectReports = _.groupBy _termReports, 'subject'
        _.map subjectReports, (_subjectReports) ->
            sr = _subjectReports[0]
            report =
                _term : sr.assessmentTerm
                _termName : sr.assessmentTermName
                subject : sr.subject
                _position : sr.assessmentTermPosition
                _session : sr.assessmentSessionId
                _sessionYear : sr.assessmentSessionYear
                _school : sr.school
                _studentCount : sr.assessmentTermStudentTotal
                totalScore : 0
                maximumScore : 0
                averageScore : 0
                _scoreIndex :{subject:0,}


            _.reduce _subjectReports, (acc, _report ) ->
                acc['totalScore'] +=  _report.score
                acc['maximumScore'] += _report.assessmentMaxScore
                acc['averageScore'] = _.round(acc['totalScore']/acc['maximumScore'],1)
                acc[_report.assessmentType] = _report.score

                # this is used to sort the fields for the table columns
                acc['_scoreIndex'][_report.assessmentType] = _report.assessmentMaxScore
                acc['_scoreIndex']['totalScore'] = acc['maximumScore']
                acc['_scoreIndex']['maximumScore'] = acc['maximumScore'] + 1
                acc['_scoreIndex']['averageScore'] = acc['maximumScore'] + 2

                acc

            ,report
            report['grade'] = rootGetters['grade/getGrader'].gradeScale(_.round(report.averageScore * 100))
            report['_scoreIndex']['grade'] = report['_scoreIndex']['averageScore'] + 1

            report

    commit "setFullReport", _.cloneDeep(termReport)
    commit "setReport", termReport
    termReport



export {fetchStudentResults, fetchReport}
