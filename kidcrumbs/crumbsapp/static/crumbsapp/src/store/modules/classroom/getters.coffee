getters =
    getClassrooms : (state) ->
        state.classrooms


    getClassroom : (state) ->
        state.classroom


    getClassroomHomeworks : (state) ->
        state.classroom?.homeWorks


    getClassroomSubjects : (state) ->
        state.classroom?.subjects

    getClassroomById : (state) -> (id) ->
        _.find(state.classrooms, {id})


    getClassroomsBySchool : (state) -> (id) ->
        _.filter(state.classrooms, ["school", id])


    getActivities : (state) -> 
        state.classroom?.activities


export {getters as default}
