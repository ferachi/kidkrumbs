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
        @histogram()

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
            default : false

    methods :
        histogram : () ->

            width = @width - @margin.left - @margin.right
            height = @height - @margin.top - @margin.bottom
            histogramData = d3.histogram().thresholds(d3.range(0,100,10)).value((d) ->  d.score)(@data)
            formatCount = d3.format(",.0f")

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
                        .classed "primary-fill stroke_0" , true

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

    watch :
        data : (val) ->
            $("##{@name} .histogram").empty()
            @histogram()




</script>
