<template>
    <div id="ClassroomDetail" class="">
        <transicion :isLoading="loading">
        <page>
            <div slot="header">
                <page-header class="primary-bg">
                    <div slot="pageTitle">
                        <h1 class="m-0 color_white">Title</h1>
                    </div>
                    <div slot="pageMenu">
                        <p class="m-0"><i class="fas fa-bars fa-fw"></i></p>
                        <p class="m-0"><i class="fas fa-glasses fa-fw"></i></p>
                    </div>
                    <div class="menu d-flex justify-content-center">
                        <div class="col-lg-8 px-0 ">
                            <page-menu :menus="menus" >
                                <div slot-scope="{menu}" class="clickable">
                                    <p class="mb-1" :class="{'color_white':menu.active}">{{menu.title}}</p>
                                </div>
                            </page-menu> 
                        </div>
                    </div>
                </page-header>
            </div>
        </page>
        </transicion>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import transicion from '../../../components/transicion.vue';
import pageMenu from '../../../components/pageMenu.vue';
import pageHeader from '../../../components/pageHeader.vue';
import page from '../../../components/page.vue';

let menus = [
    { title : 'profile', name : 'profile', link : '', active : true, index : 0},
    { title : 'activity', name : 'activities', link : '', active : false, index : 1},
    { title : 'behaviour', name : 'behaviour', link : '', active : false, index : 2},
    { title : 'homework', name : 'homework', link : '', active : false, index : 3}
]
export default {
    name: "ClassroomDetail",
    created(){
        this.fetchData();
    },
    components : {
        transicion,
        page,
        pageHeader,
        pageMenu
    },
    data(){
        return {
            loading : true,
            classroom : {},
            menus : menus
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
