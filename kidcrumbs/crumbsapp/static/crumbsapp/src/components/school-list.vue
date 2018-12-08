<template>
    <div>
        <alter-list :items="schools" :search="search" :searchFields="['name', 'short_name', 'brief_description']">
            <div slot="controls" class="d-flex justify-content-center">
                <div class="col">
                    <md-field>
                        <label>Search</label>
                        <md-input v-model="search" ></md-input>
                    </md-field>
                </div>
            </div>
            <div slot="items" class="d-flex align-items-center flex-wrap" slot-scope="{ items }">
                <div class="col-sm-6 col-12 p-2" v-for="school in items" :key="school.id">
                    <div class="p-4 clickable" :style="{background:school.color}" @click="schoolClicked(school)">
                        <div class="d-flex align-items-center">
                            <div class="col-auto px-1">
                                <md-avatar class="md-small">
                                    <img :src="school.logo" :alt="school.name">
                                </md-avatar>
                            </div>
                            <div class="col px-3 py-4">
                                <h6 class="font-weight- color_white ">
                                    {{school.name}} 
                                </h6>
                            </div>
                        </div>
                        <p class="color_white"> {{school.motto}}</p>
                    </div>
                </div>
            </div>
        </alter-list>
    </div>
</template>
<script>
import alterList from './alterlists.vue';
export default{
    name : "schoolListComp",
    created(){
    },
    props:{
        schools : {
            type : Array,
            required : true
        }
    },
    data(){
        return {
            search : '',
        }
    },
    components:{
        alterList, 
    }, 
    methods:{
        schoolClicked(school){
            this.$emit('school-click', school);
        }
    }
}
</script>
<style lang="stylus">
</style>
