<template>
    <div id="subjectOverview">
        <h5 class="righteous">{{subject.name}}</h5>
        <p>{{subject.description}}</p>
    </div>
</template>
<script>
import {mapGetters} from 'vuex'
export default{

    name : "SubjectOverview",
    components:{
    },
    computed:{
        ...mapGetters('subject', {
            subject: 'getSubject'
        })
    }
}
</script>
<style lang="stylus">

</style>
