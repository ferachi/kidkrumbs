getters = 
    getSubjects : (state) ->
        state.subjects

    getSubjectById : (state) -> (id) ->
        _.find state.subjects, id

    getSubject : (state) ->
        state.subject

export {getters as default}
