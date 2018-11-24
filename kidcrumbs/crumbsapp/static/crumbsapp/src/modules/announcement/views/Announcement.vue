<template>
    <div id="Announcement">
        <page>
        <router-view></router-view>
        </page>
    </div>
</template>
<script>
import page from '../../../components/page.vue';
export default{
    name : "Announcement",
    components :{
        page
    }
}
</script>
<style lang="stylus">
</style>

