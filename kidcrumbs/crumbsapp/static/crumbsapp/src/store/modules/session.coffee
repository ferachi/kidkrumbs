import http from "../../http"
import {SCHOOL_SESSIONS,SESSION} from "../../urls"

state =
    session : {}
    sessions : []


mutations =
    setSessions : (state, sessions) ->
        state.sessions = sessions

    setSession : (state, session) ->
        state.session = session


getters =
    getSessions : (state) ->
        state.sessions

    getSessionsBySchool : (state) -> (schoolId) ->
        _.filter state.sessions,{school : schoolId }

    getSession : (state) ->
        state.session


actions =
    fetchSessions : ({commit, getters}, schoolId) ->
        sessions = getters.getSessionsBySchool(schoolId)
        if sessions?[0]
            commit 'setSessions', sessions
            return sessions
            
        http.get(SCHOOL_SESSIONS(schoolId)).then (response) ->
            sessions = response.data
            commit 'setSessions', sessions
            sessions

    fetchSession : ({commit}, id) ->
        http.get(SESSION(id)).then (response) ->
            session = response.data
            commit 'setSession', session
            session



export default {
    namespaced : true,
    state,
    mutations,
    actions,
    getters
}
