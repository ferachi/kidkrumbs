<template>
    <div id="resultDetail">
        <transicion :isLoading="loading">
            <div>
                <div>
                    <tab-head :tabTitles="['overview', 'report']" @tab-click="tabClicked($event)"
                    justify="justify-content-end">
                        <div slot="tab" slot-scope="{tab}" class="p-2"><p :class="{'primary-color':tab.isActive}">{{tab.name}}</p></div>  
                    </tab-head>   
                </div>
                <div>
                    <div class="overview" v-if="activeTab=='overview'">
                       <overview :results="results"></overview>
                    </div>
                    <div class="report" v-else>
                        <h4>Report</h4>
                    </div>
                </div>
            </div>
        </transicion>
    </div>
</template>
<script>
import {mapActions, mapGetters} from 'vuex';
import transicion from '../../../components/transicion.vue';
import tabHead from '../../../components/tabHead.vue';
import overview from '../components/result-overview.vue';
export default {
    name : "ResultDetail",
    created(){
        this.fetchData();
    },
    components : {
        transicion,
        tabHead,
        overview
    },
    data(){
       return  {
           results : [],
           activeTab : 'overview',
           loading : true
       }
    },
    methods : {
        ...mapActions('result', ['fetchStudentResults']),
        fetchData(){
            this.fetchStudentResults(this.$route.params.username).then(results => {
                this.results = results;
                this.loading = false;
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
