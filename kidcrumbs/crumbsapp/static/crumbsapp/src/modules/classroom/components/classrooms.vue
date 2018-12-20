<template>
    <div class="classrooms">
        <search-list :items="classrooms" :search="search" :searchFields="['className']">
            <section slot="controls" class="px-lg-5"> 
                <div class="d-flex align-items-center">
                    <div class="col px-1">
                        <md-field>
                            <label ><span class="fas fa-search fa-fw color_3"></span> search</label>
                            <md-input v-model='search'></md-input>
                        </md-field>
                    </div>
                </div>
                <hr>
            </section>
            <section slot="items" slot-scope="{items}">
                <div class="d-flex flex-wrap my-4">
                    <div class="col-6 col-xl-3 p-2" v-for="classroom in items" :key="classroom.id" @click="$emit('classroom-click', classroom)">
                        <list-item :classroom="classroom"></list-item>
                    </div>
                </div>
            </section>
        </search-list>
    </div>
</template>
<script>
import searchList from '../../../components/alterlists.vue';
import listItem from './classroom-list-item.vue';
export default{
    name : "Classrooms",
    props : {
        classrooms : {
            type : Array,
            required : true
        }
    },
    data(){
        return {
            search : '',
        }
    },
    components : {
        searchList,
        listItem
    }
}
</script>
<style lang="stylus">

</style>
