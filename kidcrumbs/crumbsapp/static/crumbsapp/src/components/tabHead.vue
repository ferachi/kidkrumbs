<template>
    <div class="tab-head">
        <div class="d-flex align-items-center" :class="justify">
            <div v-for="tab in tabs" class="col-auto" @click="tabClicked(tab.name)" :key="tab.name">
                <slot name="tab" :tab="tab" >
                <p class="text-center clickable"><small class="color_3" :class="{'primary-color':tab.isActive}">{{tab.name}}</small></p>
                </slot>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "",
    created(){
        this.tabs = this.tabTitles.map(title => ({ name : title, isActive:false}));
        this.tabs[0].isActive = true;
    },
    props:{
        tabTitles : {
            type : Array,
            required : true
        },
        justify:{
            type:String,
            default : "justify-content-center"
        }
    },
    data(){
        return {
            tabs : []
        }
    },
    methods : {
        tabClicked(tab){
            this.tabs.forEach(_tab => _tab.isActive = false);
            let _tab = this.tabs.find(_tab => _tab.name == tab);
            _tab.isActive = true;
            this.$emit('tab-click', tab);
        }
    }
};
</script>
<style lang="stylus">
</style>
