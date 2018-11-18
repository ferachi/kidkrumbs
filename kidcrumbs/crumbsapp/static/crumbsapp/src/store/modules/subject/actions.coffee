import http from "../../../http";
import {SUBJECTS, SUBJECT} from "../../../urls";


fetchSubject = ({dispatch, commit, getters}, id) ->
    subject = getters.getSubjectById(id)
    if subject
        commit 'setSubject', subject
        commit 'addSubject', subject
        return subject
    dispatch('pullSubject', id).then (subject) ->
        commit 'setSubject', subject
        commit 'updateSubjects', subject
        subject


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


export {fetchSubject, pullSubject,fetchSubjects, pullSubjects}
