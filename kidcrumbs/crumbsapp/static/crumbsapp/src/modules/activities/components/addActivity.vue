<template>
    <div id="addActivity">
        <div class="py-3">
            <h4 class="font-weight-bold">New Activity</h4>
            <a-form @form-submit="submitForm($event)"></a-form>
        </div>
    </div>
</template>
<script>
import activityForm from "./activityForm.vue";
export default {
    name: "addActivity",
    components:{
        aForm : activityForm,
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
