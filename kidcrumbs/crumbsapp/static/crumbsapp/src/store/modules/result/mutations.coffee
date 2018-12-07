mutations =

    setResultSet : (state,results) ->
        state.resultSet = results

    addResults : (state, results)->
        state.results = _.unionBy state.results, results, 'id'

    setReport : (state, report) ->
        state.report = report


    setFullReport : (state, report) ->
        state.fullReport = report

export {mutations as default}
