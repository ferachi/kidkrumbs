<template>
    <div id="habitToday">
    </div>
</template>
<script>
export default {
    name : 'HabitSelect',
    created(){
        this.$router.push({name:'habitByDate', params:{date:moment().format("YYYY-MM-DD")}});
    }
}

</script>
<style lang="stylus">

</style>
