<template>
    <div id="ProfileDetail">
        <div class="text-center">
            <div class="p-3">
                <avatar :image="profile.avatar" :alt="profile.names" size="large"></avatar>
            </div>
            <div>
                <h6 class="m-0 color_3">{{profile.title}}</h6>
                <h4 class="font-weight-bld text-capitalize">{{names}}</h4>        
                <p class="m-0 color_3">{{profile.description}}</p>
            </div>
        </div>
        <hr>
        <section class="sub-views">
            <tabHead :tabTitles="tabs" @tab-click="tabClicked($event)" justify="justify-content-around">
                <div slot="tab" slot-scope="{tab}" class="text-center clickable">
                    <p class="color_5 m-0" :class="{'primary-color':tab.isActive}"><i :class="tab.icon"></i></p>
                    <p><small class="color_5 m-0" :class="{'primary-color':tab.isActive}">{{tab.name}}</small></p>
                </div>
            </tabHead>
        </section>
        <hr class="mt-0"/>
        <section class="p-2 px-lg-3 px-xl-5">
            <transition name="fade-right" mode="out-in">
                <keep-alive>
                    <component :is="currentTab" :profile="profile"></component>
                </keep-alive>
            </transition>
        </section>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import avatar from '../../../components/avatar.vue';
import tabHead from '../../../components/tabHead.vue';
import aboutProfile from '../components/about-profile.vue';
import profileContact from '../components/profile-contact.vue';
import profileRelatives from '../components/profile-relatives.vue';
import profileMedical from '../components/profile-medical.vue';
const tabs = [
    { name : 'about', icon : 'fas fa-user fa-fw', isActive:false},
    { name : 'contact', icon : 'fas fa-mobile-alt fa-fw', isActive : false},
    { name : 'relatives', icon : 'fas fa-users fa-fw', isActive : false},
    { name : 'medical', icon : 'fas fa-medkit fa-fw', isActive : false},
]
export default{
    name : "ProfileDetail",
    created(){
        _.forEach(this.tabs, tab =>{
            tab.isActive = false;
        });
        if(this.tabs.length > 0){
            this.setTab = tabs[0].name;
            this.tabs[0].isActive = true;
        }
    },
    computed : {
        ...mapGetters('person' , { profile : 'getProfile' }),
        names(){
            let other_names = this.profile.other_names.split(/\s+/g).map(x => x.charAt(0)).join('. '),
                first_name = this.profile.first_name,
                last_name = this.profile.last_name;
            return !!other_names ? `${last_name} ${other_names} ${first_name}` : `${last_name} ${first_name}`
        },
        currentTab(){
            return this.setTab;
        }
    },
    components :{
        avatar,
        tabHead,
        about : aboutProfile,
        contact : profileContact,
        relatives : profileRelatives,
        medical : profileMedical,
    },
    data(){
        return {
            tabs,
            setTab :null
        }
    },
    methods : {
        tabClicked(tab){
            this.setTab = tab;
        }
    }
}
</script>
<style lang="stylus">
</style>
