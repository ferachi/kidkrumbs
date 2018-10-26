<template>
    <div id="appMenu" class="bg_0">
        <!-- Mobile devices -->
        <div class="mobile d-lg-none">
            <div class="d-flex flex-wrap align-items-center">
                <div class="col text-center" v-for="menu in menus">
                    <menuItem :menuItem="menu"> </menuItem>
                </div>
            </div>
        </div>

        <!-- tabs and cpus  -->
        <div class="bigscreens d-none d-lg-block">
            <div class="py-3">
                <div class="text-center" v-for="menu in menus">
                    <menuItem :menuItem="menu" class="mb-3"> </menuItem>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapGetters, mapActions} from "vuex";
import menuItem from "./menuItem.vue";
export default{
    name : "AppMenu",
    created(){
        this.watchRoute(this.$route);
    },
    computed : {
        ...mapGetters("menu", {
            menus : "getMenus"
        }),
    },
    methods:{
        ...mapActions("menu",[
            "activateMenu"
        ]),
        watchRoute(_route){
            let route = _route.matched.find( record => {
                return record.meta.menuPage
            });
            if(route){
                let menu = this.menus.find( menu => menu.link == route.name)
                if(menu) this.activateMenu(menu);
            }
        }
    },
    components:{
        menuItem,
    },
    watch : {
        '$route'(newRoute,oldRoute){
            this.watchRoute(newRoute);
        }
    }

}
</script>
<style lang="stylus" scoped>
#appMenu 
    .bigscreens
        min-height 100vh
</style>
