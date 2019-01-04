<template>
    <div id="student">
        <title-header></title-header>        
        <section class="result-content">
            <transition name="fade" mode="out-in">
                <router-view></router-view>
            </transition>
        </section>
    </div>
</template>
<script>
import titleHeader from '../components/title-header.vue';
export default {
    name : "Student",
    components : {
        titleHeader
    }
}
</script>
<style lang="stylus">
#result
    .result-content
        max-height 90vh
        overflow-y auto
</style>
