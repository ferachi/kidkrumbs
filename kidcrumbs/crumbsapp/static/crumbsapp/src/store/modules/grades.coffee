import http from "../../http";
import {SCHOOL_GRADESYSTEM} from "../../urls"; 

state = 
    gradeSystem : null
    gradeSystems : []


mutations = 
    setGradeSystem : (state, gradeSystem) ->
        state.gradeSystem = gradeSystem
        
    addGradeSystem : (state, gradeSystem) ->
        state.gradeSystems = _.unionBy state.gradeSystems, [gradeSystem], 'id'


getters = 
    getGradeSystem : (state) ->
        state.gradeSystem

    getGradeSystems : (state) -> (id) ->
        state.gradeSystem

    getGradeSystemById : (state) -> (id) ->
        _.find state.gradeSystems, {id}

    getGradeSystemBySchool : (state) -> (school) ->
        _.find state.gradeSystems, {school}


actions = 
    fetchGradeSystem : ({commit, getters}, schoolId) ->
        gradeSystem = getters.getGradeSystemBySchool(schoolId)
        if gradeSystem
            commit 'setGradeSystem', gradeSystem
            return gradeSystem
            
        http.get(SCHOOL_GRADESYSTEM(schoolId)).then (response) ->
            gradeSystem = response.data
            commit 'setGradeSystem', gradeSystem
            commit 'addGradeSystem', gradeSystem
            gradeSystem


export default {
    namespaced : true,
    state,
    mutations,
    actions,
    getters
}
