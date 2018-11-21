<template>
    <div>
        <div class="dropdown">
             <a class="dropdown-toggle px-2" id="dropdownMenu" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <slot name="menuBtn"> + </slot>
             </a>
             <div class="dropdown-menu" aria-labelledby="dropdownMenu" :class="{'dropdown-menu-right':right}">
             <slot>
                <button class="dropdown-item" type="button">action 1</button>
                <button class="dropdown-item" type="button">action 2</button>
                <button class="dropdown-item" type="button">action 3</button>
            </slot>
            </div>
        </div>
    </div>
</template>
<script>

export default{
    name:"DropDownMenuComp",
    props:{
        right : {
            type : Boolean,
            default : false
        }
    }
    
}
</script>
<style lang="stylus" scoped>

</style>
