<template>
    <div :id="name">
        <div class="time-series"></div>
    </div>
</template>
<script lang="coffee">
export default

    name : 'timeSeries'

    created: () ->
        @name = _.camelCase @title

    mounted : () ->
        @timeSeries()

    data : () ->
        margin : 
            top : 20
            right : 20
            bottom : 50
            left : 60
        yScale : null
        xScale : null
        dateFormat:null
    

    methods : 
        timeSeries : () ->
            width = @width - @margin.left - @margin.right
            height = @height - @margin.top - @margin.bottom;

            @yScale = d3.scaleLinear()
                .domain([0,d3.max(@grades)])
                .range([0, height])

            if @invertY
                @yScale.domain([1,d3.max(@grades)])
                @yScale.range([height, 0])


            @dateFormat =  d3.timeParse("%Y-%m-%d")
            @xScale = d3.scaleTime()
                        .domain([d3.min(@data, (d) => @dateFormat(d.date)),d3.max(@data, (d) => @dateFormat(d.date))])
                        .range([0,width])

            line = d3.line()
                    .x( (d,i) => @xScale(@dateFormat(d.date)) )
                    .y( (d) =>
                        height - @yScale(d.score)
                    )

            svg = d3.select("##{@name} .time-series")
                .append("svg")
                    .classed @name, true
                    .attr 'width', @width
                    .attr 'height', @height

            xAxis = d3.axisBottom(@xScale).tickSize(10).tickFormat((date) => 
                    #get all the dates
                    dates = _.map(@data, (d) => @dateFormat(d.date))
                    minDate = d3.min(dates)
                    maxDate = d3.max(dates)
                    if moment(maxDate).diff(minDate, 'years') > 2
                        return d3.timeFormat('%Y')(date)
                    d3.timeFormat('%b')(date)
            )
            xMinorAxis = d3.axisBottom(@xScale).ticks(d3.timeMonth.every(3))
            #xMinorGridAxis = d3.axisBottom(@xScale).ticks(d3.timeMonth.every(3)).tickSize(-height);
                    
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
                            .attr("fill", 'transparent')

            if @showGuide
                vGuideScale = d3.scaleLinear()
                                .domain([0,d3.max(@grades)])
                                .range([height, 0])
                if @invertY
                    vGuideScale.domain([1,d3.max(@grades)])
                    vGuideScale.range([0,height])

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
                                                                                                                                                                                                                    
            hMinorGuide = svg.append("g")
                                .attr("transform", "translate(#{@margin.left},#{height + @margin.top})")
                                .call(xMinorAxis)

            hMinorGuide.selectAll('path')
                .attr("fill", 'transparent')
                .attr("class", "stroke_2")
            hMinorGuide.selectAll('line')
                .attr('class', 'stroke_2')
                .attr("fill", 'transparent')
            hMinorGuide.selectAll('text')
                .attr("fill", "transparent")


            hGuide = svg.append("g")
                        .attr("transform", "translate(#{@margin.left},#{height + @margin.top})")
                        .call(xAxis)
            hGuide.selectAll('path')
                        .attr("fill", 'transparent')
                        .attr("class", "stroke_3")
            hGuide.selectAll('line')
                        .attr('class', 'stroke_3')
                        .attr("fill", 'transparent')
            hGuide.selectAll('text')
                        .attr("class", "fill_3")


            svg.append("g")
                .attr('transform',"translate(#{@margin.left}, #{@margin.top})")
                .append('path')
                    .attr('d',line(@data))
                    .attr('fill', 'transparent')
                    .classed 'primary-stroke', true
                    .attr('stroke-width', '2')
            userResultPoint = svg.append("g")
                            .attr("transform", "translate(#{@margin.left},#{2 * @margin.top})")
                            .selectAll("g").data(@data)
                            .enter().append("g")
            userResultPoint.append("circle")
                .attr('cx', (d, i) =>  @xScale(@dateFormat(d.date)))
                .attr('cy', (d) => (height-@margin.top) - @yScale(d.score))
                .attr("r", 3)
                .attr("stroke-width", 2)
                .classed "primary-fill primary-stroke", true

            svg.append("g")
                .attr("transform", "translate(#{@margin.left + width/2},#{height + @margin.top + @margin.bottom - 5})")
                .append('text')
                .attr("text-anchor","middle")
                .text(@xLabel)
                .attr("class", "fill_4")
                .attr('font-size', '0.8em')
            svg.append("g")
                .attr("transform", "translate(#{@margin.left/2 - 5},#{height/2  }) rotate(-90)")
                .append('text')
                .attr("text-anchor","middle")
                .text(@yLabel)
                .attr("class", "fill_4")
                .attr('font-size', '0.8em')


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
        xLabel : 
            type : String
            required : true
        yLabel:
            type : String
            required : true
        invertY:
            type : Boolean
            default : false
        color : 
            type : String
            default:'dodgerblue'
        data : 
            type : Array
            required : true
        grades : 
            type : Array
            required : true
        padding : 
            type : Number
            default : 0.5
        showGuide : 
            type : Boolean
            default : false

        showGrid : 
            type : Boolean
            default : true
    watch : 
        data : () ->
            $("##{@name} .time-series").empty()
            @timeSeries()



</script>
