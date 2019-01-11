import http from "../../../http"
import {SCHOOL_ENROLLMENTS, SCHOOL_ASSESSMENTS, ASSESSMENT_RESULTS} from "../../../urls"

fetchEnrollments = ({commit, dispatch, getters},schoolId) ->
    enrollments = getters.getEnrollmentsBySchool(schoolId)

    if enrollments[0]?
        commit 'setEnrollments', enrollments
        return enrollments

    dispatch('pullEnrollments',schoolId).then (enrollments) ->
        commit 'setEnrollments', enrollments
        enrollments

pullEnrollments = ({}, schoolId) ->
    http.get(SCHOOL_ENROLLMENTS(schoolId)).then (response) ->
        response.data


fetchAssessments = ({commit, dispatch, getters},schoolId) ->
    assessments = getters.getAssessmentsBySchool(schoolId)

    if assessments[0]?
        commit 'setAssessments', assessments
        return assessments

    dispatch('pullAssessments',schoolId).then (assessments) ->
        commit 'setAssessments', assessments
        assessments


pullAssessments = ({}, schoolId) ->
    http.get(SCHOOL_ASSESSMENTS(schoolId)).then (response) ->
        response.data


fetchEnrollmentResults = ({commit, dispatch}, schoolId) ->
    assessmentsPromise = dispatch 'fetchAssessments', schoolId
    enrollmentPromise = dispatch 'fetchEnrollments', schoolId
    classroomPromise = dispatch 'classroom/fetchClassrooms', schoolId, {root : true}

    Promise.all([assessmentsPromise, enrollmentPromise, classroomPromise]).then (responses) ->
        assessments = responses[0]
        classrooms = responses[2]
        enrollments = _.map responses[1], (enrollment) ->
            enrollment.assessments = _.filter assessments , (assessment) ->
                assessment.subject.id == enrollment.subject.id

            enrollment.results = _.flatMap enrollment.assessments, (assessment) ->
                results = _.filter _.cloneDeep(assessment.assessment_results), (result) ->
                    result.enrollment == enrollment.id
                results = _.map results, (result) ->
                    assessment = _.find enrollment.assessments, (_assessment) ->
                        _assessment.id == result.assessment
                    result.term = assessment?.term.id
                    result.type = assessment?.assessment_type.name
                    result.max_score = assessment?.max_score
                    result
                results
            enrollment.classroom = _.find classrooms , (classroom) ->
                _.includes(classroom.members , enrollment.student.user) and _.includes(classroom.subjects, enrollment.subject.id)

            enrollment

        commit 'setEnrollmentResults', enrollments
        enrollments
        

saveResults = ({commit, getters, dispatch}, results) ->
    enrollments = getters.getEnrollmentsBySubject
    http.post(ASSESSMENT_RESULTS, results).then (response) ->
        results = response.data
        # schoolId = 'cc492a62-e67f-4259-b27c-6bba0e11a0c8'
        # dispatch('fetchEnrollmentResults',schoolId).then (response) ->
            # response.data
        _.map results, (result) ->
            console.log(enrollments.length, 'length')
            enrollment = _.find enrollments, (_enrollment) ->
                _enrollment.id == result.enrollment
            if enrollment
                assessment = _.find enrollment.assessments, (_assessment) ->
                    _assessment.id == result.assessment
                if assessment
                    _result = _.find enrollment.results, {id : result.id}
                    if _result
                        _result = _.assign _result, result
                    else
                        assessment.assessment_results.push result

                    commit 'updateEnrollmentResults', enrollment
                    _result

            # enrollments =  _.map _.compact(enrollments), (eResult) -> 
            #     assessment = _.find eResult.assessments, (_assessment) ->
            #         _assessment.id == result.assessment
            #     if assessment
            #         _res = _.find assessment.assessment_results, (res) ->
            #             res.id == result.id
            #         if _res
            #             _res = result
            #         else
            #             assessment.assessment_results.push(result)
            #         assessment
            # enrollments

        # commit("updateStudentRoutines", results)



updateResults = ({commit}, routine) ->
    http.put(ASSESSMENT_RESULTS, routine).then (response) ->
        routine = response.data
        commit("setStudentRoutine", routine)
        commit("updateStudentRoutines", routine)
        routine


export {pullEnrollments, fetchEnrollments, pullAssessments, fetchAssessments, fetchEnrollmentResults, saveResults}


