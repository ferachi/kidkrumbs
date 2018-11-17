mutations = 

    setChild : (state, child) ->
        state.child = child

    updateChildren : (state, child)->
        index = _.findIndex state.children, (_child) ->
            _child.username == child.username

        if index is -1
            state.children.push(child)
        else 
            state.children.splice(index, 1, child)

    setGroup : (state, group) ->
        state.group = group

    setChildMemberships : (state, memberships)->
        if state.child
            state.child = Object.assign {}, state.child,{memberships}

    setChildHabits : (state, habits)->
        if state.child
            state.child = Object.assign {}, state.child,{habits}

    setChildGroups : (state, groups)->
        state.child = Object.assign {},state.child,{groups}

    setChildCurrentGroups : (state, currentGroups)->
        if state.child
            state.child = Object.assign {}, state.child,{currentGroups}

export {mutations as default}

