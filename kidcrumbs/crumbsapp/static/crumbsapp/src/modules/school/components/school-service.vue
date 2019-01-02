<template>
    <div id="schoolService" class="p-lg-4 p-xl-5">
        <h5 class="font-weight-bold text-uppercase"> Our services</h5>
        <div class="d-flex flex-wrap py-3">
            <div v-for="service in school.services" class="col-lg-6 col-12 py-2 px-0">
                <h6 class="text-uppercase">{{service.name}}</h6>
                <p><small>{{service.description}}</small></p>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "schoolService",
    props:['school'],
    computed:{
    }
}
</script>
<style lang="stylus">
</style>
