<template> 
    <div id="menu">
        <section >
            <themer class="py-2"></themer>    
            <hr class="my-1">
        </section>
        <section class="d-flex justify-content-center">
            <div class="col-xl-7 col-lg-10 text-center pt-3">
                <div v-for="(menu,title) in menus" :key="title">
                    <menupane :menus="menu" :title="title" @menu-click="menuClicked($event)" ></menupane>
                </div>
            </div>
        </section>
        <section>
            <modal @close="modalClosing" ref="modal" :enable-mobile-fullscreen="true" :modal-theme="getTheme" :overlay-theme="getTheme" >
                <transition name="fade-right" mode="out-in">
                    <component :is="view"></component>
                </transition>
            </modal>
        </section>
    </div>
</template>
<script>
import themer from './themer.vue';
import menupane from './menu-pane.vue';
import aboutus from './about-us-view.vue';
import feedback from './feedback-view.vue';
import { SweetModal } from 'sweet-modal-vue';
import {mapGetters, mapActions} from 'vuex';
const moreMenus = { 
        school : [
            {
                name : 'kidkrumbs',
                title : 'kidkrumbs',
                icon : ` <span class="fa-layers fa-fw fa-lg" > <i class="fas fa-female" data-fa-transform="shrink-2
                right-3"></i> <i class="fas fa-male" data-fa-transform="shrink-2 left-3"></i> </span>`,
                link : 'app',
            },
            {
                name : 'schools',
                title : 'schools',
                icon:`<span class="fas fa-school fa-fw fa-lg"></span>`,
                link : ''
            }
        ],
        administration : [
            {
                name : 'admin',
                title : 'admin',
                icon:`<span class="fas fa-graduation-cap fa-fw fa-lg"></span`,
                link : ''
            },
            {
                name : 'results',
                title : 'results',
                icon:`<span class="fas fa-chart-pie fa-fw fa-lg"></span`,
                link : ''
            },
            {
                name : 'students',
                title : 'students',
                icon:`<span class="fas fa-user-graduate fa-fw fa-lg"></span`,
                link : ''
            },

        ],
        kidkrumbs : [
            {
                name : 'aboutus',
                title : 'about us',
                icon:`<span class="fas fa-lightbulb fa-fw fa-lg"></span`,
                link : ''
            },
            {
                name : 'feedback',
                title : 'feedback',
                icon:`<span class="fas fa-paper-plane fa-fw fa-lg"></span`,
                link : ''
            },
        ],
        logout : [
            {
                name : 'logout',
                title : 'logout',
                icon:`<span class="fas fa-times fa-fw fa-lg"></span`,
                link : ''
            },
        ]
}
export default {
    name : 'MoreMenu',
    computed :{
        ...mapGetters(['getTheme']),
    },
    components:{
        themer,
        menupane,
        modal : SweetModal,
        aboutus,
        feedback
    },
    data(){
        return {
            menus:moreMenus,
            view:'',
        }
    },
    methods :{
        ...mapActions('auth',['logout']),
        show (){
            this.$refs.modal.open();
        },
        hide (){
            this.$refs.modal.close();
        },
        modalClosing (){
            this.view = '';
        },
        menuClicked(_menu){
            let menus = _.find(this.menus, (list,_title) => _title == _menu.title),
                menu = _.find(menus, {name : _menu.name});
            switch(menu.name){
                case 'kidkrumbs':
                    this.$router.push({name : menu.link});
                    break;
                case 'schools':
                    break;
                case 'admin':
                    break;
                case 'results':
                    this.$router.push({name : 'results'})
                    break;
                case 'students':
                    break;
                case 'aboutus':
                    this.view = menu.name;
                    this.show();
                    break;
                case 'feedback':
                    this.view = menu.name;
                    this.show();
                    break;
                case 'logout':
                    this.logout().then( val => {
                        this.$router.push({name : 'notAllowed'})
                    });
                    break;
            }
        }
    }
}
</script>
<style lang="stylus">
</style>
