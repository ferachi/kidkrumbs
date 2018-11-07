getters = 
    getChild : (state) ->
        state.child

    getChildren : (state) ->
        state.children

    getGroup : (state) ->
        state.group

    getChildByUsername : (state) -> (username) ->
        _.find state.children, (child) ->
            child.username == username

    getChildMemberships : (state) ->
        if state.child
            state.child.memberships

    getChildGroups : (state) ->
        if state.child
            state.child.groups


    getChildCurrentGroups : (state) ->
        if state.child
            state.child.currentGroups



    getCurrentClassroom : (state, getters) ->
        if state.child
            currentGroups = getters.getChildCurrentGroups
            _.find currentGroups , (group) ->
                group.classroom isnt null
            
            

export {getters as default}
