<template> 
    <div id="themer">
        <section class="d-flex align-items-center justify-content-between">
            <div class="col-auto">
                <md-switch v-model="isLight" class="md-primary m-0"><small v-html="themeIcon"></small><small>{{nextTheme}}</small></md-switch>
            </div>
            <div class="col-auto">
                <p class="m-0 primary-color clickable" @click="showModal"><span class="fas fa-palette fa-fw fa-lg"></span></p>
            </div>
        </section>
        <section>
            <modal ref="modal" :enable-mobile-fullscreen="false" :modal-theme="theme" :overlay-theme="theme" :blocking="false" >
                <label for="title">select a color</label>
                <swatches v-model="color" :colors="getColors" shapes="circles" inline/>
            </modal>
        </section>
    </div>
</template>
<script>
import {mapGetters, mapMutations} from 'vuex';
import { SweetModal } from 'sweet-modal-vue';
import Swatches from 'vue-swatches'
export default {
    name : 'Themer',
    created(){
        this.color = this.getColor;
        this.isLight = this.theme == 'light';
    },
    components:{
        modal:SweetModal,
        Swatches
    },
    computed : {
        ...mapGetters({'theme':'getTheme'}),
        ...mapGetters(['getColors', 'getColor']),
        themeIcon(){
            return this.isLight ? `<span class="fas fa-moon fa-fw fa-sm"></span>` : `<span class="fas fa-sun
            fa-fw fa-sm"></span>`;
        },
        nextTheme(){
            return this.isLight ? 'dark' : 'light';
        }
    },
    data(){
        return {
            isLight :null  ,
            color:''
        }
    },
    methods:{
        ...mapMutations(['setTheme']),
        ...mapMutations(['setColor']),
        showModal(){
            this.$refs.modal.open();
        }
    },
    watch:{
        isLight(val){
            let theme = val ? 'light' : 'dark';
            this.setTheme(theme);
        },
        color(val){
            this.setColor(val);
            this.$refs.modal.close();
        }
    }
}
</script>
<style lang="stylus">
</style>
