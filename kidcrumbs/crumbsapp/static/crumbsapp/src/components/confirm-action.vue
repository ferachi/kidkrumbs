<template>
    <div id="confirmAction" class="text-center">
        <slot>
            <h1 class="display-3">Are you sure you want to do this?</h1>
        </slot>
        <div class="clearfix">
            <button class="btn btn-danger" @click="confirmed(true)"> Yes</button>         
            <button class="btn btn-primary" @click="confirmed(false)"> No</button>         
        </div>
    </div>
</template>
<script>
export default {
    name: "confirmAction",
    methods:{
        confirmed(confirmation){
            this.$emit("confirm", confirmation);
        }

    }
};
</script>
<style lang="stylus">
</style>
