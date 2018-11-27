<template>
    <div id="dthree">
        <grade-bar :width="300" :height="10" :score="score" title="scores" :grading="grading">{{score}}</grade-bar>
        <grade-bar :width="250" :height="8" :score="90" title="average" :grading="grading"> 90</grade-bar>
        <h3>bar chart</h3>
        <div class="bg_0 px-5 d-inline-block">
            <bar-chart title="results" :width="600" :height="400" :grading="grading" :data="barData"> </bar-chart>
        </div>
        <div class="bg_0 px-5 d-inline-block">
            <pie-chart title="perc" :width="400" :height="400" :grading="grading" :data="pieData"> </pie-chart>
        </div>
    </div>
</template>

<script lang="coffee">
import joinData from '../components/d3_join.vue'
import scales from '../components/scales.vue'
import gradeBar from '../components/grade_bar.vue'
import barChart from '../components/bar_chart.vue'
import pieChart from '../components/pie_chart.vue'
grading = [
        minScore : 70
        maxScore : 100
        color : "darkgreen"
        grade : 'A'
    ,
        minScore : 60
        maxScore : 69
        color : "forestgreen"
        grade : 'B'
    ,
        minScore : 50
        maxScore : 59
        color : "orange"
        grade : 'C'
    ,
        minScore : 45
        maxScore : 49
        color : "orangered"
        grade : 'D'
    ,
        minScore : 40
        maxScore : 45
        color : "red"
        grade : 'E'
    ,
        minScore : 0
        maxScore : 39
        color : "maroon"
        grade : 'F'
]
export default
    name : "DThree"
    components :
        joinData : joinData
        scales : scales
        gradeBar : gradeBar
        barChart : barChart
        pieChart : pieChart
    data:() ->
        score : 50
        grading : grading
        barData :[ 
            label : "English"
            score : 45
        ,
            label : "Mathematics"
            score : 67
        ,
            label : "Physics"
            score : 55
        ,
            label : "Agriculture"
            score : 67
        ,
            label : "Social Studies"
            score : 80
        ,
            label : "Inter science"
            score : 30
        ,
            label : "Intro Tech"
            score : 50
        ]
        pieData : [
            label : "A"
            percentage : 45
            color : "darkgreen"
        ,
            label : "B"
            percentage : 25
            color : "forestgreen"
        ,
            label : "C"
            percentage : 10
            color : "orange"
        ,
            label : "D"
            percentage : 20
            color : "red"
        ]



</script>
<style lang="stylus">

</style>
