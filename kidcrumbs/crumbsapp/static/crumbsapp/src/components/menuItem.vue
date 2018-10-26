<template>
    <div id="appMenuItem" class="text-center py-1 p-md-2" v-if="menuItem.display" @click="menuItemClick(menuItem)">
        <p class="m-0" :class="{'primary-color':menuItem.isActive}" ><i :class="menuItem.icon"></i></p>
       <p class="m-0" style="margin-top:-5px !important"> <small :class="{'primary-color':menuItem.isActive}" style="font-size:0.7em" >{{menuItem.title}} </small></p>
    </div>
</template>

<script>
import {mapGetters, mapActions} from "vuex";
import MenuItem from "../component_models/menu";

export default{
    name : "AppMenuItem",
    props:{
        menuItem : MenuItem
    },
    methods:{
        ...mapActions("menu",[
            "activateMenu"
        ]),
        menuItemClick(menu){
            this.activateMenu(menu);
            this.$router.push({name:menu.link});
        }
    }
}
</script>

<style lang="stylus">
#appMenuItem
    cursor pointer
</style>
