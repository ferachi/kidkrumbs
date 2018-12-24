getters =
    getClassrooms : (state) ->
        state.classrooms


    getClassroom : (state) ->
        state.classroom


    getClassroomHomeworks : (state) ->
        state.classroom?.homeWorks

    getClassroomMembers : (state) ->
        state.classroom?.members

    getClassroomSubjects : (state) ->
        state.classroom?.subjects

    getClassroomHabits : (state) ->
        state.classroom?.habits

    getClassroomById : (state) -> (id) ->
        _.find(state.classrooms, {id})


    getClassroomsBySchool : (state) -> (id) ->
        _.filter(state.classrooms, ["school", id])


    getActivities : (state) -> 
        state.classroom?.activities


export {getters as default}
