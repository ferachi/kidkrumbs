<template>
    <div id="loader" class="d-flex justify-content-center align-items-center loader">
        <self-building-square-spinner :animation-duration="6000" :size="60"/>
    </div>
</template>
<script>
import {SelfBuildingSquareSpinner} from 'epic-spinners';
export default {
    name: "loaderComponent",
    components:{
        SelfBuildingSquareSpinner
    }
};
</script>
<style lang="stylus">
</style>
