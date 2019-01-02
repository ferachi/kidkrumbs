<template>
    <div id="schoolRequirement" class="p-lg-4 p-xl-5">
        <h5 class="font-weight-bold text-uppercase"> Our Requirements</h5>
        <div class="d-flex flex-wrap py-3">
            <div v-for="requirement in school.requirements" class="col-lg-5 col-12 py-2 px-0">
                <h6 class="text-uppercase">{{requirement.title}}</h6>
                <p><small>{{requirement.description}}</small></p>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "schoolRequirement",
    props:['school'],
    computed:{
    }
}
</script>
<style lang="stylus">
</style>
