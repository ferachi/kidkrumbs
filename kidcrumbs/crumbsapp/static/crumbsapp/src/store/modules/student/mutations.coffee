
mutations = 
    setStudents : (state, students) ->
        state.students = students

    addStudent : (state, student)->
        state.students = _.unionBy state.students, [student], 'username'

    setStudent : (state, student) ->
        state.student = student

    setStudentMemberships : (state, memberships)->
        state.memberships = memberships

    setStudentGroups : (state, groups)->
        state.groups = groups

    setStudentCurrentGroups : (state, currentGroups)->
        state.currentGroups = currentGroups

export {mutations as default}
