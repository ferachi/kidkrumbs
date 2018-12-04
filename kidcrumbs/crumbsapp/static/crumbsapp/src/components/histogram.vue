<template>
    <div :id="name">
        <div class="histogram"></div>
    </div>
</template>
<script lang="coffee">
export default

    name : 'histogram'

    created: () ->
        @name = _.camelCase @title
        width = @width - @margin.left - @margin.right
        height = @height - @margin.top - @margin.bottom




    mounted : () ->
        width = @width - @margin.left - @margin.right
        height = @height - @margin.top - @margin.bottom
        histogramData = d3.histogram().value((d) ->  d.score)(@data)
        formatCount = d3.format(",.0f");

        @yScale = d3.scaleLinear()
            .domain([0,d3.max(histogramData, (h) -> h.length + 1)])
            .range([height, 0])

        @xScale = d3.scaleLinear()
                    .domain([0, 100])
                    .rangeRound([0,width])
        barWidth = _.max(_.map(histogramData, (d) =>  @xScale(d.x1) - @xScale(d.x0)))

        svg = d3.select("##{@name} .histogram")
            .append("svg")
                .classed @name, true
                .attr 'width', @width
                .attr 'height', @height

        canvas = svg.append("g")
                    .classed "canvas", true
                    .attr "transform", "translate(#{@margin.left}, #{@margin.top})"

        bars = canvas.selectAll("g")
                .data(histogramData)
                .enter().append("g")
                    .classed 'bar',true
                    .attr "transform", (d) =>
                        x = Math.floor(d.x0/10) * 10
                        "translate(#{@xScale(x)}, #{ @yScale(d.length)})"
                .append("rect")
                    .attr "height", (d) => height - @yScale(d.length)
                    .attr "width", barWidth
                    .classed "primary-fill stroke_1" , true

        canvas.selectAll('g.bar').append("text")
            .attr("dy", ".75em")
            .attr("y", 4)
            .attr("x", barWidth/2 )
            .attr("text-anchor", "middle")
            .attr("fill", "ghostwhite")
            .text((d) => formatCount(d.length) )

        hGuide = svg.append("g")
            .attr("transform", "translate(#{@margin.left}, #{ height + @margin.top} )")
                .call(d3.axisBottom(@xScale))
        hGuide.selectAll('path')
                .attr("fill", 'transparent')
                .attr("class", "stroke_3")
        hGuide.selectAll('line')
                .attr("class", "stroke_3")
        hGuide.selectAll('text')
                .attr("class", "fill_3")
        console.log histogramData


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
        showGuide :
            type : Boolean
            default : false

        showGrid :
            type : Boolean
            default : true
    methods :
        histogram : () ->

            if @showGrid
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

            if @showGuide
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
                                .attr "font-size", "0.8em"
                                .attr "y", (d) =>
                                    @yScale(d.score) + @margin.bottom/2
                                .attr "x", (d, i) =>
                                    @xScale.bandwidth()/2
            canvas.selectAll("g.bar").append("g")
                .attr("transform", (d) => "translate(10,#{@yScale(d.score)- 10}) rotate(90)")
                .append('text')
                .text((d) => "#{d.score}% #{d.label}")
                .attr('text-anchor','end')
                .attr('fill', 'white')
                .attr('font-size', '0.8em')


</script>
