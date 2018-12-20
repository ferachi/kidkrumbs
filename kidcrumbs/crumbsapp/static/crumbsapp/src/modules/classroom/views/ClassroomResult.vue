<template>
    <div id="ClassroomResult" class="">
        <h4 class="font-weight-bold m-0 text-capitalize"> Result </h4>
        <hr>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
export default {
    name: "ClassroomResults",
    components : {
    },
    computed : {
        ...mapGetters('classroom', {classroom : 'getClassroom'}),
        ...mapGetters('profile', {profile : 'getProfile' }),
    },
    data(){
        return {
        }
    },
    methods : {
    }
};
</script>
<style lang="stylus">
</style>
