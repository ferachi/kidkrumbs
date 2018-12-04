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


    # total obtainable scores. 
    getTotalAssessmentScores : (state) ->
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
            session = _results[0].assessmentSessionId
            
            # calculate the average scores per term
            _.map termResults, (_termResults, term) ->
                termEnd = _termResults[0].assessmentTermEnd
                sessionStart = _termResults[0].assessmentSessionStart
                sessionEnd = _termResults[0].assessmentSessionEnd
                termPosition = _termResults[0].assessmentTermPosition
                studentTotal = _termResults[0].assessmentTermStudentTotal
                score = _.sum _.map _termResults, 'score'
                maxScore = _.sum _.map _termResults, 'assessmentMaxScore'
                {school: school,subject:subject, term: term,score:score, subjectBase : subjectBase,session:session, 
                maxScore:maxScore,subjectBase:subjectBase, subjectCode : subjectCode,
                subjectColor:subjectColor,termEnd:termEnd, term:term, position:termPosition, studentTotal : studentTotal,
                average:_.round(score/maxScore * 100), sessionStart, sessionEnd}

    getMinResult : (state, getters) ->
        _.minBy getters.getResultSummary, 'score'

    getMaxResult : (state,getters) ->
        _.maxBy getters.getResultSummary, 'score'

    getSessionDuration : (state,getters) ->
        sessionDates = _.map getters.getResultSummary, 'sessionStart'
        {start : moment(_.min sessionDates).format("YYYY"), end : moment(_.max sessionDates).format("YYYY") }

    # gets the percentage scored per assessment type
    getAssessmentPercentageScores : (state, getters) ->
        results = getters.getResultSet

        # group by assessment type first
        assessmentTypeResults = _.groupBy results, "assessmentType" 

        _.map assessmentTypeResults, (_results, assessment) ->
            score = _.sum _.map _results, 'score'
            maxScore = _.sum _.map _results, 'assessmentMaxScore'
            averageScore = _.round(score/maxScore * 100)
            color = _results[0].assessmentColor
            {assessment, score, maxScore, averageScore, color}


    getPercentageAssessmentWritten : (state, getters) ->
        results = getters.getResultSet

        assessmentCount = results.length
        
        # group by assessment type first
        assessmentTypeResults = _.groupBy results, "assessmentType" 

        _.map assessmentTypeResults, (_results, assessment) ->
            count = _results.length
            percentage = _.round(count/assessmentCount * 100)
            color = _results[0].assessmentColor
            {assessment, count, percentage, color}


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
