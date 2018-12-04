import http from "../../http";
import {SCHOOL_GRADE_SYSTEM} from "../../urls"; 

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

    getGrades : (state) ->
        if state.gradeSystem
            state.gradeSystem.grades

    getGradeSystemById : (state) -> (id) ->
        _.find state.gradeSystems, {id}

    getGradeSystemBySchool : (state) -> (school) ->
        _.find state.gradeSystems, {school}
    
    getGrader : (state, getters) -> 
        grades = getters.getGrades
        if grades
            grades = _.reverse(_.map(grades, 'grade'))
            scores = _.flatMap( state.gradeSystem.grades, (grade) -> [grade.maxScore, grade.minScore])
            colors = _.map(state.gradeSystem.grades, (_grade) -> _grade.color).reverse()
            gradeColors = _.fromPairs(_.zip(grades,colors))
            gradeScale = d3.scaleQuantile()
                            .domain(scores)
                            .range(grades)
            {gradeColors,gradeScale}



actions = 
    fetchGradeSystem : ({commit, getters}, schoolId) ->
        gradeSystem = getters.getGradeSystemBySchool(schoolId)
        if gradeSystem
            commit 'setGradeSystem', gradeSystem
            return gradeSystem
            
        http.get(SCHOOL_GRADE_SYSTEM(schoolId)).then (response) ->
            gradeSystem = response.data
            gradeSystem.grades = _.map gradeSystem.grades, (grade) ->
                { minScore : grade.min_value, maxScore : grade.max_value, grade : grade.grade_char, color : grade.color.toLowerCase()};
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
