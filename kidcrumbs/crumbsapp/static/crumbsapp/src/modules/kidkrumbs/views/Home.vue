<template>
    <div id="kidkrumbshome" class="px-3">
        <div class=" home">
            <div class="pt-2 text-center">
            <h1 class="d-none d-lg-block display-4 m-0 font-weight-bold primary-color text-uppercase">KidCrumbs</h1>
            <h3 class="d-lg-none m-0 font-weight-bold primary-color text-uppercase">KidCrumbs</h3>
            <p class="color_3 m-0" style="margin-top : -5px !important;"> <small class="color_3">One stop school hub</small></p>
            </div>
            <div class="d-flex flex-wrap align-items-center h-100">
                <section class="col-lg col-12 order-lg-2 school-display">
                    <display :school="school" :index="index"></display>
                </section>
                <div class="col-auto order-lg-1">
                    <p class="m-0 clickable d-none d-lg-block" @click="decreaseIndex" :style="{color : `${color} !important`}"><i class="fas fa-3x fa-chevron-left"></i></p>
                </div>
                <div class="col-auto order-lg-3 d-flex">
                    <p class="m-0 clickable d-none d-lg-block" @click="increaseIndex"><i class="fas fa-3x fa-chevron-right" :style="{color : `${color} !important`}"></i></p>
                </div>
            </div>
            <div class="mt-4 mt-lg-0">
                <schools-carousel :index='index' :schools="schools" :direction="direction" @click-index="setIndex($event)"></schools-carousel>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import display from '../components/school-display.vue';
import schoolsCarousel from '../components/schools-carousel.vue';
export default{
    name : 'Home',
    created(){
    },
    components:{
        display,
        schoolsCarousel,
    },
    data(){
        return {
            index : 0,
            direction : 'right'
        }
    },
    computed:{
        ...mapGetters('school', {schools:'getSchools'}),
        ...mapGetters('home', {school:'getSchool'}),
        ...mapGetters({color:'getColor'}),
        ...mapGetters({device:'getDevice'}),
        isLarge(){
            return this.device.screen == 'lg' || this.device.screen == 'xl';
        },
        school(){
            let school = this.schools[this.index];
            return school;
        },
    },
    methods : {
        ...mapMutations('home', ['setSchool']),
        indexChanged(index){
            this.index = index;
        },
        increaseIndex(){
            this.index = this.index == this.schools.length - 1 ?  0 : this.index + 1;
            this.direction = 'right';
        },
        decreaseIndex(){
            this.index = this.index == 0 ?  this.schools.length - 1 : this.index - 1;
            this.direction = 'left';
        },
        setIndex(index){
            this.index = index;
        }
    }
}
</script>

<style lang="stylus">
#kidkrumbshome
    h1#brand.brand
        font-family 'Aclonica', 'Dosis','Muli','Roboto',Arial,sans-serif !important
    .home
        height 65vh

</style>
