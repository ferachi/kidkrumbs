<template>
    <div id="ClassroomProfile" class="">
        <classroom :classroom="classroom"></classroom>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
import  classroom from '../components/classroom-profile.vue';
export default {
    name: "ClassroomProfile",
    components : {
        classroom
    },
    computed : {
        ...mapGetters('classroom', {classroom : 'getClassroom' } ),
    }
};
</script>
<style lang="stylus">
</style>
