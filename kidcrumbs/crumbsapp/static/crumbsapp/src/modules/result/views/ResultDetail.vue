<template>
    <div id="resultDetail">
        <transicion :isLoading="loading">
            <div>
                <div class="d-flex py-3 align-items-center bg_0 m-1">

                    <div class="col d-flex align-items-center">
                        <div class="col-auto px-1">
                            <div v-if="student.avatar" key="avatar">
                                <md-avatar class="md-large">
                                    <img :src="student.avatar" alt="People">
                                </md-avatar>
                            </div>
                            <div v-else key="noAvatar">
                                <md-avatar class="md-avatar-icon md-large">
                                    <md-icon class="fas fa-user"></md-icon>
                                </md-avatar>
                            </div>
                        </div>
                        <div class="col-auto px-2">
                            <h6 class="font-weight-bold m-0 text-uppercase"> {{student.first_name}}</h6>                        
                            <h6 class="color_3 m-0"> {{student.last_name}}</h6>                        
                        </div>
                    </div>
                    <div class="col">
                        <tab-head :tabTitles="['overview', 'report']" @tab-click="tabClicked($event)"
                         justify="justify-content-end">
                            <div slot="tab" slot-scope="{tab}" class="p-2 clickable"><p class="m-0" :class="{'primary-color':tab.isActive}">{{tab.name}}</p></div>  
                        </tab-head>   
                    </div>
                </div>
                <div>
                    <transition name="fade-down-up" mode="out-in">
                        <div class="overview" v-if="activeTab=='overview'" key="overview">
                            <overview :results="results"></overview>
                        </div>
                        <div class="report" v-else key="report">
                            <report></report>
                        </div>
                    </transition>
                </div>
            </div>
        </transicion>
    </div>
</template>
<script>
import {mapActions, mapGetters, mapMutations} from 'vuex';
import transicion from '../../../components/transicion.vue';
import tabHead from '../../../components/tabHead.vue';
import overview from '../components/result-overview.vue';
import report from '../components/result-report.vue';
export default {
    name : "ResultDetail",
    created(){
        this.fetchData();
    },
    components : {
        transicion,
        tabHead,
        overview,
        report
    },
    data(){
       return  {
           results : [],
           activeTab : 'overview',
           loading : true
       }
    },
    computed : {
        ...mapGetters('result', ['getTableReport']),
        ...mapGetters('child', ['getChild']),
        student(){
            return this.getChild != null ? this.getChild : {};
        }
    },
    methods : {
        ...mapActions('result', ['fetchStudentResults', 'fetchReport']),
        ...mapActions('child', ['fetchChild', 'fetchChildResults']),
        fetchData(){
           this.fetchChild(this.$route.params.username).then(child => {
               this.fetchChildResults().then( results =>{
                   this.fetchReport().then( report => {
                       this.results = results;
                       this.loading = false;
                   });
               })
            });
        },
        tabClicked(tab){
            this.activeTab = tab; 
        }
    }
}
</script>
<style lang="stylus">

</style>
