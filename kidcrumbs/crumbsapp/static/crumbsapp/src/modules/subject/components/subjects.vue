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
                <hr>
                <group-by :items="items" field="session">
                    <div slot-scope="{values, id}" >
                        <div class="d-flex flex-wrap my-4">
                            <h4 class="font-weight-bold col-12 righteous">{{id}}</h4>
                            <div class="col-12 col-md-6 col-xl-3" v-for="subject in values" :key="subject.id"
                            @click="$emit('subject-click', subject)">
                                <list-item :subject="subject"></list-item>
                            </div>
                        </div>
                        <hr>
                    </div>
                </group-by>
                <!-- <div v&#45;for="item in items" :key="item.id"> -->
                <!--     <h6>{{item.name}}</h6> -->
                <!--     <p class="color_3">{{item.subject_code}}</p> -->
                <!-- </div>     -->
            </section>
        </search-list>
    </div>
</template>
<script>
import searchList from '../../../components/alterlists.vue';
import groupBy from '../../../components/group-by.vue';
import listItem from './subject-list-item.vue';
export default{
    name : "Subjects",
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
        searchList,
        groupBy, 
        listItem
    }
}
</script>
<style lang="stylus">

</style>
