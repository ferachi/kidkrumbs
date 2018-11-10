mutations = 
    setActivities : (state, activities) ->
        state.activities = activities
    addActivity : (state, activity)->
        state.activities = _.unionBy state.activities, [activity], 'id'
    setActivity : (state, activity) ->
        state.activity = activity
    addActivityComments : (state, comment) ->
        if state.activity
            comments = _.unionBy [comment], state.activity.comments, 'id'
            console.log comments, "what is comments"
            state.activity = Object.assign({}, state.activity, {comments})

export {mutations as default}
