getters = 
    getGroups : (state) ->
        state.groups

    getGroup : (state) ->
        state.group

    getGroupStudents : (state) ->
        if state.group
            state.group.students

    getGroupHabits : (state) ->
        if state.group
            state.group.habits

    getGroupRoutines : (state) ->
        if state.group
            state.group.routines

    getGroupRoutineByDate : (state, getters) -> (date) ->
        groupRoutines = getters.getGroupRoutines
        _.find groupRoutines, {date}

    getGroupById : (state) -> (id) ->
        _.find(state.groups, ["id", id])

    getGroupsBySchool : (state) -> (id) ->
        _.filter(state.groups, ["school", id])

export {getters as default}
