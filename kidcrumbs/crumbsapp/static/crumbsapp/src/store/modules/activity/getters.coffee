getters = 

    getActivity : (state) ->
        state.activity

    getActivities : (state) ->
        state.activities

    getActivityById : (state) -> (id) ->
        _.findBy(state.activities, id)

    getActivitiesByGroup : (state) -> (group) ->
        _.filter(state.activities, {group})

export {getters as default}
