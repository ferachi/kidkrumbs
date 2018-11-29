<template>
    <div id="more" class="d-flex justify-content-center">
        <div class="col px-0 d-flex flex-wrap align-items-center ">
            <div class="col-6 col-sm-4 col-lg-3 d-flex flex-wrap justify-content-center p-0 my-1" v-for="menu in menus" :key="menu.name">
                <div class="bg_0 border border_1 menu clickable col-auto col-lg-auto px-0 d-flex justify-content-center
                flex-wrap mx-2" @click="$router.push({name : menu.link})">
                    <div>
                        <div class="bg_aux d-none d-lg-block">
                            <span class="fa-layers fa-10x fa-fw">
                                <span v-for="(icon,index) in menu.icons" :class="addIcon(icon)" :data-fa-transform="transforma(index)"></span>
                            </span>
                        </div>
                        <div class="bg_aux d-lg-none">
                            <span class="fa-layers fa-8x fa-fw">
                                <i v-for="(icon,index) in menu.icons" :class="addIcon(icon)"
                                    :data-fa-transform="transforma(index)"></i>
                            </span>
                        </div>
                        <div class="text-center mt-2">
                            <h6 ><small>{{menu.title}}</small> </h6>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
const menus = [
    {
        name : 'profile',
        title : 'profile',
        icons : ['fa-child', 'fa-heart', 'fa-fingerprint', 'fa-birthday-cake'],
        link : 'childProfile',
        index : 0
    },
    {
        name : 'groups',
        title : 'classes/groups',
        icons : ['fa-user-friends', 'fa-chalkboard', 'fa-chess', 'fa-user-graduate'],
        link : 'childClassrooms',
        index : 1
    },
    {
        name : 'subjects',
        title : 'subjects',
        icons : ['fa-book-open', 'fa-pen-alt', 'fa-glasses', 'fa-table'],
        link : 'childSubjects',
        index : 2
    },
    {
        name : 'results',
        title : 'results',
        icons : ['fa-chart-bar', 'fa-calendar', 'fa-graduation-cap', 'fa-chart-pie'],
        link : 'childResult',
        index : 3
    },

]
export default{
    name : "More",
    created(){
    },
    data(){
        return {
            menus : menus,
        }
    },
    methods:{
        iconic(icon,index){
            return `<i class="fas ${icon} fa-fw" data-fa-transform="${this.transforma(index)}"></i>`;

        },
        addIcon(icon){
            return `fas ${icon} fa-fw`;
        },
        transforma(index){
            let transform = "";
            switch(index){
                    case 0:
                        transform = "shrink-12 up-4 left-4"
                        break;
                    case 1:
                        transform = "shrink-12 up-4 right-4"
                        break;
                    case 2:
                        transform = "shrink-12 down-4 left-4"
                        break;
                    default:
                        transform = "shrink-12 down-4 right-4"
                        break;
            }
            return transform;
        }
    }
}
</script>
<style lang="stylus">
#more
    min-height 60vh
    .menu
        min-height 160px
</style>

