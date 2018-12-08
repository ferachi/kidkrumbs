<template>
    <div id="pageHeader" >
        <div class="d-flex justify-content-between align-items-center py-2 primary-bg">
            <div class="col-auto">
                <slot name="pageTitle"></slot>
            </div>
            <div class="col-auto">
                <slot name="pageMenu"></slot>
            </div>
        </div>
        <div>
            <slot></slot>
        </div>
    </div>
</template>
<script>
export default {
    name: "pageHeaderComponent",
};
</script>
<style lang="stylus">
</style>
