<template>
    <div :id="name">
        <div class="bar-chart"></div>
    </div>
</template>
<script lang="coffee">
export default

    name : 'barChart'

    created: () ->
        @name = _.camelCase @title
        width = @width - @margin.left - @margin.right
        height = @height - @margin.top - @margin.bottom;


        grades = _.reverse _.map @grading, 'grade'
        scores = _.flatMap @grading, (grade) -> [grade.maxScore, grade.minScore]
        @grader = d3.scaleQuantile()
                    .domain(scores)
                    .range(grades)

        gradeColors = _.reverse _.map @grading, 'color'
        maximumScores = _.reverse _.map @grading, 'maxScore'

        @colorScale = d3.scaleLinear()
                        .domain([0,...maximumScores])
                        .range([gradeColors[0],...gradeColors])

        @yScale = d3.scaleLinear()
            .domain([0,d3.max(@grading, (grade) -> grade.maxScore)])
            .range([0, height])

        labels = _.map @data, 'label'
        @xScale = d3.scaleBand()
                    .domain(labels)
                    .rangeRound([0,width])
                    .paddingInner(0.05)


    mounted : () ->
        width = @width - @margin.left - @margin.right
        height = @height - @margin.top - @margin.bottom;

        svg = d3.select("##{@name} .bar-chart")
            .append("svg")
                .classed @name, true
                .attr 'width', @width
                .attr 'height', @height
        
        gridLines = 50
        xgridScale = d3.scaleLinear()
                        .domain([0,gridLines])
                        .rangeRound([0, width])

        ygridScale = d3.scaleLinear()
                        .domain([0,gridLines])
                        .rangeRound([0, height])

        # 1 is added to close the grids
        gridRange = d3.range(gridLines + 1)

        xgrid = svg.append("g")
                    .attr "transform", "translate(#{@margin.left}, #{@margin.top})"
                    .selectAll("line").data(gridRange)
                    .enter().append("line")
                    .attr('x1', (d, i) =>  xgridScale(d))
                    .attr('x2', (d, i) =>  xgridScale(d))
                    .attr('y1', (d) => 0)
                    .attr('y2', (d) => height )
                    .attr('class', 'stroke_1')
                    .attr("stroke-width", '1')
                    .attr("fill", 'transparent');

        ygrid = svg.append("g")
                    .attr "transform", "translate(#{@margin.left}, #{@margin.top})"
                    .selectAll("line").data(gridRange)
                    .enter().append("line")
                    .attr('x1',0)
                    .attr('x2', width)
                    .attr('y1', (d) => ygridScale(d))
                    .attr('y2', (d) => ygridScale(d))
                    .attr('class', 'stroke_1')
                    .attr("stroke-width", '1')
                    .attr("fill", 'transparent');

        if showVG?
            vGuideScale = d3.scaleLinear()
                            .domain([0,d3.max(@grading, (g) -> g.maxScore)])
                            .range([height, 0])

            yAxis = d3.axisLeft(vGuideScale)        
            
            vGuide = svg.append("g")
                        .attr "transform", "translate(#{@margin.left}, #{@margin.top})"
                        .call(yAxis)

            vGuide.selectAll('path')
                .attr("fill", 'transparent')
                .attr("class", "stroke_1")

            vGuide.selectAll('line')
                .attr('class', 'stroke_1')
                .attr("fill", 'transparent')

            vGuide.selectAll('text')
                .attr("class", "fill_3") 
            
        canvas = svg.append("g")
                    .classed "canvas", true
                    .attr "transform", "translate(#{@margin.left}, #{@margin.top})"

        bars = canvas.selectAll("g")
                .data(@data)
                .enter().append("g")
                    .classed 'bar',true
                    .attr "transform", (d) =>
                        "translate(#{@xScale d.label}, #{ height - @yScale d.score})"
                .append("rect")
                    .attr "height", (d) => @yScale d.score
                    .attr "width", (d, i) =>  @xScale.bandwidth() 
                    .attr "fill", (d) =>
                        @colorScale d.score

        labels = canvas.selectAll("g.bar")
                        .append("text")
                            .text (d) -> d.label.split('')[0...3].join('').toUpperCase()
                            .classed "fill_4", true
                            .attr "text-anchor", "middle"
                            .attr "y", (d) =>
                                @yScale(d.score) + @margin.bottom/2                                
                            .attr "x", (d, i) => 
                                @xScale.bandwidth()/2

        tooltip = d3.select("##{@name} .bar-chart")
                    .append("div")
                        .style "position", 'absolute'
                        .style "opacity", 0.5
                        .classed "bg_0", true


        bars.on 'mouseover', (d) =>
            tooltip.transition()
                .style 'opacity', 0.9
            tooltip.html("#{d.label} - #{d.score}")
                .classed "color_4", true
                .style "left", "#{d3.event.pageX }px"
                .style "top", "#{d3.event.pageY - 30}px"


        scores = canvas.selectAll("g.bar")
                        .append("text")
                            .text (d) -> d.score
                            .classed "fill_3", true
                            .attr "text-anchor", "middle"
                            .attr "y", -10
                            .attr "x", (d, i) => 
                                @xScale.bandwidth()/2

    data : () ->
        margin : 
            top : 20
            right : 20
            bottom : 50
            left : 40
        yScale : null
        xScale : null
        grader : null
        colorScale : null


    props : 
        width : 
            type : Number
            default : 300
        height : 
            type : Number
            default : 250
        title : 
            type : String
            required : true
        data : 
            type : Array
            required : true
        grading : 
            type : Array
            required : true

</script>
