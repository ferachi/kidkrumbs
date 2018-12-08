<template>
    <div id="ClassroomDetail" class="">
        <transicion :isLoading="loading">
            {{classroom}} 
        </transicion>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import transicion from '../../../components/transicion.vue';
export default {
    name: "ClassroomDetail",
    created(){
        this.fetchData();
    },
    components : {
        transicion
    },
    data(){
        return {
            loading : true,
            classroom : {}
        }
    },
    methods :{
        ...mapActions('classroom', ['fetchClassroom']),
        fetchData(){
            this.fetchClassroom(this.$route.params.id).then(classroom => {
                this.classroom = classroom; 
                this.loading = false;
            });
        },
    }
};
</script>
<style lang="stylus">
</style>
