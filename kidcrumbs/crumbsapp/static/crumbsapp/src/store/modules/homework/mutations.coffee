mutations = 

    setHomework : (state, homework) ->
        state.homework = homework

    removeHomework : (state, homework) ->
        index = _.findIndex state.homeworks, (_homework) ->
            _homework.id == homework.id

        if index isnt -1
            state.homeworks.splice(index, 1)

    updateHomeworks : (state, homework)->
        index = _.findIndex state.homeworks, (_homework) ->
            _homework.id == homework.id

        if index is -1
            state.homeworks.push(homework)
        else 
            state.homeworks.splice(index, 1, homework)

    addHomework : (state, homework) ->
        state.homeworks = _.unionBy state.homeworks, [homework], 'id'

    addHomeworks : (state, homeworks) ->
        state.homeworks = _.unionBy state.homeworks, homeworks, 'id'

export {mutations as default}

