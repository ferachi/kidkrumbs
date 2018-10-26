<template>
    <div id="pageComponent">
        <!-- This component -->
        <header>
            <slot name='header'>
            </slot>
        </header>
        <div class="content">
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
</style>
