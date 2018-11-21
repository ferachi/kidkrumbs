<template>
    <div id="childInit" class="">
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : "ChildInit",
    created(){
        this.$router.push({name:"activityDateDetail", params:{date:moment().format("YYYY-MM-DD")}});
    },
}
</script>
<style lang="stylus">
</style>

