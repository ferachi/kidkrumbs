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
            top : 10
            right : 80
            bottom : 10
            left : 25
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
        labels :
            type : Array
            required : true

    methods :
        pieChart : () ->
            width = @width - @margin.left - @margin.right
            height = @height - @margin.top - @margin.bottom
            rfactor = 2
            radius = _.round(width/rfactor)

            arc = d3.arc()
                    .innerRadius 0
                    .outerRadius radius

            arcs = d3.pie().value((d) -> d.percentage)(_.sortBy @data, 'label')

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
                .text((d) -> "#{d.data.percentage}%")
                    .attr 'fill', 'white'
                    .attr 'text-anchor', 'middle'
                    .attr 'transform' , (d) ->
                        "translate(#{arc.centroid(d)})"

            displayWidth = _.round(width/15)

            display = pie.selectAll('g').data(_.sortBy(@labels, 'label')).enter().append("g")
                        .classed "display" , true
                        .attr "transform",(d, i ) => "translate(#{ width/2 +  @margin.left/2  }, #{ -((@labels.length/2) * displayWidth) + (i * (displayWidth + 5)) })"
                        .append("rect")
                        .attr "width" , "#{displayWidth}"
                        .attr "height" , "#{displayWidth}"
                        .attr "fill", (d) -> d.color

            display = pie.selectAll("g.display")
                        .append("text")
                        .text( (d) -> "#{d.label}" )
                        .attr 'font-size', '0.8em'
                        .attr "class", "fill_4"
                        .attr "y", displayWidth - 5
                        .attr "x" , displayWidth + 10


</script>
