<template>
    <div id="resultSummaryBar" class="">
        <div class="d-flex justify-content-center">
            <div class="col-auto text-center">
                <h1 class="display-3 m-0 font-weight-bold">
                    {{grade}}    
                </h1>
                <p class="m-0 color_3">Total Average: {{average}} %</p>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : "resultSummaryBar",
    computed : {
        ...mapGetters('result', {
            average:'getTotalAverageScore',
        }),
        ...mapGetters('grade', [ 'getGrader']),
        grade(){
            return this.getGrader.gradeScale(this.average);
        }
    },
}
</script>
<style lang="stylus">
</style>

