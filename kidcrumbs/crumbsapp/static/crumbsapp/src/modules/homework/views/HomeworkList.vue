<template>
    <div id="homeWorkList" v-if="!isLoading">
        <section v-if="editable">
            <div class="add-btn">
                <md-button class="md-fab md-mini" @click="addHomework">
                    <md-icon class="fas fa-plus"></md-icon>
                </md-button>
            </div>
        </section>
        <div class="d-flex align-items-center flex-wrap">
            <div class="col p-0">
                <dtpicker :disable-time="true" :dark="isDark" :without-header="true" v-model="date" format="YYYY-MM-DD" :auto-close="true" formatted="dddd, MMMM DD, YYYY" label="Select date"></dtpicker>
            </div>
            <div class="col-12 p-0 d-flex">
                <div class="col d-flex justify-content-betwen align-items-center p-0">
                    <div class="col-auto p-0">
                        <md-checkbox class="md-primary" v-model="showAll">Show All</md-checkbox>
                    </div>
                    <div class="col-auto px-4 pb-1 d-flex align-items-center">
                        <div class="col-auto p-0">
                            <md-switch v-model="sortAsc" class="md-primary"> </md-switch>
                        </div>
                        <div class="col-auto p-0 pb-1" style="margin-left : -10px !important">
                            <p class="m-0" v-if="sortAsc" key="up"> <i class="fas fa-sort-amount-up fa-fw"></i></p>
                            <p class="m-0" v-else key="down"> <i class="fas fa-sort-amount-down fa-fw"></i></p>
                        </div>
                    </div>
                </div>
                <div class="col d-flex justify-content-end p-0">
                    <div class="col-auto p-0">
                        <md-radio class="md-primary" v-model="status" value="">all</md-radio>
                        <md-radio class="md-primary" v-model="status" :value="false">active</md-radio>
                        <md-radio class="md-primary" v-model="status" :value="true">inactive</md-radio>
                    </div>
                </div>
            </div>
        </div>
        <hr class="m-1 p-1">
        <div class="homework-list">
            <homeworks :sortOrder="sorting" :homeworks="homeworks" :date="dateChoice" @homework-click="homeworkClicked($event)"></homeworks>
        </div>
    </div>
</template>
<script>
import homeworks from '../components/homeworks.vue';
import dropdown from '../../../components/dropdown.vue';
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "HomeWorkList",
    created(){
        this.fetchHomeworks().then( homeworks => {
            this.isLoading = false;
        });
    },
    props:{
        editable : {
            type : Boolean,
            default : false
        }
    },
    data(){
        return {
            date : moment().format("YYYY-MM-DD"),
            isLoading : true,
            showAll : false,
            sortAsc : true,
            status : ''
        }
    },
    components:{
        dropdown,
        homeworks
    },
    computed:{
        ...mapGetters([
            'getTheme'
        ]),
        ...mapGetters('homework',[
            'getHomeworks'
        ]),
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
#homeWorkList
    .add-btn
        position fixed
        bottom 50px
        right 5px
</style>

