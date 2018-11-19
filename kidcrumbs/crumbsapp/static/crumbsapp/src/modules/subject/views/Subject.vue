<template>
    <div id="subject">
        <page>
            <router-view></router-view>
        </page>
    </div>
</template>
<script>
import page from '../../../components/page.vue';
export default{
    name : "Subject",
    components:{
        page
    }

}
</script>
<style lang="stylus">

</style>
