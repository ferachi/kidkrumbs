getters = 
    getStudents : (state) ->
        state.students

    getStudentById : (state) -> (id) ->
        _.findBy(state.students, id)

    getStudent : (state) ->
        state.student

    getMemberships : (state) ->
        state.memberships

    getGroups : (state) ->
        state.groups

    getCurrentGroups : (state) ->
        state.currentGroups

export {getters as default}
