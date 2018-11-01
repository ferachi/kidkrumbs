import http from "../../../http";
import {ACTIVITIES, ACTIVITY} from "../../../urls";


pullActivity = ({commit}, id) ->
    http.get(ACTIVITY(id)).then (response)->
        activity = response.data
        commit 'addActivity', activity
        commit 'setActivity', activity
        activity
    

export {pullActivity}
