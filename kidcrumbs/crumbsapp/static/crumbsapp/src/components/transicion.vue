<template>
    <div class="transicion">
        <transition :name="name" :mode="mode">
            <div v-if="isLoading" key="loading">
                <slot name="loader">
                    <loader></loader>
                </slot>
            </div>
            <div v-else key="loaded">
                <slot>
                
                </slot>
            </div>
        </transition>
    </div>
</template>
<script>
import loader from './loader.vue';
export default{
    name : "Transicion",
    created(){
    },
    props:{
        name : {
            type : String,
            default : 'fade'
        }, 
        mode : {
            type : String, 
            default : 'out-in'
        },
        isLoading : {
            type : Boolean,
            required : true
        }
    },
    components:{
        loader
    },
}
</script>
<style lang="stylus">
</style>

