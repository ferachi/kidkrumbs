<template>
    <transicion :isLoading="isLoading">
    <div id="child" class="" >
        <page>
        <section slot="header">
            <page-header class="border-bottom border_1 primary-bg" >
                <div slot="pageTitle" class="d-flex align-items-center mb-2">
                    <div class="col-auto px-1">
                        <avatar :image="child.avatar" :alt="child.username" size="large">
                        </avatar>
                    </div>
                    <div class="col px-2">
                        <h4 class="color_white m-0">{{child.last_name}} {{child.first_name}}</h4>
                        <h6 class="m-0 color_white clickable">{{classroom.className}}</h6>
                    </div>
                </div>
                <div slot="pageMenu">
                    <md-menu md-size="medium" :md-offset-x="-130" :md-offset-y="-36" >
                        <md-button md-menu-trigger class="md-icon-button md-dense md-primary">
                            <md-icon class="fas fa-ellipsis-v fa-fw color_white" md-theme="dark"></md-icon>
                        </md-button>
                        <md-menu-content :md-theme="getTheme">
                            <md-menu-item v-for="sm in subMenus" @click="menuClicked(sm)":key="sm.name"><small class="color_4"><i class="fas fa-fw" :class="sm.icon"></i> {{sm.title}}</small></md-menu-item>
                            <md-divider v-if="classrooms.length > 1"></md-divider>
                            <md-menu-item @click="show" v-if="classrooms.length > 1"><small><i class="fas
                                        fa-highlighter fa-fw"></i>change classroom</small></md-menu-item>
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
        </section>
        <section id="childContent" class="p-3 bg_0">
                <transition name="fade-down-up" mode="out-in">
                    <router-view></router-view>
                </transition>
        </section>
        <section>
            <modal ref="modal" :enable-mobile-fullscreen="false" :modal-theme="getTheme" :overlay-theme="getTheme">
            <div>
                <h4 class="font-weight-bold">Classrooms</h4>
                <md-list>
                    <md-list-item v-for="_classroom in classrooms" :key="_classroom.id"
                        @click="changeClassroom(_classroom)">
                        <p class="text-right" :class="{'primary-color' : _classroom.id == classroom.id }">
<span > {{_classroom.className}} </span> <span class="fas
    fa-splotch fa-fw fa-sm" v-if="_classroom.id ==getCurrentClassroom.id" ></span></p>
                    </md-list-item>
                </md-list>
            </div>
            </modal>
        </section>
        <section id="errorFetching">
            <div>
                <h4 class="text-center">{{this.errorMessage}}</h4>
            </div>
        </section>
        </page>
    </div>
    </transicion>
</template>
<script>
let menus = [
    { title : 'Activity', name : 'activity', link : 'childActivities', active : false, index : 0},
    { title : 'Behaviour', name : 'behaviour', link : 'childBehaviours', active : false, index : 1},
    { title : 'Homework', name : 'homework', link : 'childHomework', active : false, index : 2}
]

const subMenus = [
    {
        name : 'profile',
        title : 'profile',
        icon : 'fa-birthday-cake',
        link : 'childProfile',
        index : 0
    },
    {
        name : 'classes',
        title : 'classrooms',
        icon : 'fa-chalkboard-teacher',
        link : 'childClassrooms',
        index : 1
    },
    {
        name : 'subjects',
        title : 'subjects',
        icon : 'fa-book-open',
        link : 'childSubjects',
        index : 2
    },
    {
        name : 'results',
        title : 'results',
        icon : 'fa-chart-bar',
        link : 'childResult',
        index : 3
    },
]
import {mapGetters, mapActions, mapMutations} from 'vuex';
import transicion from '../../../components/transicion.vue';
import pageHeader from '../../../components/pageHeader.vue';
import pageMenu from '../../../components/pageMenu.vue';
import page from '../../../components/page.vue';
import avatar from '../../../components/avatar.vue';
import { SweetModal } from 'sweet-modal-vue';
export default{
    name : "Child",
    created(){
        this.fetchData();
        this.viewMenu();
    },
    components:{
        page,
        transicion,
        pageHeader,
        pageMenu,
        avatar,
        modal : SweetModal,
    },
    data(){
        return {
            child:{},
            date : moment().format("YYYY-MM-DD"),
            isLoading : true,
            error_fetching:false,
            errorMessage : '',
            menus : menus,
            subMenus : subMenus,
        }
    },
    computed:{
        ...mapGetters(['getTheme']),
        ...mapGetters('child', [
            'getCurrentClassroom',
            'getChildClassrooms',
            'getChildClassroom'
        ]),
        ...mapGetters('activity', [
            'getCurrentActivity'
        ]),
        classroom(){
            return !! this.getChildClassroom ? this.getChildClassroom : {};
        },
        classrooms(){
            return !!this.getChildClassrooms ? this.getChildClassrooms : [];
        }
    },
    methods : {
        ...mapActions('child',[
            "fetchChildWithProps"
        ]),
        ...mapActions('group',[
            "fetchGroupHabits"
        ]),
        ...mapMutations("group", [
            "setGroup"
        ]), 
        ...mapMutations("child", [
            "setChildClassroom"
        ]), 
        ...mapActions('activity', {
            fetchActivities : "pullActivities"
        }),
        menuClicked(menu){
            this.$router.push({name : menu.link});
        },
        fetchData(){
            this.fetchChildWithProps(this.$route.params.username).then(child =>{

                // SET GROUP

                // TODO : This will be called on every refresh
                // this means the group will always be reset 
                // to current classroom when the browser is refreshed
                let classroom = _.find(this.classrooms, { id : this.getCurrentClassroom.id})
                this.setGroup(classroom);
                this.setChildClassroom(classroom);


                // SETUP ALL GROUP RELATED MODELS
                let group = this.getCurrentClassroom,
                    groupHabits = this.fetchGroupHabits(group.id),
                    activities = this.fetchActivities(group.id);

                // get the groups activities
                Promise.all([groupHabits, activities]).then( props => {
                    this.child = child;
                    this.isLoading = false;
                })

            }).catch(err => {
                this.isLoading = false;
                this.error_fetching = true;
                this.errorMessage = err.response.data.detail
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
        changeClassroom(classroom){
            this.setChildClassroom(classroom);
            this.setGroup(classroom);
            this.hide();
        },
        show () {
            this.$refs.modal.open(); 
        },
        hide () {
            this.$refs.modal.close(); 
        }
    },
    watch : {
        '$route'(){
            this.viewMenu();
        }
    }
}
</script>
<style lang="stylus">
#child
    #childContent
        min-height 85vh
        padding-bottom 100px !important
        margin-bottom 20px
</style>

