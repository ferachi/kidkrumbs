<template>
    <div id="activityItemAdd">
        <div class="py-3">
            <h4 class="font-weight-bold">New Activity</h4>
            <a-form @form-submit="submitForm($event)"></a-form>
        </div>
    </div>
</template>
<script>
import activityItemForm from "./activityItemForm.vue";
export default {
    name: "activityItemAdd",
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
