mutations = 
    setActivities : (state, activities) ->
        state.activities = activities

    addActivities : (state, activities)->
        state.activityList = _.unionBy state.activities, activities, 'id'

    addActivity : (state, activity)->
        state.activities = _.unionBy state.activities, [activity], 'id'

    setActivity : (state, activity) ->
        state.activity = activity

    addActivityComments : (state, comment) ->
        if state.activity
            comments = _.unionBy [comment], state.activity.comments, 'id'
            state.activity = Object.assign({}, state.activity, {comments})

export {mutations as default}
