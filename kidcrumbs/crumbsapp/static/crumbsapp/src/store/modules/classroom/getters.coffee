getters = 
    getClassrooms : (state) ->
        state.classrooms

    getClassroom : (state) ->
        state.classroom

    getClassroomStudents : (state) ->
        if state.classroom
            state.classroom.students

    getClassroomHabits : (state) ->
        if state.classroom
            state.classroom.habits

    getClassroomHomeworks : (state) ->
        if state.classroom
            state.classroom.homeWorks

    getClassroomActivities : (state) ->
        if state.classroom
            state.classroom.activities

    getClassroomRoutines : (state) ->
        if state.classroom
            state.classroom.routines

    getClassroomRoutineByDate : (state, getters) -> (date) ->
        classroomRoutines = getters.getClassroomRoutines
        _.find classroomRoutines, {date}

    getClassroomById : (state) -> (id) ->
        _.find(state.classrooms, ["id", id])

    getClassroomsBySchool : (state) -> (id) ->
        _.filter(state.classrooms, ["school", id])

export {getters as default}
