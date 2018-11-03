<template>
    <div class="slideMenu d-inline-block">
        <div class="d-flex align-items-center" :class="{'flex-column':direction=='top' || direction=='bottom',
        'flex-row':direction=='left' || direction=='right'}">
            <div @click="toggleMenu" class="menu-icon col-auto p-1"
                                     :class="{'order-0':direction=='bottom'||direction=='right','order-1':direction=='top'|| direction=='left'}">
                <div class="text-center">
                    <slot>
                    <div v-if="layout=='horizontal'">
                        <i class="fas fa-ellipsis-h fa-fw"></i>
                    </div>
                    <div v-else>
                        <i class="fas fa-ellipsis-v fa-fw"></i>
                    </div>
                    </slot>
                </div>
            </div>
            <div class="menus col-auto px-0 ">
                <div v-if="canShowMenu && menuOpen" class="d-flex slide-menu-pane border border_2 rounded p-1 text-center "
                    :class="[layout=='vertical' ? 'flex-column' : 'flex-row', 
                    {'leftright left': direction=='left','leftright right': direction=='right',
                    'topbottom top':direction == 'top', 'topbottom bottom': direction == 'bottom'}] ">
                    <div @click="menuClicked(menu.name)" class="col-auto py-1 px-2 s-menu color_5" 
                                                         v-for="menu in menus" @mouseover="hoverMenu=menu.name"
                                                         @mouseout="hoverMenu=''" :class="{'bg_1':hoverMenu == menu.name}" >
                                                         <i :class="menu.icon"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "slideMenu",
    props:{
        menus:{
            type : Array, // [{name, icon}]
            required:true
        },
        layout:{
            type : String, 
            default : 'vertical' // 'horizontal' | 'vertical'
        }, 
        direction:{
            type : String,
            default: 'right' //'top', 'bottom', 'left', 'right'
        },
        canShowMenu:{
            type : Boolean,
            default : false
        }
    },
    data(){
        return {
            menuOpen : false,
            hoverMenu : ''
        }
    }, 
    methods : {
        toggleMenu(){
            this.menuOpen = !this.menuOpen;
        }, 
        menuClicked(item){
            this.menuOpen = false;
            this.$emit('menu-click', item);
        }
    },
    watch : {
        canShowMenu(val){
            if(!val)
                this.menuOpen = val;
        }
    }
};
</script>
<style lang="stylus" scoped>
.slideMenu
    .menus
        position relative
        z-index 100
        top 0
        .slide-menu-pane
            position absolute
            z-index 100
        .slide-menu-pane.leftright
            top 50%
            transform : translate(0%,-50%)
        .slide-menu-pane.topbottom
            left 50%
            transform : translate(-50%,0%)
        .slide-menu-pane.right
            left 0
        .slide-menu-pane.left
            right 0
        .slide-menu-pane.bottom
            top 0
        .slide-menu-pane.top
            bottom 0

</style>

