<template lang="html">
    <div :id='theme.app'>
        <div id="appTheme" class="teal" v-if="!isLoading" key='app'>
            <router-view></router-view>
        </div>
        <div v-else key='loader'>
            Loading...
        </div>
    </div>
</template>

<script>
import {mapGetters, mapActions, mapMutations} from "vuex";
import _ from 'lodash';
export default {
    created() {
        // get the device type on which the application runs
        // note: this actually sets up the device on the store by
        // running it on the first create (before mount)

        this.getDevice().then( values =>{
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
        ]),
    },
    methods:{
        ...mapMutations([
            "setTheme"
        ]),
        ...mapActions("auth",[
            "obtainToken"
        ]),
        ...mapActions([
            "getDevice"
        ])
    }, 
    watch:{
        'getTheme'(val){
            this.theme = this[this.getTheme];
        }
    }

};
</script>

<style lang="stylus" module="dark">
theme="dark"
themify() 
    appColor =split(" ",split(".",selector())[1])[0] 
    @import './styles'
#app
    :global
        // list of colors 
        colors = 'blue' 'pink' 'purple' 'red' 'green' 'orange' 'teal'

        // for each color create an app theme selector to call themify on
        for color in colors
            #appTheme.{color}
                themify()

</style>

<style lang="stylus" module="light">
theme="light"
themify() 
    appColor =split(" ",split(".",selector())[1])[0] 
    @import './styles'
#app
    :global
        // list of colors 
        colors = 'blue' 'pink' 'purple' 'red' 'green' 'orange' 'teal'

        // for each color create an app theme selector to call themify on
        for color in colors
            #appTheme.{color}
                themify()
</style>

<style lang="stylus" module="krumbs">
theme="krumbs"
#app
    :global
        @import './styles'
</style>


