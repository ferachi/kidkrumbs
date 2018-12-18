<template>
    <div id="Classroom" class="">
        <transition name="fade-up" mode="out-in">
            <router-view></router-view>
        </transition>
    </div>
</template>
<script>
export default {
    name: "Classroom",
};
</script>
<style lang="stylus">
#Classroom
    .add-btn
        position fixed
        bottom 50px
        right 10px
</style>
