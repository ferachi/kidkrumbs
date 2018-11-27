<template>
    <div class="grade-bar" :class="name">
        <div class="d-flex align-items-center">
            <div class="col-auto">
                <div class="bar"></div>
            </div>
            <div class="col px-0" :style="{color:`${gradeColor} !important`}">
                <slot :color="gradeColor"></slot>
            </div>
        </div>
    </div>
</template>
<script lang="coffee">
export default
    name : 'gradeBar'
    created : () ->
        grades = _.reverse _.map @grading, 'grade'
        scores = _.flatMap @grading, (grade) -> [grade.maxScore, grade.minScore]
        @grader = d3.scaleQuantile()
                    .domain(scores)
                    .range(grades)

        @xScale = d3.scaleLinear()
                    .domain([0, 100])
                    .range([0,@width])

        # gradeColors = ["maroon", "red","orangered","orange", "forestgreen", "darkgreen"]
        gradeColors = _.reverse _.map @grading, 'color'
        maximumScores = _.reverse _.map @grading, 'maxScore'
        # gradeColors = ["red", "darkgreen"]

        @colorScale = d3.scaleLinear()
                        .domain([0,...maximumScores])
                        .range([gradeColors[0],...gradeColors])

        @name = _.camelCase @title


    computed : 
        gradeColor : () ->
            @colorScale @score


    mounted : () ->
        d3.select(".#{@name} .bar")
            .append("svg")
                .attr 'id',@name 
                .attr 'width', @width
                .attr 'height', @height
        @gradeChart()


    props :
        width : 
            type : Number
            default : 300

        height : 
            type : Number
            default : 10

        score : 
            type : Number
            required : true
        grading : 
            type : Array # array of object with interface {minScore, maxScore, color,grade}
            required : true

        title :
            type : String
            required : true


    data : () ->
        xScale : null
        colorScale: null
        name : ''
        grader : null

 


    methods : 
        grades : () ->
            pieces = 100
            maximum = _.maxBy(@grading, 'maxScore').maxScore
            minimum = _.minBy(@grading, 'minScore').minScore
            intercept = maximum/pieces

            for i in [minimum...maximum]
                    minScore = intercept * i
                    maxScore = minScore + intercept
                    grade = @grader(maxScore) 
                    color = @colorScale(maxScore) 
                    {minScore, maxScore, grade, color}

        gradeChart : () ->
            grades = @grades()
            d3.select(".#{@name} ##{@name}").selectAll("rect")
                .data(grades, (d) -> d.grade)
                .enter().append("rect")
                    .attr "width", (d) =>
                        @xScale(d.maxScore - d.minScore + 1)
                    .attr "height", "#{@height}px"
                    .attr "x" , (d) => @xScale(d.minScore)
                    .attr "fill", (d,i) =>
                        color = d3.color(d.color)
                        color.opacity = 0.1
                        color
                    .transition(d3.easeQuadInOut)
                    .duration(500)
                    .delay (d, i,g) =>
                        i * 10
                    .attr "fill", (d,i) =>
                        if @score > d.maxScore
                            d.color
                        else
                            color = d3.color(d.color)
                            color.opacity = 0.1
                            color

        updateChart : (score, oScore) ->
            d3.select(".grade-bar .bar ##{@name}").selectAll("rect")
                .transition()
                .duration(200)
                .delay (d, i,g) =>
                    if score > oScore
                        i * 10
                    else
                        (g.length - i) * 10

                .attr "fill", (d) =>
                    if score > d.maxScore
                        d.color
                    else
                        color = d3.color(d.color)
                        color.opacity = 0.1
                        color

    watch : 
        score : (n,o) ->
            @updateChart(n,o)
</script>
