<template>
    <div id="pie" class="">
        <div class="px-0">
            <pie title="pieSum" :width="350" :height="350" :data="pieData" :labels="labels"> </pie>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import pie from '../../../components/pie_chart.vue'
export default{
    name : "pieChart",
    created(){
    },
    components : {
        pie
    },
    computed : {
        ...mapGetters('result', [ 'getGradeFrequency']),
        ...mapGetters('grade', [ 'getGrades']),
        pieData(){
            return _.map(this.getGradeFrequency, grade => {
                let {grade : label, percentage, color} = grade;
                return {label, percentage, color}
            })
        },
        labels(){
            return _.map( this.getGrades, grade => {
                let {grade : label, color} = grade;
                return {label, color}
            })
        },
    },
}
</script>
<style lang="stylus">
#pie
    max-width 98vw
    overflow-x auto
</style>

