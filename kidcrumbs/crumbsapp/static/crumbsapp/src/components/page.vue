<template>
    <div id="pageComponent" class="d-flex justify-content-center flex-wrap">
        <!-- This component -->
        <header class="col-12 px-0">
            <slot name='header'>
            </slot>
        </header>
        <div class="content col-12 d-flex justify-content-center px-0">
            <div class="col-xl-6 col-lg-8 col-12 px-0">
                <slot>
                    Content comes here
                </slot>
            </div>
        </div>
        <footer class="col-12">
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
        max-height 90vh
        overflow-y auto
</style>
