mutations = 
    setGroups : (state, groups) ->
        state.groups = groups

    setGroup : (state, group) ->
        state.group = group

    addGroups : (state, groups)->
        state.groups = _.unionBy state.groups, groups, 'id'

    updateGroups : (state, group)->
        index = _.findIndex state.groups, (_group) ->
            _group.id == group.id

        if index is -1
            state.groups.push(group)
        else
            state.groups.splice(index, 1, group)

    setGroupStudents : (state, students)->
        state.group = Object.assign {},state.group,{students}

    setGroupHomeworks : (state, students)->
        state.group = Object.assign {},state.group,{students}

    setGroupRoutines : (state, routines)->
        state.group = Object.assign {},state.group,{routines}

    addGroupRoutine : (state, routine)->
        state.group?.routines = _.unionBy state.group?.routines, [routine], 'id'

    removeGroupRoutine : (state, routine)->
        state.group.routines = _.differenceBy state.group.routines,[routine], 'id'
        console.log(state.group.routines, 'routineee')
            
    setGroupHabits : (state, habits)->
        state.group = Object.assign {},state.group,{habits}

    setGroupActivities : (state, activities)->
        state.group = Object.assign {},state.group,{activities}

export {mutations as default}
