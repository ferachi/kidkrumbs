getters =
    getEnrollments : (state) ->
        state.enrollments

    getSession : (state) ->
        state.session

    getClassroom : (state) ->
        state.classroom

    getTerm : (state) ->
        state.term

    getBaseSubject : (state) ->
        state.baseSubject

    getSubject : (state) ->
        state.subject

    getAssessments : (state) ->
        state.assessments

    getEnrollmentsBySchool : (state) -> (schoolId) ->
        _.filter state.enrollments, (enrollment) ->
            enrollment.subject.core_subject.school == schoolId

    getAssessmentsBySchool : (state) -> (schoolId) ->
        _.filter state.assessments, (assessment) ->
            assessment.subject.core_subject.school == schoolId

    getEnrollmentResults : (state) ->
        state.enrollmentResults

    getSessions : (state) ->
        return [] unless state.enrollmentResults[0]?
        
        sessions = _.flatMap state.enrollmentResults, (enrollment)->
            _.map enrollment.assessments, (assessment) ->
                assessment.term.session

        sessions = _.uniqBy sessions, 'id'
        sessions

    getTerms : (state) ->
        return [] unless state.enrollmentResults[0]?
        
        terms = _.flatMap state.enrollmentResults, (enrollment)->
            _.map enrollment.assessments, (assessment) ->
                assessment.term

        terms = _.uniqBy terms, 'id'
        _.sortBy terms, ['fullName']

    getTermsBySession : (state, getters) ->
        return [] unless getters.getTerms[0]?

        return getters.getTerms if _.isEmpty state.session

        terms = _.filter getters.getTerms, (term) ->
                term.session.id == state.session
        terms

    getSubjects : (state) ->
        return [] unless state.enrollmentResults[0]?
        
        subjects = _.flatMap state.enrollmentResults, (enrollment)->
            _.map enrollment.assessments, (assessment) ->
                assessment.subject

        subjects = _.uniqBy subjects, 'id'
        _.sortBy subjects, ['name']

    getAssessmentTypes : (state) ->
        return [] unless state.enrollmentResults[0]?
        
        assessments = _.flatMap state.enrollmentResults, (enrollment)->
            _.map enrollment.assessments, (assessment) ->
                assessment.assessment_type.name

        assessments = _.uniq assessments
        assessments


    # get subject by base and session
    getSubjectsByBaseNSession : (state, getters) ->
        return [] unless getters.getSubjects[0]?


        subjects =  getters.getSubjects if _.isEmpty state.baseSubject

        unless _.isEmpty(state.baseSubject)
            subjects  = _.filter getters.getSubjects, (subject) ->
                subject.core_subject == state.baseSubject
        
        return subjects if _.isEmpty state.session
            

        subjects  = _.filter subjects, (subject) ->
            subject.session == state.session

        subjects


    getBaseSubjects : (state) ->
        return [] unless state.enrollmentResults[0]?
        
        subjects = _.flatMap state.enrollmentResults, (enrollment)->
            enrollment.subject.core_subject

        subjects = _.uniqBy subjects, 'id'
        _.sortBy subjects, ['name']


    getClassrooms : (state) ->
        return [] unless state.enrollmentResults[0]?

        classrooms = _.map state.enrollmentResults, (enrollment) ->
            enrollment.classroom

        classrooms = _.uniqBy classrooms, 'id'
        classrooms

    getClassroomsBySession : (state, getters) ->
        return [] unless getters.getClassrooms[0]?

        return getters.getClassrooms if _.isEmpty state.session

        classrooms = _.filter getters.getClassrooms, (classroom) ->
                classroom.session.id == state.session
        classrooms

    getEnrollmentsBySession : (state, getters) ->
        enrollments = getters.getEnrollmentResults
        session = getters.getSession

        return enrollments if _.isEmpty session

        enrollments = _.filter enrollments, (enrollment) ->
            assessments = _.filter enrollment.assessments, (assessment) ->
                assessment.term.session.id == session
            assessments[0]?
        enrollments

    getEnrollmentsByClass : (state, getters) ->
        enrollments = getters.getEnrollmentsBySession
        classroom = getters.getClassroom

        return enrollments if _.isEmpty classroom

        enrollments = _.filter enrollments, (enrollment) ->
            enrollment.classroom.id == classroom

        enrollments

    getEnrollmentsByTerm : (state, getters) ->
        enrollments = getters.getEnrollmentsByClass
        term = getters.getTerm

        return enrollments if _.isEmpty term

        enrollments = _.filter enrollments, (enrollment) ->
            assessments = _.filter enrollment.assessments, (assessment) ->
                assessment.term.id == term
            assessments[0]?
        enrollments


    getEnrollmentsByBaseSubject : (state, getters) ->
        enrollments = getters.getEnrollmentsByTerm
        baseSubject = getters.getBaseSubject

        return enrollments if _.isEmpty baseSubject

        enrollments = _.filter enrollments, (enrollment) ->
            enrollment.subject.core_subject.id == baseSubject

        enrollments

         
    getEnrollmentsBySubject : (state, getters) ->
        enrollments = getters.getEnrollmentsByBaseSubject
        subject = getters.getSubject

        return enrollments if _.isEmpty subject

        enrollments = _.filter enrollments, (enrollment) ->
            enrollment.subject.id == subject

        enrollments


    _getResultSheet : (state, getters) ->
        sheet = _.flatMap getters.getEnrollmentsBySubject, (enrollment) ->
            results = _.groupBy enrollment.results, 'term'
            _.map results, (_results, term) ->
                result = _.reduce _results, (acc, res) ->
                    acc[res.type] = if acc[res.type]? then parseInt(acc[res.type]) + parseInt(res.score) else res.score
                    acc['total'] = if acc['total']? then parseInt(acc['total']) + parseInt(res.score) else res.score
                    acc['maxScore'] = if acc['maxScore']? then acc['maxScore'] + parseInt(res.max_score) else res.max_score
                    acc['percentage'] = _.round acc.total / acc.maxScore * 100, 0
                    acc['term'] =term
                    acc
                ,{}
                result.name = enrollment.student.names
                result

        return sheet if _.isEmpty state.term

        _.filter sheet, (result) ->
            result.term == state.term

            
    getResultSheet : (state, getters) ->
        enrollments = getters.getEnrollmentsBySubject
        sheets = _.flatMap enrollments , (enrollment) ->
            _.map enrollment.assessments, (assessment) ->
                result = _.find assessment.assessment_results, (_result) ->
                    _result.enrollment == enrollment.id


                sheet =
                    maxScore : assessment.max_score
                    subject : enrollment.subject.name
                    type : assessment.assessment_type.name
                    term : assessment.term.id
                    student : enrollment.student.names
                    enrollment : enrollment.id

                if result
                    sheet.score = result.score
                else
                    sheet.score = null
                sheet


        unless _.isEmpty state.term
            sheets = _.filter sheets, (result) ->
                result.term == state.term

        results = _.groupBy sheets, (sheet) -> [sheet.term, sheet.student, sheet.subject]

        mapResults = _.map results, (_results, key) ->
            result = _.reduce _results, (acc, res) ->
                acc[res.type] = res.score
                if res.score
                    acc['total'] = if acc['total']? then parseInt(acc['total']) + parseInt(res.score) else res.score
                    acc['maxScore'] = if acc['maxScore']? then parseInt(acc['maxScore']) + parseInt(res.maxScore) else res.maxScore
                    acc['percentage'] = _.round acc.total / acc.maxScore * 100, 0
                acc['term'] =res.term
                acc['name'] =res.student
                acc['subject'] =res.subject
                acc['enrollment'] =res.enrollment
                acc
            ,{}
            result
        _.sortBy mapResults, ['name']

    getResultColumn : (state, getters) ->

        types = getters.getAssessmentTypes
        termAssessments = _.groupBy getters.getAssessments, (_assessment) -> _assessment.term.id
        index = 0
        columns = _.flatMap termAssessments, (_assessments, term) ->
            typeColumns = _.map _assessments, (_assessment) ->
                type = _assessment.assessment_type.name
                column =
                    field : type
                    _index : ++index
                    label : type
                    _term : term
                    type : 'number'
                column
            _columns = [{field:'name', label : 'Name', _index : 0, _term:term}]

            tailColumns = [
                {field:'total', label : 'total score', _index : ++index, _term:term, type:'number'},
                {field:'maxScore', label : 'max score', _index : ++index, _term:term, type:'number'},
                {field:'percentage', label : 'percentage %', _index : ++index, _term:term, type:'number'}
            ]


            _columns = _columns.concat typeColumns, tailColumns

        unless _.isEmpty state.term
            columns = _.filter columns, (column) ->
                column._term == state.term

        _.uniqBy columns, 'field'



    # _getResultColumn : (state, getters) ->
    #     sheet = _.flatMap getters.getEnrollmentsBySubject, (enrollment) ->
    #         results = _.groupBy enrollment.results, 'term'
    #         _.flatMap results, (_results, term) ->
    #             index = 0
    #             column = [{field:'name', label : 'Name', index : 0}]
    #             assessmentColumns = _.map _results, ( res) ->
    #                 _column =
    #                     field : res.type
    #                     _index : ++index
    #                     label : res.type
    #                 _column
    #             
    #             tailColumns = [{field:'total', label : 'total score', index : ++index},
    #             {field:'maxScore', label : 'max score', index : ++index,},
    #             {field:'percentage', label : 'percentage', index : ++index}]
    #             column = column.concat assessmentColumns, tailColumns
    #
    #     unless _.isEmpty state.term
    #         sheet = _.filter sheet, (column) ->
    #             column.term == state.term
    #
    #     _.uniqBy sheet, 'field'


export {getters as default}
