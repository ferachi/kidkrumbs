<template>
    <div id="pageMenu">
        <div class="d-flex align-items-center py-2" :class="justify">
            <div v-for="menu in menus" class="col-auto text-center px-2 menu" :class="[menu.active ? `${activeClasses} active` : '']"
                :key="menu.name" @click="menuClicked(menu.name)">
                <slot :menu="menu" ></slot>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "pageMenuComponent",
    props:{
        menus : {
            type : Array, // array of objects with interface of {title, name, link, active, index}
            required : true
        },
        justification:{
            type : String,
            default : 'between'
        },
        activeClasses : {
            type : String,
            default : 'border-bottom border_white'
        }
    },
    computed : {
        justify(){
            let justifications = {
                'center' : 'justify-content-center',  
                'end' : 'justify-content-end',
                'between' : 'justify-content-between',
                'around' : 'justify-content-around',
            }
            return justifications[this.justification];
        },
    },
    methods : {
        menuClicked(selectedMenu){
            // deactivate all menus
            this.menus.forEach( _menu => _menu.active= false) ;

            // get the selected menu
            let _menu = this.menus.find( _menu => _menu.name == selectedMenu );    

            // activate this menu
            _menu.active = true;

            
            //emit it to parent
            this.$emit('menu-click', _menu);
        }
    }
};
</script>
<style lang="stylus">
#pageMenu
    .menu
        transition border-color 0.3s ease-in-out
        border-color transparent !important

    .active
        border-width 3px !important
</style>
