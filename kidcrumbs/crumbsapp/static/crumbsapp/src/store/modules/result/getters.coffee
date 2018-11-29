getters = 

    getResults : (state) ->
        state.results

    getResultSet : (state) ->
        state.resultSet

    # List of scores
    getScores : (state) ->
        _.map state.resultSet , (result) ->
            result.score


    # Total scores obtained on the result set
    getTotalScores : (state, getters) ->
        _.sum getters.getScores


    getBestResult : (state) ->
        results = _.groupBy state.resultSet, 'subject'
        results

    # total obtainable scores. 
    getTotalAssessmentScores : (state, getters) ->
        getters.getBestResult
        _.sum _.map state.resultSet , (result) ->
            result.assessmentMaxScore
        
    # total average on result set
    getTotalAverageScore : (state, getters) ->
        _.round (getters.getTotalScores / getters.getTotalAssessmentScores * 100)

    # This calculates the summary of the current result set
    # Most result transforms can be derived from here except
    # if they use assessment types
    getResultSummary : (state, getters) ->
        # group by the subjects
        results = _.groupBy state.resultSet, 'subject'

        # get the summary of results for each subject 
        _.flatMap results, (_results, subject) ->

            # group them by terms
            termResults = _.groupBy _results, 'assessmentTerm'

            # get the subject base, code and session from one of the results
            subjectBase = _results[0].subjectBase
            subjectCode = _results[0].subjectCode
            subjectColor = _results[0].subjectColor
            school = _results[0].school
            session = _results[0].assessmentSession
            
            # calculate the average scores per term
            _.map termResults, (_termResults, term) ->
                score = _.sum _.map _termResults, 'score'
                maxScore = _.sum _.map _termResults, 'assessmentMaxScore'
                {school: school,subject:subject, term: term,score:score, subjectBase : subjectBase,session:session, 
                maxScore:maxScore,subjectBase:subjectBase, subjectCode : subjectCode,
                subjectColor:subjectColor,
                average:_.round(score/maxScore * 100)}

    getMinResult : (state, getters) ->
        _.minBy getters.getResultSummary, 'score'


    getMaxResult : (state,getters) ->
        _.maxBy getters.getResultSummary, 'score'


    getBaseSubjectResultSummary : (state, getters) ->
        resultSummary = getters.getResultSummary
        baseResults = _.groupBy resultSummary,'subjectBase'
        _.map baseResults, (_baseResults, base) ->
            score = _.sumBy _baseResults , 'score'
            maxScore = _.sumBy _baseResults , 'maxScore'
            average = _.round(score/maxScore * 100)
            {base, score, maxScore, average}

    getGradeFrequency : (state, getters, rootState, rootGetters) ->
        # grader has an interface of {gradeScale, gradeColor}
        grader = rootGetters['grade/getGrader']
        if grader
            grades = _.map getters.getResultSummary, (result) -> grader.gradeScale(result.score)
            _.map _.countBy(grades), (v,k) ->
                percentage = _.round((v/grades.length) * 100)
                {grade:k, percentage:percentage, color: grader.gradeColors[k] }

    getResultsByStudentId : (state) -> (id) ->
        _.filter state.result, (result) ->
            result.enrollment.student == id
        

export {getters as default}
