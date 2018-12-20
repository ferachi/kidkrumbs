<template>
    <div id="activityForm">
        <form @submit.prevent="validateBeforeSubmit">
            <div class="form-group">
                <label for="title">Date</label>
                <dtpicker v-model="factivity.date" :dark="theme" format="YYYY-MM-DD"  formatted="DD/MM/YYYY" label="Date" :without-header="true" :auto-close="true" disable-time />
            </div>
            <div class="form-group">
                <label for="title">select a color</label>
                <swatches v-model="factivity.color" :colors="colors" shapes="circles" inline/>
            </div>
            <div class="form-group">
                <label for="title">Teachers' Comment</label>
                <textarea v-model="factivity.note" v-validate="'min:10|max:450'" id="note" name="note"
                    class="form-control" placeholder="Teachers' comment" rows=3>
                </textarea>
                <i v-show="errors.has('note')" class="fa fa-warning"></i>
                <span class="text-danger">{{ errors.first('note') }}</span> 
            </div>
            <div class="form-group clearfix">
                <button type="submit" class="btn btn-primary float-right">Submit</button>
            </div>
        </form>
    </div>
</template>
<script>
import Swatches from 'vue-swatches'
import {mapGetters} from 'vuex';
import "vue-swatches/dist/vue-swatches.min.css"

export default {
    name: "activityForm",
    created(){
        if(!this.activity){
            let color = "DODGERBLUE",
                jsDate = new Date(),
                date = jsDate.toISOString();
            this.factivity = {color,date};
        }
    },
    data(){
        return{
            factivity : this.activity,
            colors:[
                [ 'DARKRED','RED','ORANGERED','TOMATO',],
                ['SEAGREEN','FORESTGREEN','DARKOLIVEGREEN','TEAL'],
                ['LIGHTBLUE','DODGERBLUE','DARKBLUE','CADETBLUE'],
                ['REBECCAPURPLE','MEDIUMPURPLE','PLUM','HOTPINK'],
            ]
        }
    },
    computed:{
        ...mapGetters([
            'getTheme'
        ]),
        theme(){
            return this.getTheme == 'dark';
        }
    },
    props:{
        activity : {
            type : Object,
            default : null 
        }
    },
    components:{
        swatches: Swatches,
    },
    methods:{
        validateBeforeSubmit() {
            this.$validator.validateAll().then((result) => {
                if (result) {
                    this.$emit("form-submit", this.factivity)
                    return;
                }
            });
        }
    },
    watch:{
        activity(val){
            this.factivity = val;
        }
    }
};
</script>
<style lang="stylus">
#activityForm
    min-height 30vh
</style>
