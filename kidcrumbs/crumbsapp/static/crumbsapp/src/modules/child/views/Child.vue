<template>
    <div v-if="isLoading" key="loading">
    </div>
    <div id="child" v-else key="loaded">
        <div id="childContent">
            <section class="page-header primary-bg">
                <div class="d-flex align-items-center">
                    <div class="col-xl-1 col">
                        <avatar :image="child.avatar" class="p-2" :rounded="true" >
                        </avatar>
                    </div>
                    <div class="col-8">
                        <h4 class="color_0">{{child.names}}</h4>
                    </div>
                </div>
                <div class="d-flex align-items-center justify-content-around">
                    <router-link class="col p-0 py-3 text-center color_0" :to="{name:'childActivity', params:{id:1}}"><small class="color_0">Activity</small></router-link>
                    <router-link class="col p-0 text-center color_0" :to="{name:'childBehaviour', params:{id:1}}"><small class="color_0">Behaviour</small></router-link>
                    <router-link class="col p-0 text-center color_0" :to="{name:'childHomework', params:{id:1}}"><small class="color_0">Homework</small></router-link>
                    <router-link class="col p-0 text-center color_0" :to="{name:'app'}"><small class="color_0">More</small></router-link>
                </div>
            </section>
            <section class="p-2">

                <router-view></router-view>
            </section>
        </div>
        <div id="errorFetching">
            <div>
                <h4 class="text-center">{{this.errorMessage}}</h4>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
import avatar from '../../../components/avatarHolder.vue';
export default{
    name : "Child",
    created(){
        this.fetchStudent(this.$route.params.username).then(child =>{
            this.child = child;
            this.isLoading = false;
        }).catch(err => {
            this.isLoading = false;
            this.error_fetching = true;
            this.errorMessage = err.response.data.detail
        });
    },
    components:{
        avatar
    },
    data(){
        return {
            child:{},
            isLoading : true,
            error_fetching:false,
            errorMessage : ''
        }
    },
    computed:{

    },
    methods : {
        ...mapActions('student',[
            "fetchStudent"
        ])
    }

}
</script>
<style lang="stylus">
</style>

