<template lang="html">
    <div :id='theme.app'>
        <div id="appTheme" :class="getColor" v-if="!isLoading" key='app'>
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
import * as d3 from 'd3';
import moment from 'moment';
import anime from 'animejs';

import Cropper from 'cropperjs'
export default {
    created() {
        // get the device type on which the application runs
        // note: this actually sets up the device on the store by
        // running it on the first create (before mount)
        window.moment = moment;
        window.d3 = d3;
        window.anime = anime;
        window.Cropper = Cropper;


        this.manageScreen();
        

        window.addEventListener("orientationchange",this.manageScreen);

        window.addEventListener('resize', this.manageScreen);

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
        ...mapGetters(['getColor'])
    },
    methods:{
        ...mapMutations([
            "setTheme"
        ]),
        ...mapActions("auth",[
            "obtainToken"
        ]),
        ...mapActions([
            "screenSize"
        ]),
        manageScreen(){
            this.screenSize().then( screen =>{
                this.theme = this[this.getTheme];
                this.isLoading = false;
            });
        }
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


