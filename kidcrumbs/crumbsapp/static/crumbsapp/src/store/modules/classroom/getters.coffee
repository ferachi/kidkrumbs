getters = 
    getClassrooms : (state) ->
        state.classrooms


    getClassroom : (state) ->
        state.classroom


    getClassroomHomeworks : (state) ->
        if state.classroom
            state.classroom.homeWorks


    getClassroomById : (state) -> (id) ->
        _.find(state.classrooms, ["id", id])


    getClassroomsBySchool : (state) -> (id) ->
        _.filter(state.classrooms, ["school", id])

export {getters as default}
