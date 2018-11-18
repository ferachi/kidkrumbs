getters = 
    getSubject : (state) ->
        state.subject

    getSubjects : (state) ->
        state.subjects

    getSubjectById : (state) -> (id) ->
        _.find state.subjects, {id}

export {getters as default}
