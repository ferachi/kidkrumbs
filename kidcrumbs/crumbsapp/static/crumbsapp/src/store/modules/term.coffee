import http from "../../http"
import {SCHOOL_TERMS,TERM} from "../../urls"

state =
    term : {}
    terms : []


mutations =
    setTerms : (state, terms) ->
        state.terms = terms

    setTerm : (state, term) ->
        state.term = term


getters =
    getTerms : (state) ->
        state.terms

    getTermsBySchool : (state) -> (schoolId) ->
        _.filter state.terms,{school : schoolId }

    getTerm : (state) ->
        state.term


actions =
    fetchTerms : ({commit, getters}, schoolId) ->
        terms = getters.getTermsBySchool(schoolId)
        if terms?[0]
            commit 'setTerms', terms
            return terms
            
        http.get(SCHOOL_TERMS(schoolId)).then (response) ->
            terms = response.data
            commit 'setTerms', terms
            terms

    fetchTerm : ({commit}, id) ->
        http.get(TERM(id)).then (response) ->
            term = response.data
            commit 'setTerm', term
            term



export default {
    namespaced : true,
    state,
    mutations,
    actions,
    getters
}
