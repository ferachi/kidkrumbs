<template>
    <div id="pageComponent" class="d-flex justify-content-center flex-wrap">
        <!-- This component -->
        <header class="col-12 px-0">
            <slot name='header'>
            </slot>
        </header>
        <div class="content col-xl-7 col-lg-8 col-12 px-0 ">
            <slot>
                Content comes here
            </slot>
        </div>

        <footer>
            <slot name='footer'>
            </slot>
        </footer>
    </div>
</template>
<script>
export default {
    name: "pageComponent",
};
</script>
<style lang="stylus">
#pageComponent
    >.content
        max-height 80vh
        overflow-y auto
</style>
