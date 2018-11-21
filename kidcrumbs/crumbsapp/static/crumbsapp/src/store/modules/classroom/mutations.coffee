
mutations = 
    setClassrooms : (state, classrooms) ->
        state.classrooms = classrooms

    setClassroom : (state, classroom) ->
        state.classroom = classroom

    addClassrooms : (state, classrooms)->
        state.classrooms = _.unionBy state.classrooms, classrooms, 'id'

    updateClassrooms : (state, classroom)->
        index = _.findIndex state.classrooms, (_classroom) ->
            _classroom.id == classroom.id

        if index is -1
            state.classrooms.push(classroom)
        else 
            state.classrooms.splice(index, 1, classroom)

    setClassroomStudents : (state, students)->
        state.classroom = Object.assign {},state.classroom,{students}

    setClassroomHomeworks : (state, students)->
        state.classroom = Object.assign {},state.classroom,{students}

    setClassroomRoutines : (state, routines)->
        state.classroom = Object.assign {},state.classroom,{routines}

    setClassroomHabits : (state, habits)->
        state.classroom = Object.assign {},state.classroom,{habits}

    setClassroomActivities : (state, activities)->
        state.classroom = Object.assign {},state.classroom,{activities}

export {mutations as default}
