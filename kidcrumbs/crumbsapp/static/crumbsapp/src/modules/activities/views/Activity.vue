<template>
    <div id="activity" class="p-2">
        <h4>Activity</h4>
        <page>
            <router-view></router-view>
        </page>
    </div>
</template>
<script>
import page from "../../../components/page.vue"
export default{
    name : "Activity",
    created(){
    },
    components:{
        page,
    }
}
</script>
<style lang="stylus">
</style>

