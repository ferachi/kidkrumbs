<template>
    <div id="homeWorkList" v-if="!isLoading">
        <div class="d-flex align-items-center">
            <div class="col p-0">
                <dtpicker :disable-time="true" :dark="isDark" :without-header="true" v-model="date" format="YYYY-MM-DD" :auto-close="true" formatted="dddd, MMMM DD, YYYY" label="Select date"></dtpicker>
            </div>
            <div class="col-auto px-1" v-if="editable">
                <!-- <dropdown :right="true">  -->
                <!--     <template slot="menuBtn"> -->
                <!--         <span class="fas fa&#45;ellipsis&#45;v fa&#45;fw"></span>   -->
                <!--     </template> -->
                <!--     <button class="dropdown&#45;item" @click="addHomework"><span class="fas fa&#45;plus fa&#45;fw"></span> Add Homework</button> -->
                <!-- </dropdown> -->
                <md-button class="md-icon-button md-raised md-primary" :md-theme="getTheme" @click="addHomework">
                    <md-icon class="fas fa-plus fa-fw"></md-icon>
                </md-button>
            </div>
        </div>
        <hr>
        <div class="homework-list">
            <homeworks :homeworks="homeworks" :date="date" @homework-click="homeworkClicked($event)"></homeworks>
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
            isLoading : true
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
        ...mapGetters('homework',{
            homeworks : 'getHomeworks'
        }),
        isDark(){
            return this.getTheme == 'dark';
        },

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

