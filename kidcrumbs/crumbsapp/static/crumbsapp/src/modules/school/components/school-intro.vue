<template>
    <div id="schoolIntro">
    <!-- <div id="schoolIntro" :style="{'background&#45;color':school.color}"> -->
        <div class="d-flex justify-content-center align-items-center flex-wrap">
                <div class="col-lg order-lg-2">
                    <hr>
                    <h3 class="display- text-center text-uppercase m-0 font-weight-bold" >{{school.name}}</h3>
                    <h6 class="m-0 text-center "><small class="color_3" :style="{color:`${school.color} !important`}">{{school.motto}}</small></h6>
                    <hr >
                    <h6 class="m-0 text-center color_3">{{school.contact.city}}, {{school.contact.state}}</h6>
                </div>
                <div class="col-lg-7 order-lg-1">
                    <img class="image-fluid" :src="school.home_image" :alt="school.name">
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "SchoolIntro",
    props:['school'],
}
</script>
<style lang="stylus">
#schoolIntro
    >div
        min-height 85vh
</style>
