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
                        <md-menu md-size="medium" :md-offset-x="-130" :md-offset-y="-36" >
                            <md-button md-menu-trigger class="md-icon-button md-dense md-primary">
                                <md-icon class="fas fa-ellipsis-v fa-fw color_white" md-theme="dark"></md-icon>
                            </md-button>
                            <md-menu-content :md-theme="getTheme">
                                <md-menu-item @click="$router.push({name:'classroomMember'})">members</md-menu-item>
                                <md-menu-item @click="$router.push({name:'classroomSubject'})">subjects</md-menu-item>
                                <md-menu-item @click="$router.push({name:'classroomResult'})">results</md-menu-item>
                                <md-divider></md-divider>
                                <md-menu-item @click="backToSchools">classrooms</md-menu-item>
                            </md-menu-content>
                        </md-menu>
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
    computed:{
        ...mapGetters([ 'getTheme' ]),
    },
    data(){
        return {
            loading : true,
            classroom : {},
            menus : menus
        }
    },
    methods :{
        ...mapActions('classroom', ['fetchClassroomWithProps']),
        fetchData(){
            this.fetchClassroomWithProps(this.$route.params.id).then(classroom => {
                this.classroom = classroom; 
                this.loading = false;
            });
        },
        viewMenu(){

            this.menus.forEach( menu => menu.active = false );

            // find the parent link/route
            let route = this.$route.matched.find( record => {
                return record.meta.subMenu;
            });
            if(route){
                let activeMenu = this.menus.find(menu => menu.link == route.meta.subMenuName);
                activeMenu.active = true;
            }
        },
        menuClicked(menu){
            this.$router.push({name : menu.link});
        },
        backToSchools(){
            this.$router.push({name : "classroomList" , params : {id : this.classroom.group_base.school}});
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
        min-height 85vh
        padding-bottom 80px !important
    .md-icon.md-theme-default.md-icon-font 
        color white !important
</style>
