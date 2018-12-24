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

    setChildClassroom : (state, classroom) ->
        if state.child
            state.child = Object.assign {}, state.child,{classroom}


    setChildMemberships : (state, memberships)->
        if state.child
            state.child = Object.assign {}, state.child,{memberships}

    setChildRelationships : (state, relationships)->
        if state.child
            state.child = Object.assign {}, state.child,{relationships}

    setChildRelatives : (state, relatives)->
        if state.child
            state.child = Object.assign {}, state.child,{relatives}

    setChildHabits : (state, habits)->
        if state.child
            state.child = Object.assign {}, state.child,{habits}

    setChildGroups : (state, groups)->
        if state.child
            state.child = Object.assign {},state.child,{groups}

    setChildClassrooms : (state, classrooms)->
        if state.child
            state.child = Object.assign {},state.child,{classrooms}

    setChildEnrollments : (state, enrollments)->
        if state.child
            state.child = Object.assign {},state.child,{enrollments}

    setChildSubjects : (state, subjects)->
        if state.child
            state.child = Object.assign {},state.child,{subjects}

    setChildResults : (state, results)->
        if state.child
            state.child = Object.assign {},state.child,{results}

    setChildCurrentGroups : (state, currentGroups)->
        if state.child
            state.child = Object.assign {}, state.child,{currentGroups}

export {mutations as default}

