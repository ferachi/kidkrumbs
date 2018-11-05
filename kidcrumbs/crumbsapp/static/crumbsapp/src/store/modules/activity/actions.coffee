import http from "../../../http";
import {ACTIVITIES, ACTIVITY, ACTIVITYITEMS, ACTIVITYITEM} from "../../../urls";


pullActivity = ({commit}, id) ->
    http.get(ACTIVITY(id)).then (response)->
        activity = response.data
        activity.activities = _.map activity.activities, (act) ->
            act._time = moment(act.time, "kk:mm:ss").format "hh:mm a"
            act
        commit 'addActivity', activity
        commit 'setActivity', activity
        activity
    
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
        dispatch('pullActivity',activity).then (activity) ->
            item

export {pullActivity, saveActivityItem, updateActivityItem, deleteActivityItem}
