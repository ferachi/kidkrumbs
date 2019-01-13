<template>
    <div id="subjectOverview">
        <h4 class="font-weight-bold my-3">About</h4>
        <p class="">{{subject.description}}</p>
        <p class="p-3"><span class="color_3">"{{subject.overview}}"</span></p>
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
