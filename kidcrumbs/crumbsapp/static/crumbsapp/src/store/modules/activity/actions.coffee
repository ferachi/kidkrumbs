import http from "../../../http";
import {GROUP_ACTIVITIES,ACTIVITIES, ACTIVITY, ACTIVITYITEMS, ACTIVITYITEM, ACTIVITYCOMMENTS, ACTIVITYCOMMENTREPLIES} from "../../../urls";


# Pulls a groups' activities 
# id - group id
pullActivities = ({commit}, id) ->
    http.get(GROUP_ACTIVITIES(id)).then (response)->
        activities = response.data
        commit 'setActivities', activities
        commit 'addActivities', activities
        activities


pullActivity = ({commit}, id) ->
    http.get(ACTIVITY(id)).then (response)->
        activity = response.data
        activity.activities = _.map activity.activities, (act) ->
            act._time = moment(act.time, "kk:mm:ss").format "hh:mm a"
            act
        activity.comments = _.map activity.comments, (com) ->
            com.date = moment(com.created_date).format("h:mm a, DD MMM YYYY")
            com.replies = _.map com.replies, (rep) ->
                rep.date = moment(rep.created_date).format("h:mm a, DD MMM YYYY")
                rep
            com
        commit 'addActivity', activity
        commit 'setActivity', activity
        activity

saveComment = ({commit}, comment) ->
    http.post(ACTIVITYCOMMENTS, comment).then (response)->
        _comment = response.data
        commit("addActivityComments", _comment)
        _comment
            
saveReplyComment = ({commit, getters}, comment) ->
    console.log comment, 'what is the coment'
    http.post(ACTIVITYCOMMENTREPLIES, comment).then (response)->
        _comment = response.data
        activity = getters.getActivity
        originalComment = _.find activity.comments, {id : _comment.activity_comment}
        originalComment.replies.push(_comment)
        commit 'setActivity', activity
        _comment
            
saveActivity = ({dispatch}, item) ->
    http.post(ACTIVITIES, item).then (response)->
        activity = response.data
        dispatch('pullActivities',activity.group).then (activities) ->
            # return the activity not the list
            activity
            

updateActivity = ({dispatch}, item) ->
    http.put(ACTIVITY(item.id),item ).then (response)->
        activity = response.data
        dispatch('pullActivities',activity.group).then (activities) ->
            # return the activity not the list
            activity


deleteActivity = ({dispatch}, {id, group}) ->
    http.delete(ACTIVITY(id)).then (response)->
        dispatch('pullActivities',group)
    
saveActivityItem = ({dispatch}, item) ->
    http.post(ACTIVITYITEMS, item).then (response)->
        item = response.data
        dispatch('pullActivity',item.activity).then (activity) ->
            item


updateActivityItem = ({dispatch}, item) ->
    http.put(ACTIVITYITEM(item.id),item ).then (response)->
        item = response.data
        dispatch('pullActivity',item.activity).then (activity) ->
            item


deleteActivityItem = ({dispatch}, {id, activity}) ->
    http.delete(ACTIVITYITEM(id)).then (response)->
        dispatch('pullActivity',activity)

export {pullActivities, pullActivity,saveActivity, deleteActivity,updateActivity, saveActivityItem, updateActivityItem, deleteActivityItem, saveComment, saveReplyComment}
