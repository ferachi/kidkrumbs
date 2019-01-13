getters =
    getSubject : (state) ->
        state.subject

    getTerm : (state) ->
        state.term


    getAssessments : (state) ->
        state.subject?.assessments

    getTerms : (state, getters) ->
        assessments = getters.getAssessments

        terms = _.map assessments, (assessment) ->
            assessment.term

        terms = _.sortBy _.uniqBy(terms, 'id'), 'fullName'
        terms

    getAssessmentsByTerm : (state, getters) ->
        assessments = getters.getAssessments
        return assessments  unless not _.isEmpty state.term

        _.filter assessments, (assessment) ->
            assessment.term.id == state.term

    getAssessmentsResults : (state, getters) ->
        assessments = getters.getAssessmentsByTerm
        groupedAssessments = _.groupBy assessments, (assessment) -> assessment.assessment_type.name
        assessmentResults = _.flatMap groupedAssessments, (_assessments, key) ->
            _.map _assessments , (assessment) ->
                {results: assessment.assessment_results, assessment : key, maxScore : assessment.max_score, term : assessment.term.id }
        assessmentResults

    getAssessmentsAverages : (state, getters) ->
        assessmentResults = getters.getAssessmentsResults
        _.reduce assessmentResults, (acc, assessment) ->
            mean = _.meanBy assessment.results, 'score'
            percentage = mean/assessment.maxScore
            scores = percentage * 100
            if not acc["#{assessment.assessment}"]
                acc["#{assessment.assessment}"] = []
            acc["#{assessment.assessment}"].push(scores)
            acc
        ,{}

    getResults : (state, getters) ->
        assessments = getters.getAssessmentsByTerm
        results = _.flatMap assessments, (assessment) ->
            _.map assessment.assessment_results, (result) ->
                result.type = assessment.assessment_type.name
                result.maxScore = assessment.max_score
                result.average = result.score/result.maxScore
                result.term = assessment.term.fullName
                result
        results


    getMinScore : (state, getters) ->
        enrollmentResults = _.groupBy getters.getResults, 'enrollment'
        results = _.map enrollmentResults, (_results) ->
            _.round _.meanBy( _results, 'average') * 100
        _.min results


    getMaxScore : (state, getters) ->
        enrollmentResults = _.groupBy getters.getResults, 'enrollment'
        results = _.map enrollmentResults, (_results) ->
            _.round _.meanBy( _results, 'average') * 100
        _.max results


    getTotalScore : (state, getters) ->
        results = getters.getResults
        total = _.sumBy results, 'score'
        overallTotal = _.sumBy results, 'maxScore'
        {total, overallTotal}

    getResultSummary : (state, getters) ->
        minScore = getters.getMinScore
        maxScore = getters.getMaxScore
        total = getters.getTotalScore['total']
        overallTotal = getters.getTotalScore['overallTotal']
        {minScore, maxScore, total, overallTotal}


    getHistogramData : (state, getters) ->
        enrollmentResults = _.groupBy getters.getResults , 'enrollment'
        _.map enrollmentResults, (results, enrollment) ->
            average = _.meanBy results, 'average'
            score = _.round(average * 100)
            {score}
            


    getTotalAverageScore : (state, getters) ->
        averages = getters.getAssessmentsAverages

        scores = _.flatMap averages, (assessment, key) ->
           assessment
            
        _.round _.mean scores

    getAssessmentAverageScore : (state, getters) ->
        averages = getters.getAssessmentsAverages

        _.reduce averages, (acc, assessment,key) ->
            average = _.round _.mean _.values assessment
            acc["#{key}"] = average
            acc
        ,{}



    getSubjects : (state) ->
        state.subjects


    getSubjectById : (state) -> (id) ->
        _.find state.subjects, {id}


export {getters as default}
