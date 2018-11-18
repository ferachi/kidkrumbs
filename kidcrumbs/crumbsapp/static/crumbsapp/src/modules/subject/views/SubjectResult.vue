<template>
    <div id="subjectResult">
        <h5 class="righteous">{{subject.name}} Results</h5>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
export default{
    name : "SubjectResult",
    computed : {
        ...mapGetters('subject', {
            subject : 'getSubject'
        })
    }

}
</script>
<style lang="stylus">

</style>
