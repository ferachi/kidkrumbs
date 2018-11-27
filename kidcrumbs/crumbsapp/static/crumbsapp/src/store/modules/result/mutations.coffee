mutations = 

    setResultSet : (state,results) ->
        state.resultSet = results

    addResults : (state, results)->
        state.results = _.unionBy state.results, results, 'id'

export {mutations as default}
