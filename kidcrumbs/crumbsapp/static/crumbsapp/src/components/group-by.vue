<template>
    <div class="group-by">
        <div class="group" v-for="(items,key) in listItems" :key="key">
            <slot :id="key" :values="items">
                {{key}}
            </slot>
       </div>
    </div>
</template>
<script>
export default{
    name : "GroupBy",
    props:{
        items : {
            type : Array,
            required: true
        },
        field : {
            type : String,
            required: true
        }
    },
    computed:{
        listItems(){
            return _.groupBy(this.items, this.field);
        }
    }
}
</script>
<style lang="stylus">

</style>
