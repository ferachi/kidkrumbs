getters = 
    getSchools : (state) ->
        state.schools

    getSchool : (state) ->
        state.school

    getSchoolStudents : (state) ->
        if state.school
            state.school.students

    getSchoolHabits : (state) ->
        if state.school
            state.school.habits

    getSchoolRoutines : (state) ->
        if state.school
            state.school.routines

    getSchoolById : (state) -> (id) ->
        _.find(state.schools, ["id", id])

    getSchoolSubjects : (state) ->
        if state.school
            state.school.subjects

export {getters as default}
