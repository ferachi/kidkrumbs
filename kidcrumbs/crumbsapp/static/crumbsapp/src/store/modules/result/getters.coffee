getters = 

    getResults : (state) ->
        state.results

    getResultSet : (state) ->
        state.resultSet

    getScores : (state) ->
        _.map state.resultSet , (result) ->
            result.score

    getTotalScores : (state, getters) ->
        _.sum getters.getScores

    getTotalAssessmentScores : (state, getters) ->
        _.sum _.map state.resultSet , (result) ->
            result.assessment.max_score
        
    getMinScore : (state) ->
        _.minBy state.resultSet, 'score'

    getMaxScore : (state) ->
        _.maxBy state.resultSet, 'score'

    getResultsByStudentId : (state) -> (id) ->
        _.filter state.result, (result) ->
            result.enrollment.student == id
        

export {getters as default}
