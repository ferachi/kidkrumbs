<template>
    <div id="footer" class="d-flex align-items-center justify-content-between">
        <div class="col-auto">
            <p class="m-0 color_3">created by  <span class="fas fa-frog fa-fw primary-color"></span> <span class="color_4">Fercube</span></p>
        </div>
        <div class="col-auto d-flex">
            <div class="col-auto text-center " @click="menuClicked(menu)" v-for="menu in menus" :key="menu.name"
                v-if="!menu.bigDisplay">
                <div class="clickable">
                    <span v-html="menu.icon" :class="{'primary-color':menu.isActive}"></span> <span :class="{'primary-color':menu.isActive}"> {{menu.title}}</span>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapMutations, mapActions} from 'vuex';
export default{
    name : 'KidKrumbs',
    created(){
        this.watchRoute(this.$route);
    },
    data(){
        return {
        }
    },
    computed:{
        ...mapGetters('home',{'menus':'getMenus'}),
    },
    methods : {
        ...mapActions('home', ['activateMenu']),
        ...mapMutations("page", ["setPage"]),
        menuClicked(menu){
            this.$router.push({name : menu.link});
        },
        watchRoute(_route){

            // find the parent link/route
            let route = _route.matched.find( record => {
                return record.meta.krumbMenu
            });

            // activate the menu if it exist
            if(route){
                // set the page
                this.setPage(route.meta.page);

                // activate menu
                let menu = this.menus.find( menu => menu.link == route.meta.page);
                this.activateMenu(menu);
            }
        }
    },
    watch:{
        '$route'(newVal){
            this.watchRoute(newVal);
        }
    }
}
</script>


