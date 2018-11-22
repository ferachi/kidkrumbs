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

    getChildSubjects : (state) ->
        if state.child
            state.child.subjects

    getChildCurrentGroups : (state) ->
        if state.child
            state.child.currentGroups

    getCurrentClassroom : (state, getters) ->
        if state.child
            currentGroups = getters.getChildCurrentGroups
            _.find currentGroups , (group) ->
                group.classroom isnt null
            
            

export {getters as default}
