<template>
    <div id="ClassroomDetail" class="">
        <transicion :isLoading="loading">
        <page>
            <div slot="header">
                <page-header class="border-bottom " :style="{'background':`${classroom.color} !important`}">
                    <div slot="pageTitle" class="d-flex align-items-center">
                        <div class="col-auto px-1">
                            <p class="m-0 color_white"> <i class="fas fa-chalkboard-teacher fa-fw fa-lg"></i></p>
                        </div>
                        <div class="col px-2">
                            <h4 class="m-0 color_white"><span class="font-weight-bold">{{classroom.className}}</span></h4>
                        </div>
                    </div>
                    <div slot="pageMenu">
                        <p class="m-0 color_white d-inline-block"> <i class="fas fa-ellipsis-v fa-fw fa-lg"></i></p>
                        <!-- <div class="py&#45;1"> -->
                        <!--     <md&#45;avatar class="md&#45;avatar&#45;icon"> <md&#45;icon class="fas fa&#45;glasses"></md&#45;icon></md&#45;avatar> -->
                        <!-- </div> -->
                    </div>
                    <div class="menu d-flex justify-content-center">
                        <div class="col-xl-6 col-lg-8 px-0 ">
                            <page-menu :menus="menus" :activeClasses="''" @menu-click="menuClicked($event)">
                                <div slot-scope="{menu}" class="clickable" :style="{'border-bottom': menu.active ? `3px solid white !important` : 'transparent'}">
                                    <p class="mb-1 color_white">{{menu.title}}</p>
                                </div>
                            </page-menu> 
                        </div>
                    </div>
                </page-header>
            </div>
            <section class="p-3 bg_0 detail-content">
                <transition name="fade-down-up" mode="out-in">
                    <router-view></router-view>
                </transition>
            </section>
        </page>
        </transicion>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import transicion from '../../../components/transicion.vue';
import pageMenu from '../../../components/pageMenu.vue';
import pageHeader from '../../../components/pageHeader.vue';
import page from '../../../components/page.vue';

let menus = [
    { title : 'profile', name : 'profile', link : 'classroomDetail', active : false, index : 0},
    { title : 'activity', name : 'activities', link : 'classroomActivity', active : false, index : 1},
    { title : 'behaviour', name : 'behaviour', link : 'classroomBehaviour', active : false, index : 2},
    { title : 'homework', name : 'homework', link : 'classroomHomework', active : false, index : 3}
]
export default {
    name: "ClassroomDetail",
    created(){
        this.fetchData();
        this.viewMenu();
    },
    components : {
        transicion,
        page,
        pageHeader,
        pageMenu
    },
    data(){
        return {
            loading : true,
            classroom : {},
            menus : menus
        }
    },
    methods :{
        ...mapActions('classroom', ['fetchClassroom']),
        fetchData(){
            this.fetchClassroom(this.$route.params.id).then(classroom => {
                this.classroom = classroom; 
                this.loading = false;
            });
        },
        viewMenu(){
            let activeMenu = this.menus.find(menu => menu.link == this.$route.name);
            activeMenu.active = true;
        },
        menuClicked(menu){
            this.$router.push({name : menu.link});
        }
    },
    watch:{
        '$route'(){
            this.viewMenu();
        }
    }
};
</script>
<style lang="stylus">
#ClassroomDetail
    .detail-content
        min-height 80vh
</style>
