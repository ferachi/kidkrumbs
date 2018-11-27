<template>
    <div :id="name">
        <div class="pie-chart"></div>
    </div>
</template>
<script lang="coffee">
export default

    name : 'pieChart'

    created: () ->
        @name = _.camelCase @title

    mounted : () ->
        @pieChart()



    data : () ->
        margin : 
            top : 20
            right : 20
            bottom : 20
            left : 20
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

    methods : 
        pieChart : () ->
            width = @width - @margin.left - @margin.right
            height = @height - @margin.top - @margin.bottom;
            rfactor = 2
            radius = width/rfactor

            arc = d3.arc()
                    .innerRadius 0
                    .outerRadius radius

            arcs = d3.pie().value((d) -> d.percentage)(@data)

            svg = d3.select("##{@name} .pie-chart")
                .append("svg")
                    .classed @name, true
                    .attr 'width', @width
                    .attr 'height', @height

            pie = svg.selectAll("g")
                    .data(arcs)
                    .enter().append("g")
                        .attr "transform", "translate(#{ width/2 + @margin.left}, #{height/2 + @margin.top })"

            slices = pie.append("path")
                    .attr("fill",(d) -> d.data.color)
                    .attr "d", arc

            text = pie.append("text")
                    .text((d) -> d.data.label)
                    .attr 'fill', 'white'
                    .attr 'text-anchor', 'middle'
                    .attr 'transform' , (d) ->
                        console.log d
                        "translate(#{arc.centroid(d)})"

            tooltip = d3.select("##{@name} .pie-chart")
                        .append("div")
                            .style "position", 'absolute'
                            .style "opacity", 0.5
                            .classed "bg_0", true

            pie.on 'mouseover', (d) =>
                tooltip.transition()
                    .style 'opacity', 0.9
                tooltip.html("#{d.data.label} - #{d.data.percentage}%")
                    .classed "color_4", true
                    .style "left", "#{d3.event.pageX }px"
                    .style "top", "#{d3.event.pageY - 30}px"



</script>
