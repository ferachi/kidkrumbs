<template>
    <div id="editActivity">
        <div class="py-3">
            <h4 class="font-weight-bold">Edit Activity</h4>
            <actform :activity="activity" @form-submit="submitForm($event)"></actform>
        </div>
    </div>
</template>
<script>
import actform from "./activityForm.vue";
export default {
    name: "editActivity",
    components:{
        actform,
    },
    props:["activity"],
    methods:{
        submitForm(item){
            this.$emit("form-submit", item);
        }
    }

};
</script>
<style lang="stylus">
</style>
