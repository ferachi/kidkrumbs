<template>
    <div id="child" class="">
        <div v-if="isLoading" class="" key="loading">
        </div>
        <div id="child" v-else key="loaded">
            <page>
            <div slot="header">
                <section class="page-header primary-bg d-flex flex-wrap justify-content-center">
                    <div class="col-xl-8 col px-0">
                        <div class="d-flex align-items-center">
                            <div class="col-xl-2 col">
                                <avatar :image="child.avatar" class="p-2" :rounded="true" >
                                </avatar>
                            </div>
                            <div class="col-8">
                                <h4 class="color_0 m-0">{{child.names}}</h4>
                                <router-link class="m-0 color_0" :to="{name:'childHomework', params:{id:1}}"><small
                                             class="color_0">view profile</small></router-link>
                            </div>
                        </div>
                        <div class="d-flex align-items-center  col-12 justify-content-around">
                            <router-link class="col p-0 py-3 m-0 text-center color_0" :to="{name:'childActivity',
                            params:{id:activityId}}"><small class="color_0">Activity</small></router-link>
                        <router-link class="col p-0 text-center color_0" :to="{name:'childBehaviour', params:{id:1}}"><small class="color_0">Behaviour</small></router-link>
                        <router-link class="col p-0 text-center color_0" :to="{name:'childHomework', params:{id:1}}"><small class="color_0">Homework</small></router-link>
                        <router-link class="col p-0 text-center color_0" :to="{name:'app'}"><small class="color_0">More</small></router-link>
                        </div>
                    </div>
                </section>
            </div>
            <div id="childContent">
                <section class="p-2">
                    <router-view></router-view>
                </section>
            </div>
            <div id="errorFetching">
                <div>
                    <h4 class="text-center">{{this.errorMessage}}</h4>
                </div>
            </div>
            </page>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import avatar from '../../../components/avatarHolder.vue';
import page from '../../../components/page.vue';
export default{
    name : "Child",
    created(){
        this.fetchChildWithProps(this.$route.params.username).then(child =>{

            // SET GROUP

            // TODO : This will be called on every refresh
            // this means the group will always be reset 
            // to current classroom when the browser is refreshed
            this.setGroup(this.getCurrentClassroom);


            // SETUP ALL GROUP RELATED MODELS

            // get the groups activities
            this.fetchActivities(this.getCurrentClassroom.id).then( activities => {
                this.child = child;
                this.activityId = this.getCurrentActivity.id;
                this.$router.push({name:"childActivity", params:{id:this.activityId}});
                this.isLoading = false;
            })

        }).catch(err => {
            this.isLoading = false;
            this.error_fetching = true;
            this.errorMessage = err.response.data.detail
        });
    },
    components:{
        avatar,
            page
    },
    data(){
        return {
            child:{},
            activityId: 0,
            isLoading : true,
            error_fetching:false,
            errorMessage : ''
        }
    },
    computed:{
        ...mapGetters('child', [
            'getCurrentClassroom'
        ]),
            ...mapGetters('activity', [
                'getCurrentActivity'
            ])
    },
    methods : {
        ...mapActions('child',[
            "fetchChild",
            "fetchChildWithProps"
        ]),
            ...mapMutations("child", [
                "setGroup"
            ]), 
            ...mapActions('activity', {
                fetchActivities : "pullActivities"
            })

    }

}
</script>
<style lang="stylus">
</style>

