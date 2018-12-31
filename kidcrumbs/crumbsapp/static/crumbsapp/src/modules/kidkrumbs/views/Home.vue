<template>
    <div id="kidkrumbshome">
        <transicion :isLoading='loading'>
            <div class="home" style="position:relative">
                <section class="h-100">
                    <school-display :school="school"></school-display>
                </section>
                <section class="d-lg-none fixed-bottom bg_0" v-if="!isLarge" >
                    <school-player :schools="getSchools" class="" @school-change="schoolChangedMobile($event)"></school-player>
                </section>
                <section id="controlPane" class="h-100 d-none d-lg-block " v-else>
                    <div class="h-100 d-flex align-items-center justify-content-center">
                        <school-player :schools="getSchools" class="" @school-change="schoolChanged($event)"></school-player>
                    </div>
                </section>
            </div>
        </transicion>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import transicion from '../../../components/transicion.vue';
import schoolDisplay from '../components/school-display.vue';
import schoolPlayer from '../components/school-player.vue';
export default{
    name : 'Home',
    created(){
        this.fetchData();
    },
    data(){
        return {
            loading : true
        }
    },
    components:{
        transicion,
        schoolDisplay,
        schoolPlayer,

    },
    computed:{
        ...mapGetters('school', ['getSchools']),
        ...mapGetters('home', {school:'getSchool'}),
        ...mapGetters({device:'getDevice'}),
        isLarge(){
            return this.device.screen == 'lg' || this.device.screen == 'xl';
        }
    },
    methods : {
        ...mapActions('school', ['fetchSchools']),
        ...mapMutations('home', ['setSchool']),
        fetchData(){
            this.fetchSchools().then(schools => {
                this.loading = false;
            })
        },
        schoolChanged(school){
            this.setSchool(school);
        },
        schoolChangedMobile(school){
            this.setSchool(school);
        }
    }
}
</script>

<style lang="stylus">
#kidkrumbshome
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
