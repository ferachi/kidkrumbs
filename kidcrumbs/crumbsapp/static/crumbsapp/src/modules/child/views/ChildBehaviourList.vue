<template>
    <div id="childBehaviourList" class="">
    </div>
</template>
<script>
export default{
    name : "ChildBehaviourList",
    created(){
        this.$router.push({name: "childBehaviour", params : {date : moment().format("YYYY-MM-DD")}});
    }
}
</script>
<style lang="stylus">
</style>

