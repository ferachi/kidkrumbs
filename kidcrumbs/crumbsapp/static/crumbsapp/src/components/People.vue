<template>
    <div>
        <alter-list :items="people" :search="search" :searchFields="['first_name', 'last_name', 'other_names']">
            <div slot="controls" class="d-flex justify-content-center">
                <div class="col-md-8">
                    <md-field>
                        <label>Search</label>
                        <md-input v-model="search" ></md-input>
                    </md-field>
                </div>
            </div>
            <div slot="items" class="d-flex align-items-center flex-wrap" slot-scope="{ items }">
                <div class="col-6 col-md-3 col-xl-2 p-2" v-for="item in items">
                    <div class="text-center " @click="personClicked(item)">
                        <div class="d-inline-block clickable p-2">
                        <div class="clickable" v-if="item.avatar" key="avatar">
                            <md-avatar class="md-large">
                                <img :src="item.avatar" alt="People">
                            </md-avatar>
                        </div>
                        <div v-else key="noAvatar">
                            <md-avatar class="md-avatar-icon md-large">
                                <md-icon class="fas fa-user"></md-icon>
                            </md-avatar>
                        </div>
                        <h6 class="m-0"><small>{{item.last_name}} {{item.first_name}}</small></h6>
                        </div>
                    </div>
                </div>
            </div>
        </alter-list>
    </div>
</template>
<script>
import alterList from './alterlists.vue';
export default{
    name : "People",
    created(){
    },
    props:{
        people : {
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
        personClicked(person){
            this.$emit('person-click', person);
        }
    }
}
</script>
<style lang="stylus">
</style>
