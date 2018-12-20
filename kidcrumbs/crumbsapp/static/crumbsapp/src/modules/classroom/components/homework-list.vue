<template>
<transicion :isLoading="isLoading">
    <div id="homeworkList" >
        <section v-if="editable">
            <div class="add-btn">
                <md-button class="md-fab md-mini" @click="addHomework">
                    <md-icon class="fas fa-plus"></md-icon>
                </md-button>
            </div>
        </section>
        <div class="d-flex align-items-center flex-wrap">
            <div class="col-12 p-0 d-flex flex-wrap justify-content-between">
                <div class="col-auto p-0 order-sm-2">
                    <md-radio class="md-primary my-2" v-model="status" value="">all</md-radio>
                    <md-radio class="md-primary my-2" v-model="status" :value="false">active</md-radio>
                    <md-radio class="md-primary my-2" v-model="status" :value="true">inactive</md-radio>
                </div>
                <div class="col-auto p-0 order-sm-1">
                    <div class="d-none d-sm-block">
                        <div class="d-flex align-items-center" >
                            <div class="col-auto p-0">
                                <md-checkbox class="md-primary my-2" v-model="showAll">Show All</md-checkbox>
                            </div>
                            <div class="col-auto px-4 pb-1 d-flex align-items-center">
                                <div class="col-auto p-0">
                                    <md-switch v-model="sortAsc" class="md-primary my-2"> </md-switch>
                                </div>
                                <div class="col-auto p-0 pb-1" style="margin-left : -10px !important">
                                    <p class="m-0" v-if="sortAsc" key="up"> <i class="fas fa-sort-amount-up fa-fw"></i></p>
                                    <p class="m-0" v-else key="down"> <i class="fas fa-sort-amount-down fa-fw"></i></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col p-0 mt-3">
                <dtpicker :disable-time="true" :dark="isDark" :without-header="true" v-model="date" format="YYYY-MM-DD" :auto-close="true" formatted="dddd, MMMM DD, YYYY" label="Select date"></dtpicker>
            </div>
        </div>
        <div class="homework-list">
            <homeworks :sortOrder="sorting" :homeworks="homeworks" :date="dateChoice" @homework-click="homeworkClicked($event)"></homeworks>
        </div>
    </div>
    </transicion>
    
</template>
<script>
import homeworks from '../../homework/components/homeworks.vue';
import dropdown from '../../../components/dropdown.vue';
import transicion from '../../../components/transicion.vue';
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "HomeWorkList",
    mounted(){
        this.isLoading = false;
    },
    beforeDestroy(){
        $('.add-btn').hide();
    },
    props:{
        editable : {
            type : Boolean,
            default : false
        },
    },
    data(){
        return {
            date : moment().format("YYYY-MM-DD"),
            showAll : false,
            sortAsc : true,
            isLoading :true,
            status : ''
        }
    },
    components:{
        dropdown,
        transicion,
        homeworks
    },
    computed:{
        ...mapGetters([
            'getTheme'
        ]),
        ...mapGetters('classroom',{
            getHomeworks : 'getClassroomHomeworks'
        }),
        homeworks(){
            if(this.status === '') return this.getHomeworks;
            else return _.filter(this.getHomeworks, {isExpired : this.status})
        },
        isDark(){
            return this.getTheme == 'dark';
        },
        dateChoice(){
            return this.showAll ? '' : this.date;
        },
        sortOrder(){
            return this.sortAsc ? 'ascending' : 'descending';
        },
        sorting(){
            return this.sortAsc ? 'asc' : 'desc';
        }
    },
    methods:{
        ...mapActions('homework',[
            'fetchHomeworks',
        ]),
        homeworkClicked(homework){
            this.$emit('homework-click', homework);
        },
        addHomework(){
            this.$emit("add-homework");
        },
    }
}
</script>
<style lang="stylus">
</style>

