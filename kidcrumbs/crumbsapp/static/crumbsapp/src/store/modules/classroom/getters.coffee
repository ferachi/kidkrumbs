getters =
    getClassrooms : (state) ->
        state.classrooms


    getClassroom : (state) ->
        state.classroom


    getClassroomHomeworks : (state) ->
        state.classroom?.homeWorks


    getClassroomById : (state) -> (id) ->
        _.find(state.classrooms, {id})


    getClassroomsBySchool : (state) -> (id) ->
        _.filter(state.classrooms, ["school", id])


export {getters as default}
