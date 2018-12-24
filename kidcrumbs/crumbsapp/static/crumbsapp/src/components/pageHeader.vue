<template>
    <div id="pageHeader" class="p-2" >
        <div class="d-flex justify-content-between align-items-center">
            <div class="col-10 px-1">
                <slot name="pageTitle"></slot>
            </div>
            <div class="col-auto px-0">
                <slot name="pageMenu">
                    <p class="m-0 d-inline-block color_white" @click="$emit('page-head-menu-click')"> <i class="fas fa-ellipsis-v fa-fw fa-lg"></i></p>
                </slot>
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
