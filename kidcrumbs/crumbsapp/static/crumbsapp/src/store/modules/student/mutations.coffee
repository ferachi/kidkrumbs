
mutations = 
    setStudents : (state, students) ->
        state.students = students
    addStudent : (state, student)->
        state.students = _.unionBy state.students, [student], 'username'

export {mutations as default}
