<template>
    <div id="childProfile" >
        <profile :profile="getChild"></profile>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import profile from '../../profile/components/profile-summary.vue';
export default{
    name : "ChildProfile",
    computed : {
        ...mapGetters('child',['getChild'])
    },
    components:{
        profile
    }
}
</script>
<style lang="stylus">
</style>

