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
            state.child.memberships = memberships

    setChildGroups : (state, groups)->
        if state.child
            state.child.groups = groups

    setChildCurrentGroups : (state, currentGroups)->
        if state.child
            state.child.currentGroups = currentGroups

export {mutations as default}

