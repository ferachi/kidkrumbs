<template>
    <div id="ProfileDetail">
        {{profile}}
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : "ProfileDetail",
    created(){
        let username = this.$route.params.username;
        this.fetchProfile(username).then(profile =>{
            this.profile = profile;    
        });
    },
    data(){
        return {
            profile : null
        }
    },
    methods:{
        ...mapActions('person',[
            'fetchProfile'
        ])
    }

    

}
</script>
<style lang="stylus"></style>
