<template>
    <div :id="name">
        <div class="arc-chart"></div>
    </div>
</template>
<script lang="coffee">
export default

    name : 'arcChart'

    created: () ->
        @name = _.camelCase @title

    mounted : () ->
        @arcChart()



    data : () ->
        margin :
            top : 10
            right : 20
            bottom : 30
            left : 20


    props :
        width :
            type : Number
            default : 300
        height :
            type : Number
            default : 300
        title :
            type : String
            required : true
        percentage :
            type : Number
            required : true
        label :
            type : String
            required : true
        color :
            type : String
            required : true

    methods :
        arcChart : () ->
            width = @width - @margin.left - @margin.right
            height = @height - @margin.top - @margin.bottom
            rfactor = 2
            radius = _.round(width/rfactor)


            # arc to represent the percentage scores 
            arc = d3.arc()
                    .innerRadius  radius * 8 / 10
                    .outerRadius radius
                    .startAngle 0
                    .endAngle (@percentage/100) * 2 * Math.PI


            # svg to display percentage scores
            svg = d3.select("##{@name} .arc-chart")
                .append("svg")
                    .classed @name, true
                    .attr 'width', @width
                    .attr 'height', @height


            g = svg.append("g")
                    .attr "transform", "translate(#{ width/2 + @margin.left}, #{height/2 + @margin.top })"


            curve = g.append("path")
                    .attr("fill",@color)
                    .attr "d", arc

            text = g.append("text")
                    .text(@percentage + "%")
                    .classed(" font-weight-bold fill_4", true)
                    .attr("text-anchor", "middle")
                    .attr("transform", "translate(0,20)")
                    .attr("font-size", '4em')

            text = g.append("text")
                    .text(@label)
                    .classed("fill_4", true)
                    .attr("text-anchor", "middle")
                    .attr("transform", "translate(0,#{radius + 30})")
                    .attr("font-size", '1.3em')
    watch :
        percentage : (val) ->
            $("##{@name} .arc-chart").empty()
            @arcChart()

</script>
