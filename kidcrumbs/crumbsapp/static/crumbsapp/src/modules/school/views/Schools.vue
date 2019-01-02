<template>
    <div id="kidkrumbSchools" class="p-2 p-lg-0 g_aux ">
        <transition :name="anim" mode="out-in">
            <section class="d-flex flex-wrap schools" v-if="isList" key="schoolList">
                <div class="col-lg-3 col-md-6 px-0 " v-for="school in schools" :key="school.id">
                    <school-item :school="school" class="school" @school-click="schoolClicked($event)"></school-item>
                </div>
            </section>
            <section class="search-pane" v-else key="searchPage">
                <search-page></search-page>
            </section>
        </transition>
        <section>
            <modal ref="modal" :enable-mobile-fullscreen="true" :modal-theme="theme" :overlay-theme="theme"
            @close="modalClosed">
                <school-overview :school="school" @view-school="viewSchool($event)"></school-overview>
            </modal>
        </section>
        <section class="search-btn">
            <md-button v-if="isList" class="md-fab md-mini" @click="isList=!isList" key="search">
                <md-icon class="fas fa-search"></md-icon>
            </md-button>
            <md-button v-else class="md-fab md-mini" @click="isList=!isList" key="list">
                <md-icon class="fas fa-th-large"></md-icon>
            </md-button>
        </section>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import schoolItem from '../components/school-list-item.vue';
import searchPage from '../components/search-page.vue';
import schoolOverview from '../components/school-overview.vue';
import { SweetModal } from 'sweet-modal-vue';
export default{
    name : 'kidkrumbSchools',
    computed:{
        ...mapGetters('school', {schools:'getSchools'}),
        ...mapGetters({theme:'getTheme'}),
        icon(){
            return this.isList ?'fas fa-search fa-fw md-small' : 'fas fa-th fa-fw md-small' 
        },
        anim(){
            return this.isList ? 'fade-up' : 'fade-down';
        }
    },
    mounted(){
        setTimeout(() => {
            $(".search-btn").show();
        }, 500);
    },
    data(){
        return{
            isList : true,
            school : {},
            schoolSelected : false 
        }
    },
    components:{
        schoolItem,
        searchPage,
        schoolOverview,
        modal : SweetModal
    },
    methods : {
        ...mapMutations('home' , ['setSchool']),
        schoolClicked(school){
            this.$refs.modal.open();
            this.school = school; 
        },
        viewSchool(school){
            this.schoolSelected = true;
            this.$refs.modal.close();
            this.setSchool(this.school);
            $(".search-btn").hide();
            setTimeout(()=>{
                this.$router.push({name : 'kidkrumbsSchoolDetail', params : {id : this.school.id}});
            },300);
        },
        modalClosed(){
            if(this.schoolSelected){
                this.schoolSelected = false;
            }
        }
    }
}
</script>

<style lang="stylus">
#kidkrumbSchools
    position relative
    top 0
    left 0
    min-height 85vh
    .search-btn
        display none
        position fixed
        top 60px
        right 10px
//   .schools:hover
//     .school
//        opacity : 0.8
//        transition all 0.4s ease-in-out
//        &:hover
//          //transform translate(2px,2px)
//          opacity 1
//          cursor pointer
</style>
