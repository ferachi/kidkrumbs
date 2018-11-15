import http from "../../../http";
import {ROUTINE,ROUTINES, GROUP_ROUTINES,ROUTINE_STUDENT_ROUTINES, STUDENT_ROUTINES, STUDENT_ROUTINE, STUDENT_ROUTINE_ATTITUDES, ATTITUDES} from "../../../urls";



# fetches a routine from the store 
# or from the server if none exist
fetchRoutine = ({dispatch,commit, getters}, id) -> 
    routine = getters.getRoutineById(id)
    if routine
        routine
        commit('setRoutine', routine)
    else
        dispatch('pullRoutine', id).then (routine)->
            commit('setRoutine', routine)
            commit("updateRoutines", routine)
            routine


pullRoutine = ({commit}, id) ->
    http.get(ROUTINE(id)).then (response) ->
        response.data

saveRoutine = ({commit}, routine) ->
    http.post(ROUTINES, routine).then (response) ->
        routine = response.data
        commit("setRoutine", routine)
        commit("updateRoutines", routine)
        routine

deleteRoutine = ({commit, state}, id) ->
    http.delete(ROUTINE(id)).then (response) ->
        routineIndex = _.findIndex state.routines, {id}
        console.log state.routines, routineIndex, id
        if routineIndex != -1
            state.routines.splice(routineIndex, 1)
            routineIndex
        else
            id

updateRoutine = ({commit, state}, routine) ->
    http.put(ROUTINE(routine.id), routine).then (response) ->
        commit("setRoutine", routine)
        commit("updateRoutines", routine)
        routine

# fetches students routines given a routine, from the store 
# or from the server if none exist
# id - routine id 
fetchRoutineStudentsRoutines = ({dispatch, getters, commit}, id) -> 
    # set up current routine
    dispatch('fetchRoutine', id).then (routine) ->
        # get the routines habits (studentsroutines)
        habits = getters.getRoutineHabits
        if habits
            habits
        else
            dispatch('pullRoutineStudentsRoutines', id).then (routines) ->
                commit("setRoutineHabits", routines)
                commit("addStudentsRoutines", routines)
                routines


pullRoutineStudentsRoutines = ({commit}, id) ->
    http.get(ROUTINE_STUDENT_ROUTINES(id)).then (response) ->
        response.data


fetchRoutineWithProps = ({dispatch, getters, state, commit}, id) -> 
    dispatch('fetchRoutine',id).then (routine) ->
        studentsRoutines = dispatch('fetchRoutineStudentsRoutines', id)
        Promise.all([studentsRoutines]).then (props) ->
            commit('updateRoutines', state.routine)
            state.routine



################################## STUDENTS ROUTINES ######################################3

############### DETAIL  ##############

# fetches a students' routine from the store 
# or from the server if none exist
fetchStudentRoutine = ({dispatch,commit, getters}, id) -> 
    routine = getters.getStudentsRoutineById(id)

    if routine
        commit("setStudentRoutine", routine)
        commit("updateStudentRoutines", routine)
        routine

    else
        dispatch('pullStudentRoutine', id).then (routine) ->
            commit("setStudentRoutine", routine)
            commit("updateStudentRoutines", routine)
            routine


pullStudentRoutine = ({commit}, id) ->
    http.get(STUDENT_ROUTINE(id)).then (response) ->
        response.data



############ LIST ################

        
saveStudentsRoutines = ({commit}, routines) ->
    http.post(STUDENT_ROUTINES, routines).then (response) ->
        routine = response.data
        commit("setStudentRoutine", routine)
        commit("updateStudentRoutines", routine)
        routine

updateStudentsRoutine = ({commit}, routine) ->
    http.put(STUDENT_ROUTINE(routine.id), routine).then (response) ->
        routine = response.data
        commit("setStudentRoutine", routine)
        commit("updateStudentRoutines", routine)
        routine


# fetchStudentAttitudes = ({dispatch, getters}, id) -> 
#     # get the attitudes by the students' routine
#     # attitudes = getters.getAttitudesByRoutine(id)
#     # if attitudes[0]?
#     #     attitudes
#     # else
#     #     dispatch('pullStudentAttitudes', id)
#     dispatch('pullStudentAttitudes', id).then (attitudes) -> 
#         attitudes
#
#
# pullStudentAttitudes = ({commit}, id) ->
#     http.get(STUDENT_ROUTINE_ATTITUDES(id)).then (response) ->
#         attitudes = response.data
#         attitudes
#

saveStudentsAttitudes = ({commit}, attitudes) ->
    http.post(ATTITUDES, attitudes).then (response) ->
        attitudes = response.data
        attitudes


export {
    fetchRoutine,
    fetchRoutineStudentsRoutines,
    fetchRoutineWithProps
    pullRoutineStudentsRoutines,
    pullRoutine,
    saveRoutine,
    updateRoutine,
    deleteRoutine,
    fetchStudentRoutine,
    pullStudentRoutine,
    updateStudentsRoutine, 
    saveStudentsRoutines,
    saveStudentsAttitudes,
    ## fetchStudentAttitudes,
    ## pullStudentAttitudes,
}
