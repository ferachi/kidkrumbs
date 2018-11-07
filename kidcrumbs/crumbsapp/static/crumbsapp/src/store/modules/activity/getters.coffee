getters = 

    getActivity : (state) ->
        state.activity


    getActivities : (state) ->
        state.activities


    getActivityById : (state) -> (id) ->
        _.findBy(state.activities, id)


    getActivitiesByGroup : (state) -> (group) ->
        _.filter(state.activities, {group})

    # latest activity not greater than todays date
    getCurrentActivity : (state , getters) ->
        # activities not greater than today
        activities = _.filter state.activities, (act) ->
            # no greater than today
            moment(act.date).isSameOrBefore(moment().format("YYYY-MM-DD"))
        activities = _.reverse _.sortBy activities, ['date']
        activities[0] if activities[0]?


    
export {getters as default}
