import http from "../../../http";
import {GROUP} from "../../../urls";


fetchGroup = ({commit}, id) ->
    http.get(GROUP(id)).then (response)->
        group = response.data
        commit 'addGroup', group
        commit 'setGroup', group
        group
    

fetGroups = ({commit}, schoolId) ->
    http.get(GROUPS).then (response)->
        groups = response.data
        commit 'addGroups', groups
        groups


export {fetchGroup, fetGroups}
