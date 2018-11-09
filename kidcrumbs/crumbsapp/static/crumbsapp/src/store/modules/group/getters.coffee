getters = 
    getGroups : (state) ->
        state.groups

    getGroup : (state) ->
        state.group

    getGroupById : (state) -> (id) ->
        _.findBy(state.groups, id)

export {getters as default}
