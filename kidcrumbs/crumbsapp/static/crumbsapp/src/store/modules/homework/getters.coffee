getters = 
    getHomework : (state) ->
        state.homework

    getHomeworks : (state) ->
        state.homeworks
            
    getHomeworkById : (state) -> (id) ->
        _.find state.homeworks, {id}

export {getters as default}
