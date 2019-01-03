<template>
    <transicion :isLoading="isLoading">
    <div id="Profile" class="" >
        <page>
        <section slot="header">
            <page-header class="border-bottom border_1 primary-bg" >
                <div slot="pageTitle" class="d-flex align-items-center mb-2">
                    <div class="col-auto px-1">
                        <avatar :image="profile.avatar" :alt="profile.username" > </avatar>
                    </div>
                    <div class="col px-2">
                        <h5 class="color_white m-0 text-capitalize">{{profile.last_name}} {{profile.first_name}}</h5>
                    </div>
                </div>
                <div slot="pageMenu">
                    <div class="d-flex">
                        <div class="col-auto px-2 clickable" @click="showProfile" v-if="isEdit" v-html="profileIcon"></div>
                        <div class="col-auto px-2 clickable" @click="editProfile" v-else v-html="profileIcon"></div>
                        <div class="col-auto px-2 clickable" @click="signOut"><span class="fas fa-sign-out-alt fa-fw color_white"></span></div>
                    </div>
                </div>
            </page-header>
        </section>
        <section id="profileContent" class="p-3 bg_0">
                <transition name="fade-down-up" mode="out-in">
                    <router-view></router-view>
                </transition>
        </section>
        <section id="errorFetching">
            <div>
                <h4 class="text-center">{{this.errorMessage}}</h4>
            </div>
        </section>
        </page>
    </div>
    </transicion>
</template>
<script>
import transicion from '../../../components/transicion.vue';
import avatar from '../../../components/avatar.vue';
import page from '../../../components/page.vue';
import pageHeader from '../../../components/pageHeader.vue';
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "Profile",
    created(){
        this.fetchData();
    },
    components:{
        page,
        pageHeader,
        transicion,
        avatar
    },
    computed :{
        ...mapGetters('profile', [ 'getProfile' ]),
        ...mapGetters('person', {profile : 'getProfile' }),
        isEdit(){
            return this.$route.name != 'profile';
        },
        profileIcon (){
            return this.isEdit ? `<span class="fas fa-user fa-fw color_white"></span>` : `<span class="fas fa-fw fa-edit color_white"></span>` ;
        }
    },
    data(){
        return {
            isLoading  : true,
            error_fetching:false,
            errorMessage : '',
        }
    },
    methods : {
        ...mapActions('person', ['fetchProfile']),
        ...mapActions('auth', ['logout']),
        fetchData(){
            this.fetchProfile(this.getProfile.username).then(profile =>{
                this.isLoading = false; 
            }).catch(err => {
                this.isLoading = false;
                this.error_fetching = true;
                this.errorMessage = err.response.data.detail
            });
        },
        showProfile(){
            this.$router.push({name : 'profile'});
        },
        editProfile(){
            this.$router.push({name : 'profileEdit'});
        },
        signOut(){
            this.logout().then( response => {
                this.$router.push({name : 'app'});   
            });
        }
    }
}
</script>
<style lang="stylus">
#Profile
    #profileContent
        min-height 90vh
        padding-bottom 100px !important
</style>
