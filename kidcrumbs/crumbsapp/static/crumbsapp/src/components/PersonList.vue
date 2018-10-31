<template>
    <div>
        <alter-list :items="people" :searchFields="['first_name', 'last_name', 'other_names']">
            <div slot="items" class="d-flex align-items-center" slot-scope="{ items }">
                <div class="col-6 col-md-3 col-xl-2 px-1" v-for="item in items">
                    <div class="card" @click="personClicked(item)">
                        <div class="card-body">
                            <avatar :image="item.avatar" class="p-2" >
                            </avatar>
                            <h6 class="card-text text-center secondary-color">{{item.last_name}} {{item.first_name}}</h6>
                        </div>
                    </div>
                </div>
            </div>
        </alter-list>
    </div>
</template>
<script>
import alterList from './alterlists.vue';
import avatar from './avatarHolder.vue';
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
    components:{
        alterList, 
        avatar
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
