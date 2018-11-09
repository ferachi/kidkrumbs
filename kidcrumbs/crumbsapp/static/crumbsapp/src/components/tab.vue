<template>
    <div class="crumb-tab" v-show='isActive'>
        <slot>

        </slot>
    </div>
</template>
<script>
export default {
    name: "",
    data(){
        return{
            isActive : this.selected
        };
    },
    props:{
        name:{
            type:String,
            required:true
        },
        selected:{
            type:Boolean,
            default:false
        }
    }
};
</script>
<style lang="stylus">
</style>
