getters = 
    getStudents : (state) ->
        state.students

    getStudentById : (state) -> (id) ->
        _.findBy(state.students, id)

export {getters as default}
