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
                            <router-link class="col p-0 py-3 m-0 text-center color_0" :to="{name:'activityDetailByDate',
                            params:{date:date}}"><small class="color_0">Activity</small></router-link>
                        <router-link class="col p-0 text-center color_0" :to="{name:'childBehaviour', params:{date:date}}"><small class="color_0">Behaviour</small></router-link>
                        <router-link class="col p-0 text-center color_0" :to="{name:'childHomework', params:{id:1}}"><small class="color_0">Homework</small></router-link>
                        <router-link class="col p-0 text-center color_0" :to="{name:'more'}"><small class="color_0">More</small></router-link>
                        </div>
                    </div>
                </section>
            </div>
            <section id="childContent" class="p-2 ">
                <router-view></router-view>
            </section>
            <section id="errorFetching">
                <div>
                    <h4 class="text-center">{{this.errorMessage}}</h4>
                </div>
            </section>
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
            let group = this.getCurrentClassroom
            let habits = this.fetchChildHabitsByGroup(group.id),
                groupHabits = this.fetchGroupHabits(group.id),
                activities = this.fetchActivities(group.id);
            
            // get the groups activities
            Promise.all([habits,groupHabits, activities]).then( props => {
                this.child = child;
                this.isLoading = false;
            })

        }).catch(err => {
            console.log(err);
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
            date : moment().format("YYYY-MM-DD"),
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
            "fetchChildHabitsByGroup",
            "fetchChildWithProps"
        ]),
        ...mapActions('group',[
            "fetchGroupHabits"
        ]),
        ...mapMutations("group", [
            "setGroup"
        ]), 
        ...mapActions('activity', {
            fetchActivities : "pullActivities"
        })
    }

}
</script>
<style lang="stylus">
#child
    #childContent
        min-height 70vh
</style>

