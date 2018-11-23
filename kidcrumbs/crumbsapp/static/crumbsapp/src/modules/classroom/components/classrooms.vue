<template>
    <div class="classrooms">
        <search-list :items="classrooms" :search="search" :searchFields="['className','tags','overview']">
            <section slot="controls"> 
                <md-field>
                    <label >search</label>
                    <md-input v-model='search'></md-input>
                </md-field>
            </section>
            <section slot="items" slot-scope="{items}">
                <div class="d-flex flex-wrap my-4">
                    <div class="col-6 col-xl-3 px-2" v-for="classroom in items" :key="classroom.id"
                                                          @click="$emit('classroom-click', classroom)">
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
