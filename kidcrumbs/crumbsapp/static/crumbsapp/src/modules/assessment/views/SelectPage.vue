<template>
    <div id="selectPage" class="d-flex flex-wrap align-items-center justify-content-center" >
        <div class="col-lg-auto col-12  px-1">
            <div class="select-btn mx-auto d-flex align-items-center bg_0 justify-content-center" @click="viewResults">
                <div class="col-auto">
                    <h1 class="">
                        <span class="fas fa-chart-line fa-fw fa-2x"></span>
                    </h1>
                    <h6>View Results</h6>
                </div>
            </div>
        </div>
        <div class="col-lg-auto col-12 px-1">
            <div class="select-btn mx-auto d-flex align-items-center bg_0 justify-content-center" @click="viewAssessments">
                <div class="col-auto">
                    <h1 class="">
                        <span class="fas fa-chart-pie fa-fw fa-2x"></span>
                    </h1>
                    <h6>Edit Results</h6>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : 'selectPage',
    computed : {
    },
    components : {
    },
    methods:{
        viewResults(){
            this.$router.push({name : 'results'});
        },
        viewAssessments(){
            this.$router.push({name : 'assessmentDetail'});
        }
    }
}
</script>
<style lang='stylus'>
#selectPage
    min-height 85vh
    .select-btn
        width 200px
        height @width
        cursor pointer
</style>

