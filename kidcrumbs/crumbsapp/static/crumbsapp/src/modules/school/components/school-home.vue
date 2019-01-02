<template>
    <div id="schoolHome" class="bg_aux">
        <div class="d-flex justify-content-center align-items-center">
            <div class="col-lg-10 d-flex flex-wrap align-items-center">
                <div class="col-lg-5 col-12">
                    <div>
                        <p class="color_3 m-0"><small class="color_3">ABOUT</small></p>
                        <h4 class="font-weight-bold text-uppercase m-0" >Who we are</h4>
                    </div>
                    <div>
                        <p>{{school.description}}</p>
                    </div>

                </div>
                <div class="col text-center">
                    <img class="image-fluid" :src="school.about_image" :alt="school.name">
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "SchoolHome",
    props:['school'],
}
</script>
<style lang="stylus">
#schoolHome
    >div
        min-height 85vh
</style>
