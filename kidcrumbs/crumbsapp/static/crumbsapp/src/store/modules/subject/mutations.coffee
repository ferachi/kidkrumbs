
mutations = 
    setStudent : (state, subject) ->
        state.subject = subject

    addStudent : (state, student)->
        state.students = _.unionBy state.students, [student], 'id'

    addStudents : (state, students)->
        state.students = _.unionBy state.students, students, 'id'

    updateStudents : (state, student)->
        index = _.findIndex state.students, (_student) ->
            _student.id == student.id

        if index is -1
            state.students.push(student)
        else 
            state.students.splice(index, 1, student)


export {mutations as default}
