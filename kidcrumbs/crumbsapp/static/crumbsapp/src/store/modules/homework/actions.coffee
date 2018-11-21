import http from "../../../http";
import {HOMEWORKS, HOMEWORK} from "../../../urls";


fetchHomework = ({commit}, id) ->
    homework = getters.getHomeworkById(id)

    if homework
        return homework

    http.get(HOMEWORK(id)).then (response)->
        homework = response.data
        homework.isExpired = moment(homework.submission_date, "YYYY-MM-DD").isBefore(moment().format("YYYY-MM-DD"));
        _homework._name = homework.subject.name
        commit 'setHomework', homework
        commit 'updateHomeworks', homework
        homework
    

fetchHomeworks = ({commit, getters}) ->
    homeworks = getters.getHomeworks

    if homeworks[0]?
        return homeworks

    http.get(HOMEWORKS).then (response)->
        homeworks = _.map response.data, (homework) ->
            homework.isExpired = moment(homework.submission_date, "YYYY-MM-DD").isBefore(moment().format("YYYY-MM-DD"));
            homework._name = homework.subject.name
            homework
        commit 'addHomeworks', homeworks
        homeworks

saveHomework = ({commit}, homework) -> 
    http.post(HOMEWORKS, homework).then (response) -> 
        _homework = response.data
        _homework.isExpired = moment(homework.submission_date, "YYYY-MM-DD").isBefore(moment().format("YYYY-MM-DD"));
        _homework._name = homework.subject.name
        commit 'setHomework', _homework
        commit 'updateHomeworks', _homework
        _homework


updateHomework = ({commit}, homework) -> 
    http.put(HOMEWORK(homework.id), homework).then (response) -> 
        _homework = response.data
        _homework.isExpired = moment(homework.submission_date, "YYYY-MM-DD").isBefore(moment().format("YYYY-MM-DD"));
        _homework._name = homework.subject.name
        commit 'setHomework', _homework
        commit 'updateHomeworks', _homework
        _homework

deleteHomework = ({commit}, homework) -> 
    http.delete(HOMEWORK(homework.id)).then (response) -> 
        commit('removeHomework',homework)
        response

export { fetchHomework, fetchHomeworks, saveHomework, updateHomework, deleteHomework}

