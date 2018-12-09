<template>
    <div id="pageHeader" class="p-2" >
        <div class="d-flex justify-content-between align-items-center">
            <div class="col-auto px-1">
                <slot name="pageTitle"></slot>
            </div>
            <div class="col-auto px-1">
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
