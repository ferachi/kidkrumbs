<template>
    <div id="kidkrumbshome" class="px-3">
        <div class=" home d-flex flex-wrap align-items-center justify-content-center">
            <div class="col-12 px-0 text-center">
                <h1 id="brand" class="display-2 brand primary-color m-0 font-weight-bold" >Kidkrumbs</h1>
                <p class="color_3 m-0">School hub for all</p>
            </div>
            <div class="px-0" style="height:45vh">
                <section class="schools-slide text-center py-3">
                    <schools-slide :index='index' :schools="schools" class="d-inline-block"></schools-slide>
                </section>
                <section class="school-preview text-center py-4">
                    <school-preview :school="school"></school-preview>
                </section>
                <section class="control-pane py-4">
                    <control :schools="schools" @index-change="indexChanged($event)"> </control>
                </section>

            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import schoolPreview from '../components/school-preview.vue';
import schoolsSlide from '../components/schools-slide.vue';
import control from '../components/schools-slide-control.vue';
export default{
    name : 'Home',
    created(){
    },
    components:{
        schoolPreview,
        schoolsSlide,
        control
    },
    data(){
        return {
            index : 0
        }
    },
    computed:{
        ...mapGetters('school', ['getSchools']),
        ...mapGetters('home', {school:'getSchool'}),
        ...mapGetters({device:'getDevice'}),
        isLarge(){
            return this.device.screen == 'lg' || this.device.screen == 'xl';
        },
        school(){
            let school = this.schools[this.index];
            return school;
        },
        schools(){
            let sortedSchools = _.sortBy(this.getSchools, 'name');
            return sortedSchools 
        }
    },
    methods : {
        ...mapMutations('home', ['setSchool']),
        indexChanged(index){
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
        height 85vh
        overflow-y auto
        #controlPane
            position absolute
            top 0
            left 0
            background rgba(240,240,240,0.1)
            width 30vw

</style>
