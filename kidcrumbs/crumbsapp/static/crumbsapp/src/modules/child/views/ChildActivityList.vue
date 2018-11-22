<template>
    <div id="childActivityList" class="">
    </div>
</template>
<script>
export default{
    name : "ChildActivityList",
    created(){
        this.$router.push({name: "activityDateDetail", params : {date : moment().format("YYYY-MM-DD")}});
    }
}
</script>
<style lang="stylus">
</style>

