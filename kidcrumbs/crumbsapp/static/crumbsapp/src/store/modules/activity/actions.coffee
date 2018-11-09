import http from "../../../http";
import {GROUP_ACTIVITIES,ACTIVITIES, ACTIVITY, ACTIVITYITEMS, ACTIVITYITEM} from "../../../urls";


# Pulls a groups' activities 
# id - group id
pullActivities = ({commit}, id) ->
    http.get(GROUP_ACTIVITIES(id)).then (response)->
        activities = response.data
        commit 'setActivities', activities
        activities

pullActivity = ({commit}, id) ->
    http.get(ACTIVITY(id)).then (response)->
        activity = response.data
        activity.activities = _.map activity.activities, (act) ->
            act._time = moment(act.time, "kk:mm:ss").format "hh:mm a"
            act
        commit 'addActivity', activity
        commit 'setActivity', activity
        activity

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

export {pullActivities, pullActivity,saveActivity, deleteActivity,updateActivity, saveActivityItem, updateActivityItem, deleteActivityItem}
