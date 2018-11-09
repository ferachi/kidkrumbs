<template>
    <div id="activityItemDetail">
        <div v-if="type == 'view'">
            <aiv :activity="activity"></aiv>
        </div>
        <div v-else>
            <aie :activity="activity"></aie>
        </div>
    </div>
</template>
<script>
import activityItemEdit from './ActivityItemEdit.vue';
import activityItemView from './ActivityItemView.vue';
export default {
    name: "activityItemDetail",
    components:{
        aie:activityItemEdit,
        aiv:activityItemView,
    },
    props:['type', 'activity']
};
</script>
<style lang="stylus">
</style>
