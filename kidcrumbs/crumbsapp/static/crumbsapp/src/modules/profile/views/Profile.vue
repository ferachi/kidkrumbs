<template>
    <div id="Profile">
        <page>
            <router-view></router-view>
        </page>
    </div>
</template>
<script>
import page from '../../../components/page.vue'
export default{
    name : "Profile",
    components:{
        page
    }
}
</script>
<style lang="stylus"></style>
