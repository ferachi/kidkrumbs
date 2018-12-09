<template>
    <div id="ClassroomBehaviour" class="">
        <h1>Behaviour</h1>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
export default {
    name: "ClassroomBehaviour",
    components : {
    },
    computed : {
        ...mapGetters('classroom', {classroom : 'getClassroom' } ),
    }
};
</script>
<style lang="stylus">
</style>
