<template>
    <div id="activityItemDelete" class="text-center">
        <h4>Are you sure you want to delete</h4>
        <h1>{{activity.title}}</h1>
        <div class="clearfix">
            <button class="btn btn-danger" @click="deleteItem(true)"> Yes</button>         
            <button class="btn btn-primary" @click="deleteItem(false)"> No</button>         
        </div>
    </div>
</template>
<script>
export default {
    name: "activityItemDelete",
    props:['activity'], 
    methods:{
        deleteItem(canDelete){
            this.$emit("delete-item", canDelete);
        }

    }
};
</script>
<style lang="stylus">
</style>
