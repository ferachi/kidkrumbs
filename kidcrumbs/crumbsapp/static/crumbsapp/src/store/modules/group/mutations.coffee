
mutations = 
    setGroups : (state, groups) ->
        state.groups = groups
    addGroup : (state, group)->
        state.groups = _.unionBy state.groups, [group], 'id'
    addGroups : (state, groups)->
        state.groups = _.unionBy state.groups, groups, 'id'
    setGroup : (state, group) ->
        state.group = group

export {mutations as default}
