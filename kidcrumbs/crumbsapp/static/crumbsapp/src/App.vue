<template lang="html">
    <div :id='theme.app'>
        <div v-if="!isLoading" class="" key='app'>
            <div id="app" class="green">
        	    <p class="primary-color">Hello again</p>
                <form action="">
                <div class="form-group">
                    <label for="exampleInputEmail1" class="bmd-label-floating">Email address</label>
                    <input type="email" class="form-control" id="exampleInputEmail1">
                    <span class="bmd-help">We'll never share your email with anyone else.</span>
                </div></form>
            </div>
        </div>
        <div v-else key='loader'>
            Loading...
        </div>
    </div>
</template>

<script>
import {mapGetters, mapActions, mapMutations} from "vuex";
export default {
    created() {
        // get the device type on which the application runs
        // note: this actually sets up the device on the store by
        // running it on the first create (before mount)
        this.$store.dispatch('getDevice').then(res => {
            this.isLoading = false;
            this.theme = this[this.getTheme];
        });
    },
    data(){
        return {
            isLoading:true,
            theme:''
        };
    },
    computed : {
        ...mapGetters([
            'getTheme'
        ])
    },
    methods:{
        ...mapMutations([
            "setTheme"
        ])
    }

};
</script>

<style lang="stylus" module="dark">
theme="dark"
#app
    :global
        @import './styles'
</style>

<style lang="stylus" module="light">
theme="light"
#app
    :global
        @import './styles'
</style>

<style lang="stylus" module="krumbs">
theme="krumbs"
#app
    :global
        @import './styles'
</style>

<style lang="stylus">
#app.orange
    appColor =split(" ",split(".",selector())[1])[0] 
    @import './styles' 
#app.blue
    appColor =split(" ",split(".",selector())[1])[0] 
    @import './styles' 
#app.red
    appColor =split(" ",split(".",selector())[1])[0] 
    @import './styles' 
</style>

