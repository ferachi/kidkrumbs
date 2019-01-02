<template>
    <div id="SchoolDetail" >
        <transicion :isLoading="loading">
        <div>
            <section class="school-page intro" >
                <intro :school="school"></intro>
            </section>
            <section class="school-page home">
                <home :school="school"></home>
            </section>
            <section class="school-page about">
                <concept :school="school"></concept>
            </section>
            <section class="school-page contact">
                <contact :school="school"></contact>
            </section>
        </div>
        </transicion>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import transicion from '../../../components/transicion.vue';
import concept from '../components/school-concepts.vue';
import intro from '../components/school-intro.vue';
import home from '../components/school-home.vue';
import contact from '../components/school-contact.vue';
export default{
    name : "SchoolDetail",
    created(){
        this.fetchData();
    },
    data(){
        return {
            loading : true
        }
    },
    components : {
        transicion,
        intro,
        concept,
        home,
        contact
    },
    computed : {
        ...mapGetters('school', {school : 'getSchool'})
    },
    methods : {
        ...mapActions('school', ['fetchSchool']),
        fetchData(){
            this.fetchSchool(this.$route.params.id).then( school => {
                this.loading = false;
            });
        }
    }
}
</script>
<style lang="stylus">
#SchoolDetail
    .school-page
        min-height 85vh
        >div
            padding 10px
</style>
