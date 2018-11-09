mutations = 
    setActivities : (state, activities) ->
        state.activities = activities
    addActivity : (state, activity)->
        state.activities = _.unionBy state.activities, [activity], 'id'
    setActivity : (state, activity) ->
        state.activity = activity

export {mutations as default}
