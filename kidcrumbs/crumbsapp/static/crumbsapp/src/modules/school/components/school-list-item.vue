<template>
    <div class="school-list-item d-flex align-items-center bg_0 border border_aux p-2"
    @click="$emit('school-click',school)">
        <div class="text-center col-12 px-0">
            <div class="" >
                <div class="d-flex align-items-center text-left">
                    <div class="col-auto px-1">
                        <div class="">
                            <avatar :image="school.logo" size="large"></avatar>
                        </div>
                    </div>
                    <div class="col px-0">
                        <h5 class="font-weight-bold m-0 text-capitalize" :style="{color : `${school.color} !important`}">{{school.name}}</h5>
                        <p class="m-0"><small class="color_3">{{school.motto}}</small></p>
                    </div>
                </div>
            </div>
            <div class="mt-4">
                <div class="px-5">
                    <hr class="mt-1" />
                </div>
                <div>
                    <p class="righteous">{{school.brief_description}}</p>
                </div>
                <div class="px-4" >
                    <hr class=" mt-1"  />
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import avatar from '../../../components/avatar.vue';
export default{
    name : 'SchoolListItem',
    props : ['school'],
    computed : {
    },
    components : {
        avatar
    }
}
</script>
<style lang='stylus'>
.school-list-item
    height 350px
    //margin 1px
    cursor pointer
</style>

