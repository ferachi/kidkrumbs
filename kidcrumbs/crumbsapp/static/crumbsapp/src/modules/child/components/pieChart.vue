<template>
    <div id="pie" class=" d-flex justify-content-center">
        <div class="col-auto px-0">
            <pie title="pieSum" :width="250" :height="250" :data="pieData" class="col-auto px-0"> </pie>
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
        pieData(){
            return _.map(this.getGradeFrequency, grade => {
                let {grade : label, percentage, color} = grade;
                return {label, percentage, color}
            })
        }
    },
}
</script>
<style lang="stylus">
</style>

