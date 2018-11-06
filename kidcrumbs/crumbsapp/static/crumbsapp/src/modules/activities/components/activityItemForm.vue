<template>
    <div id="activityItemForm">
        <form @submit.prevent="validateBeforeSubmit">
            <div class="form-group">
                <label for="title">title</label>
                <input v-model="activityItem.title" v-validate="'required|min:10|max:45'" id="title" name="title"
                                                                                               class="form-control" type="text" placeholder="title"/>
                <i v-show="errors.has('title')" class="fa fa-warning"></i>
                <span class="text-danger">{{ errors.first('title') }}</span> 
            </div>
            <div class="form-group">
                <label for="title">description</label>
                <textarea v-model="activityItem.description" v-validate="'required|min:20|max:450'" id="description"
                                                                                             name="description" class="form-control" placeholder="description" rows=3>
                </textarea>
                <i v-show="errors.has('title')" class="fa fa-warning"></i>
                <span class="text-danger">{{ errors.first('description') }}</span> 
            </div>
            <div class="form-group">
                <label for="title">select a color</label>
                <swatches v-model="activityItem.color" :colors="colors" shapes="circles" inline/>
            </div>
            <div class="form-group">
                <label for="title">time</label>
                <dtpicker v-model="activityItem.time" :color="activityItem.color" :dark="false" formatted="h:mm a"
                format="HH:mm" time-format="h:mm a" :minute-interval="5" label="" :without-input="true" :without-header="true" disable-date />
            </div>
            <div class="form-group clearfix">
                <button type="submit" class="btn btn-primary float-right">Submit</button>
            </div>
        </form>
    </div>
</template>
<script>
import Swatches from 'vue-swatches'
import "vue-swatches/dist/vue-swatches.min.css"

export default {
    name: "activityItemForm",
    created(){
        if(!this.item){
                let time = moment().format("hh:mm"),
                color = "DODGERBLUE";
            this.activityItem = { time, color};
        }
    },
    data(){
        return{
            activityItem : this.item,
            colors: ['DODGERBLUE', 'RED', 'DARKSEAGREEN', 'ORANGE']
        }
    },
    props:{
        item : {
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
                    this.activityItem._time = moment(this.activityItem.time, "HH:mm").format("hh:mm a");
                    this.$emit("form-submit", this.activityItem)
                    return;
                }
            });
        }
    }
};
</script>
<style lang="stylus">
#activityItemEdit
    min-height 30vh
</style>
