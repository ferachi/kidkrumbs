<template>
    <div id="aListItem" class="my-1"@click="alistItemClicked(item)">
        <div class="bg_0 px-0"  :class="{'primary-border border-bottom':isActive}" >
            <div class="pt-3 pb-1">
                <div class="d-flex align-items-center">
                    <div class="col px-1">
                        <slot :item="item"></slot>
                    </div>
                    <div class="col-auto item-menu px-0" v-if="showMenu">
                        <div @click="displayMenu">
                            <slot name="menu" :menus="menus" :id="id" :active="isActive">
                            </slot>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "AListItem",
    data(){
        return {
            isActive : false
        }
    },
    props : {
        id : {
            type : String,
            required : true
        },
        selected:{
            type : Boolean,
            default : false
        },
        showMenu : {
            type : Boolean,
            default : false
        },
        menus : {
            type : Array, // [{name,icon}]
            required:true
        },
        item:{
            type : Object,
            required : true
        }
    },
    methods:{
        displayMenu(){
            this.menuOn = true;
        },
        alistItemClicked(item){
            this.$emit('alist-click',item);
        }
    }
};
</script>
<style lang="stylus" scoped>
#aListItem
    .item-menu
        > div
            position relative
            top 0px
            left 0px
            .a-list-menu
                position absolute
                top 0px
                right 0px
</style>
