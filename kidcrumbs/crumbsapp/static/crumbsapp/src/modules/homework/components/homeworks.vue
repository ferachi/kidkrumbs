<template>
    <div class="homeworks">
        <search-list :items="homeworks" :search="search" :filters="[{assigned_date:date}]" :sortFields="['assigned_date']" :order="[sortOrder]" :searchFields="['_name', 'description','date']">
            <section class="" slot="controls"> 
                <div class="">
                    <md-field class="mb-2">
                        <label >search</label>
                        <md-input v-model='search'></md-input>
                    </md-field>
                    <!-- <md&#45;checkbox v&#45;model="undone">show undone</md&#45;checkbox> -->
                </div>
            </section>
            <section slot="items" slot-scope="{items}">
                <div class="d-flex flex-wrap justify-content-center my-4">
                    <div class="col-12 col-md-8 " v-for="homework in items" :key="homework.id" @click="$emit('homework-click', homework)">
                        <list-item :homework="homework"></list-item>
                        <hr>
                    </div>
                </div>
            </section>
        </search-list>
    </div>
</template>
<script>
import searchList from '../../../components/alterlists.vue';
import dropdown from '../../../components/dropdown.vue';
import listItem from './homework-list-item.vue';
import {mapGetters} from 'vuex';
export default{
    name : "Subjects",
    created(){
    },
    props : {
        homeworks : {
            type : Array,
            required : true
        },
        date:{
            type : String,
            required : true
        },
        sortOrder : {
            type : String, // asc, desc
            default : 'desc'
        },
    },
    computed:{
        ...mapGetters([
            'getTheme'
        ]),
        isDark(){
            return this.getTheme == 'dark';
        }
    },
    data(){
        return {
            search : '',
        }
    },
    components : {
        searchList,
        listItem,
        dropdown
    },
}
</script>
<style lang="stylus">

</style>
