<template> 
    <div class="menu-pane pt-4 pb-3" >
        <div class="d-flex align-items-center justify-content-around mb-3">
            <div class="col-auto clickable text-center" v-for="menu in menus" :key="menu.name"
                @click="menuClicked(menu.name)">
                <div v-icon-button.border v-html="menu.icon">
                </div>
                <div>
                    <small>{{menu.title}}</small>
                </div>
            </div>
        </div>
        <h6 class="color_2 m-0 text-right text-uppercase"><small class="color_2">{{title}}</small></h6>
        <hr class="m-0">
    </div>
</template>
<script>
export default {
    name : 'menuPane',
    props:['menus','title'],
    methods :{
        menuClicked(name){
            this.$emit('menu-click', {title:this.title,name:name});
        }
    }
}

</script>
<style lang="stylus">

</style>
