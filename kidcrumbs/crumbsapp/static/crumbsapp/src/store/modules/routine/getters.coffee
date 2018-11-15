getters = 
    getRoutine : (state) ->
        state.routine


    getRoutines : (state) ->
        state.routines


    getRoutineById : (state) -> (id) ->
        _.find state.routines, {id}


    getRoutineHabits : (state) ->
        if state.routine
            state.routine.habits

    getStudentRoutine : (state) ->
        state.studentRoutine


    getStudentsRoutines : (state) ->
        state.studentsRoutines

    getStudentsRoutineById : (state) -> (id) ->
        _.find state.studentsRoutines, {id}

    getStudentsRoutinesByRoutineId : (state) -> (routineId) ->
        _.filter state.studentsRoutines, {routine : routineId} 

export {getters as default}
