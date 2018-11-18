
mutations = 
    setSubject : (state, subject) ->
        state.subject = subject

    addSubject : (state, subject)->
        state.subjects = _.unionBy state.subjects, [subject], 'id'

    addSubjects : (state, subjects)->
        state.subjects = _.unionBy state.subjects, subjects, 'id'

    updateSubjects : (state, subject)->
        index = _.findIndex state.subjects, (_subject) ->
            _subject.id == subject.id

        if index is -1
            state.subjects.push(subject)
        else 
            state.subjects.splice(index, 1, subject)


export {mutations as default}
