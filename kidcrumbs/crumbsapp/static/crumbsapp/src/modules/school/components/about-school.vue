<template>
    <div id="aboutSchool" class="p-lg-4 p-xl-5">
        <h5 class="font-weight-bold text-uppercase"> About</h5>
        <p><small>{{school.about}}</small></p>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "aboutSchool",
    props:['school'],
    computed:{
    }
}
</script>
<style lang="stylus">
</style>
