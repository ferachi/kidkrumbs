<template>
    <div id="homeWork" class="p-3">
        <page v-if="!isLoading">
        <router-view></router-view>
        </page>
    </div>
</template>
<script>
import page from '../../../components/page.vue';
import {mapGetters, mapActions} from 'vuex'
export default{
    name : "HomeWork",
    created(){
        this.fetchClassroom(this.classroomId).then( classroom => {
            this.isLoading = false;
        });
    },
    components:{
        page
    },
    data(){
        return {
            classroomId : '944e18be-0b51-4ab5-a584-a87811cf1886', // test classroom Id
            isLoading : true
        }
    },
    methods:{
        ...mapActions('classroom',[ 'fetchClassroom' ]),
    }
}
</script>
<style lang="stylus">
</style>

