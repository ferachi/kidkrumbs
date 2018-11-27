<template>
    <div id="childResult" >
        {{getTotalAssessmentScores}} <br>
        {{getTotalScores}} <br>

    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : "ChildResult",
    computed : {
        ...mapGetters('child',['getChildResults']),
        ...mapGetters('result',[
            'getTotalAssessmentScores',
            'getTotalScores',
            'getMinScore',
            'getMaxScore',
        ])
    },
    components:{
    }
}
</script>
<style lang="stylus">
</style>

