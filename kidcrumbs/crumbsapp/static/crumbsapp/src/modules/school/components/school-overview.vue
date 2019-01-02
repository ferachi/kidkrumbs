<template>
    <div id="schoolOverview" >
        <div class="d-flex p-2 flex-wrap">
            <div class="col-12 col-lg px-0 text-left">
                <h4 class="m-0 text-capitalize" :style="{color : `${school.color} !important`}">{{school.name}}</h4>
                <p class="m-0"><small class="color_3">{{school.contact.city}}, {{school.contact.state}}</small></p>
                <hr class="mb-0">
                <p class="m-0"><small class="color_3">{{school.motto}}</small></p>
            </div>
            <div class="col-12 col-lg">
                <img :src="school.thumb_image" class="img-fluid" :alt="school.name">
            </div>
        </div>
        <hr>
        <div class="text-left">
            <h5 class="font-weight-bold color_5 m-0">About us</h5>
            <p class="m-0"><small>{{school.description}}</small></p>
        </div>
        <hr>
        <div class="d-flex text-left align-items-center">
            <div class="col px-0">
                <p class="m-0"><small class="color_3"><i class="fas fa-mobile fa-fw"></i> : <span class="color_5">{{school.contact.phone_number}}</span> </small></p>
                <p class="m-0"><small class="color_3"><i class="fas fa-at fa-fw"></i> : <span class="color_5">{{school.contact.email}}</span></small></p>
            </div>
            <div class="col-auto px-0">
                <md-button class="md-primary md-raised" :style="{'background-color' : `${school.color} !important`}"
                    @click="viewSchool">View School</md-button>
            </div>
        </div>
    </div>
</template>
<script>
import avatar from '../../../components/avatar.vue';
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : 'SchoolListItem',
    props : ['school'],
    computed : {
    },
    components : {
        avatar
    },
    methods:{
        viewSchool(){
            this.$emit('view-school', this.school);
        }
    }
}
</script>
<style lang='stylus'>
</style>

