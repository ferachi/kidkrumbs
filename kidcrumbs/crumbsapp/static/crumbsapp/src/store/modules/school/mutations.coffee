
mutations = 
    setSchools : (state, schools) ->
        state.schools = schools

    setSchool : (state, school) ->
        state.school = school

    addSchools : (state, schools)->
        state.schools = _.unionBy state.schools, schools, 'id'

    updateSchools : (state, school)->
        index = _.findIndex state.schools, (_school) ->
            _school.id == school.id

        if index is -1
            state.schools.push(school)
        else 
            state.schools.splice(index, 1, school)

    setSchoolStudents : (state, students)->
        state.school = Object.assign {},state.school,{students}

    setSchoolHomeworks : (state, students)->
        state.school = Object.assign {},state.school,{students}

    setSchoolRoutines : (state, routines)->
        state.school = Object.assign {},state.school,{routines}

    setSchoolHabits : (state, habits)->
        state.school = Object.assign {},state.school,{habits}

    setSchoolActivities : (state, activities)->
        state.school = Object.assign {},state.school,{activities}
        
    setSchoolSubjects : (state, subjects)->
        state.school = Object.assign {},state.school,{subjects}

export {mutations as default}
