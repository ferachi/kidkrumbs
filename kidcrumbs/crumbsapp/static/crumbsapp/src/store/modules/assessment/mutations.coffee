mutations =
    setEnrollments : (state, enrollments) ->
        state.enrollments = enrollments

    setEnrollmentResults : (state, enrollments) ->
        state.enrollmentResults = enrollments

    updateEnrollmentResults : (state, enrollment)->
        index = _.findIndex state.enrollmentResults, (_enrollment) ->
            _enrollment.id == enrollment.id

        if index is -1
            state.enrollmentResults.push(enrollment)
        else
            state.enrollmentResults.splice(index, 1, enrollment)
        state.enrollmentResults = _.cloneDeep state.enrollmentResults


    setAssessments : (state, assessments) ->
        state.assessments = assessments

    setSession : (state, session) ->
        state.session = session

    setTerm : (state, term) ->
        state.term = term

    setClassroom : (state, classroom) ->
        state.classroom = classroom

    setBaseSubject : (state, baseSubject) ->
        state.baseSubject = baseSubject

    setSubject : (state, subject) ->
        state.subject = subject

export {mutations as default}

