<template>
    <div id="activityItemEdit">
        <div class="py-3">
            <h4 class="font-weight-bold">Edit Activity</h4>
            <a-form :item="activity" @form-submit="submitForm($event)"></a-form>
        </div>
    </div>
</template>
<script>
import activityItemForm from "./activityItemForm.vue";
export default {
    name: "activityItemEdit",
    props:['activity'],
    components:{
        aForm : activityItemForm,
    },
    methods:{
        submitForm(item){
            this.$emit("form-submit", item);
        }
    }

};
</script>
<style lang="stylus">
</style>
