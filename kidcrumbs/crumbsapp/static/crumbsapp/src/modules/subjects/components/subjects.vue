<template>
    <div class="subjects">
        <search-list :items="subjects" :search="search" :searchFields="['name', 'subject_code','overview']">
            <section slot="controls"> 
                <md-field>
                    <label >search</label>
                    <md-input v-model='search'></md-input>
                </md-field>
            </section>
            <section slot="items" slot-scope="{items}">
                <div v-for="item in items" :key="item.id">
                    {{item.name}}                    
                </div>    
            </section>
        </search-list>
    </div>
</template>
<script>
import searchList from '../../../components/alterlist.vue';
export default{
    name : "Subjects"
    props : {
        subjects : {
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
        searchList
    }
}
</script>
<style lang="stylus">

</style>
