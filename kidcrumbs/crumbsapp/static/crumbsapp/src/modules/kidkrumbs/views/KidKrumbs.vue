<template>
    <div id="kidkrumbs">
        <transicion :isLoading='loading'>
            <section class="site-header">
                <site-header></site-header>
            </section>
            <section class="site-body bg_0">
                <transition name="fade" mode="out-in">
                <router-view></router-view>
                </transition>
            </section>
            <section class="bg_0 site-footer py-3 d-none d-lg-block">
                <footer-base></footer-base>
            </section>
        </transicion>
    </div>
</template>
<script>
import siteHeader from '../components/site-header.vue';
import footerBase from '../components/footer.vue';
import transicion from '../../../components/transicion.vue';
import { mapActions} from 'vuex';
export default{
    name : 'KidKrumbs',
    created(){
        this.fetchData();
    },
    data(){
        return {
            loading : true
        }
    },
    components : {
        siteHeader,
        transicion,
        footerBase
    },
    methods:{
        ...mapActions('school', ['fetchSchools']),
        fetchData(){
            this.fetchSchools().then(schools => {
                this.loading = false;
            })
        },
    }
}
</script>
<style lang="stylus">
#kidkrumbs
    min-height 100vh
    .site-body
        height 85vh
        width 100vw
        overflow-y auto
        overflow-x hidden
    .site-footer
        height 8vh
</style>


