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
        sessionDates = _.flatMap getters.getResultSummary,(result)-> [result.sessionStart, result.sessionEnd]
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

    getResultTerms : (state, getters) ->
        terms = _.uniq _.map getters.getResultSet,'assessmentTermName'
        terms.sort()

    getResultSessions : (state, getters) ->
        sessions = _.uniq _.map getters.getResultSet,'assessmentSessionYear'
        sessions.sort()

    getReportBySession : (state, getters, rootState, rootGetters) -> (session) ->
        if session.term?
            report = _.filter getters.getFullReport, (rep) ->
                rep._sessionYear == session.name and rep._termName == session.term
            report
        else
            unAfColumns = ['subject', 'averageScore','grade']
            report = _.filter getters.getFullReport, (rep) ->
                rep._sessionYear == session.name
            report = _(report).groupBy('subject').map( (rows) ->
                _.reduce(rows, (acc, row) ->
                    keys = _.keys(row._scoreIndex)
                    _.forEach keys, (key) ->
                        unless _.includes unAfColumns, key
                            acc[key] = if acc[key]? then row[key] + acc[key] else row[key]
                            
                    acc['subject'] = row['subject']
                    acc['averageScore'] = _.round(acc['totalScore']/acc['maximumScore'],1)
                    acc['grade'] = rootGetters['grade/getGrader'].gradeScale(_.round(acc.averageScore * 100))

                    _.forEach _.keys(row), (key) ->
                        if key.startsWith('_')
                            acc[key] = row[key]
                    acc
                ,{})
            ).value()
            report

        
    getTableReport : (state, getters) ->
        rows = getters.getReport
        columns =_.flatMap rows, (row) ->
            keys = _(row._scoreIndex).toPairs().sortBy(1).fromPairs().keys().value()
            _.map keys, (key) ->
                column = {label : _.replace(_.snakeCase(key),'_',' '), field : key}
                if key == 'averageScore'
                    column['type'] = 'percentage'
                else
                    unless _.includes(['grade','subject'],key)
                        column['type'] = 'number'
                column
        columns = _.uniqBy columns, 'field'
        {rows, columns}

    getReportSummary : (state, getters, rootState, rootGetters) ->
        report = getters.getReport
        total = _(report).map('totalScore').sum()
        maximum = _(report).map('maximumScore').sum()
        average = _.round(total/maximum * 100,0)
        maxScore = _.maxBy(report, 'totalScore')
        minScore = _.minBy(report, 'totalScore')
        grade = rootGetters['grade/getGrader']?.gradeScale(average)
        color = rootGetters['grade/getGrader']?.gradeColors[grade]
        {total,maximum, average, maxScore, minScore, grade, color }



    getReport : (state) ->
        state.report

    getFullReport : (state) ->
        state.fullReport

export {getters as default}
