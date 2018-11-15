mutations = 

    setRoutines : (state, routine) ->
        state.routines = routine

    addRoutines : (state, routines)->
        state.routines = _.unionBy state.routines, routines, 'id'

    setRoutine : (state, routine) ->
        state.routine = routine

    updateRoutines : (state, routine)->
        index = _.findIndex state.routines, (_routine) ->
            _routine.id == routine.id

        if index is -1
            state.routines.push(routine)
        else 
            state.routines.splice(index, 1, routine)

    # add students routines (habits/attitudes) to the 
    # current routine
    setRoutineHabits : (state, habits)->
        state.routine = Object.assign {},state.routine,{habits}







    setStudentRoutine : (state, routine) ->
        state.studentRoutine = routine

    addStudentsRoutines : (state, routines)->
        state.studentsRoutines = _.unionBy state.studentsRoutines, routines, 'id'

    updateStudentRoutines : (state, routine)->
        index = _.findIndex state.studentsRoutines, (_routine) ->
            _routine.id == routine.id

        if index is -1
            state.studentsRoutines.push(routine)
        else 
            state.studentsRoutines.splice(index, 1, routine)

export {mutations as default}
