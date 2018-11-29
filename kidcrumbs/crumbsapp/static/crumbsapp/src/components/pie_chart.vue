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
            left : 40
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
                        "translate(#{arc.centroid(d)})"

            display = pie.append("g")
                        .classed "display" , true
                        .attr "transform",(d, i ) =>
                            "translate(#{-width/2 - @margin.left},#{ -height/2 + @margin.top + (i * 35) })"
                        .append("rect")
                        .attr "width" , "30"
                        .attr "height" , "30"
                        .attr "fill", (d) -> d.data.color

            display = pie.selectAll("g.display")
                        .append("text")
                        .text( (d) -> "#{d.data.percentage}%" )
                        .attr 'text-anchor', 'middle'
                        .attr 'font-size', '0.8em'
                        .attr "class", "fill_0" 
                        .attr "y", 20 
                        .attr "x", 15 




</script>
