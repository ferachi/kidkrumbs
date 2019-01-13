import http from "../../../http"
import {SUBJECTS, SUBJECT, SUBJECT_RESULTS} from "../../../urls"


fetchSubject = ({dispatch, commit, getters}, id) ->
    subject = getters.getSubjectById(id)
    if subject
        commit 'setSubject', subject
        commit 'addSubject', subject
        return subject

    dispatch('pullSubject', id).then (_subject) ->
        subject = _subject
        schoolId = subject.core_subject.school
        gradeSystemPromise = dispatch 'grade/fetchGradeSystem', schoolId, {root : true}
        Promise.all([dispatch('pullSubjectResults', id),gradeSystemPromise]).then (responses) ->
            assessments = responses[0]
            subject.assessments = assessments
            commit 'setSubject', subject
            commit 'updateSubjects', subject
            subject

pullSubjectResults =  ({commit}, id) ->
    http.get(SUBJECT_RESULTS(id)).then (response)->
        response.data

pullSubject = ({commit}, id) ->
    http.get(SUBJECT(id)).then (response)->
        response.data


fetchSubjects = ({dispatch, commit, getters}) ->
    subjects = getters.getSubjects

    if subjects[0]?
        return subjects

    dispatch('pullSubjects').then (subjects) ->
        commit 'addSubjects', subjects
        subjects


pullSubjects = ({commit}) ->
    http.get(SUBJECTS).then (response)->
        response.data


export {fetchSubject, pullSubject,fetchSubjects, pullSubjects, pullSubjectResults}
