<template>
    <div id="ClassroomList" class="">
        <transicion :isLoading="loading">
           <div class="classroom-list">
               <classrooms :classrooms="classrooms" @classroom-click="classroomClicked($event)"></classrooms> 
           </div>
        </transicion>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import transicion from '../../../components/transicion.vue';
import classrooms from '../components/classrooms.vue';
export default {
    name: "ClassroomList",
    created(){
        this.fetchData();
    },
    computed :{
    },
    components:{
        transicion,
        classrooms
    },
    data(){
        return {
            classrooms : [],
            loading : true
        }
    },
    methods :{
        ...mapActions('classroom', ['fetchClassrooms']),
        fetchData(){
            this.fetchClassrooms(this.$route.params.id).then( classrooms => {
                this.classrooms = classrooms;
                this.loading = false;
            });
        },
        classroomClicked(classroom){
            this.$router.push({name : 'classroomDetail', params : {id : classroom.id}});
        }
    }
};
</script>
<style lang="stylus">
</style>
