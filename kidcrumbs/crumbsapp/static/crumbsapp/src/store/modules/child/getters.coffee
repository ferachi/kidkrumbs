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

    getChildHabits : (state) ->
        if state.child
            state.child.habits
        else
            []


    getChildHabitsByGroup : (state, getters) -> (groupId) ->
        habits = getters.getChildHabits
        _.filter habits, (habit) ->
            habit.routine.group == groupId


    getChildGroups : (state) ->
        if state.child
            state.child.groups


    getChildRelationships : (state) ->
        state.child?.relationships

        
    getChildRelationships : (state) ->
        state.child?.relatives


    getChildResults : (state) ->
        if state.child
            state.child.results


    getChildClassrooms : (state) ->
        state.child?.classrooms

    getChildSubjects : (state) ->
        if state.child
            state.child.subjects

    getChildCurrentGroups : (state) ->
        if state.child
            state.child.currentGroups

    getChildClassroom : (state) ->
        state.child?.classroom

    getCurrentClassroom : (state, getters) ->
        if state.child
            currentGroups = getters.getChildCurrentGroups
            group = _.find currentGroups , (group) ->
                group.classroom isnt null
            group =if group? then group else {}
            group
            

export {getters as default}
