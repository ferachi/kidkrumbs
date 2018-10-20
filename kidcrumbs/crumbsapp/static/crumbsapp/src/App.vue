<template lang="html">
    <div class='app'>
        <div v-if="!isLoading" key='app'>
        	Hello again
        </div>
        <div v-else key='loader'>
            Loading...
        </div>
    </div>
</template>

<script>
export default {
    created() {
        // get the device type on which the application runs
        // note: this actually sets up the device on the store by
        // running it on the first create (before mount)
        this.$store.dispatch('getDevice').then(res => {
        	console.log("What is res", res);
            this.isLoading = false;
        });
    },
    data(){
        return {
            isLoading:true,
        };
    }
};
</script>

<style lang="stylus">
@import './styles'
</style>
