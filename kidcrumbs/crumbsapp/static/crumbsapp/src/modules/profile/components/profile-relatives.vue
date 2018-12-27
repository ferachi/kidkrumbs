<template>
    <div id="profileRelatives" class="">
        <section class="" v-if="profile.relatives.length > 0">
            <h5 class="m-0"><strong>Relatives</strong></h5>
            <hr>
            <div class="d-flex flex-wrap" >
                <div v-for="relative in profile.relatives" class="col-6 col-lg-4 px-1 text-center py-2 clickable"
                                                           :key="relative.user" @click="relativeClicked(relative)">
                    <avatar :image="relative.avatar" :alt="relative.names" ></avatar>
                    <h6><small class="font-weight-bold color_5">{{relative.last_name}}
                            {{relative.first_name}}</small> <br/> <small class="color_3">{{relative.relation.relationship}}</small></h6>
                </div>
            </div>
        </section>
        <section v-else class="text-center d-flex justify-content-center align-items-center" >
            <div class=" text-center col-auto py-4">
                <h3 class="color_3 text-uppercase">No Relatives</h3>
                <h1 class="display-4 color_2"><i class="fas fa-user-alt-slash fa-2x"></i></h1>
                <h6 class="color_3 text-upperase" style="line-height : 1.3em !important"><span
                                                  class="text-uppercase">{{profile.names}}</span> <br/> does not have any relatives </h6>
            </div>
        </section>
        <section class="relative-contact">
            <modal ref="modal" :enable-mobile-fullscreen="false" :modal-theme="getTheme" :overlay-theme="getTheme" class="px-0">
            <div class="d-flex justify-content-center"  v-if="relative">
                <div class="col px-0 col-lg-10 py-2 text-left text-center">
                    <avatar :image="relative.avatar" :alt="relative.names" size="large"></avatar>
                    <h6 class="font-weight-bold mt-2 mb-0">{{relative.names}}</h6>
                    <p class="m-0"> <span class="color_3">{{relative.relation.relationship}}</span></p>
                    <div >
                        <div class="mt-4">
                            <p class="color_3 m-0">Email</p>
                            <p class="color_5">{{relative.email}}</p>
                        </div>
                        <div v-if="relative.contact" class="mt-4">
                            <p class="color_3 m-0">Numbers</p>
                            <p class="color_5 m-0">{{phoneNumbers(relative)}}</p>
                        </div>
                    </div>
                </div>
            </div>
            </modal>
        </section>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import avatar from '../../../components/avatar.vue';
import { SweetModal } from 'sweet-modal-vue';
export default{
    name : "ProfileDetail",
    props : ['profile'],
    computed : {
        ...mapGetters(['getTheme']),
        birthDate(){
            return moment(this.profile.dob).format("Do MMMM, YYYY");
        },
        gender(){
            return this.profile.gender.toLowerCase() == 'male' ? 'Male' : 'Female';
        },
        names(){
            let other_names = this.profile.other_names.split(/\s+/g).map(x => x.charAt(0)).join('. '),
                first_name = this.profile.first_name,
                last_name = this.profile.last_name;
            return !!other_names ? `${last_name} ${other_names} ${first_name}` : `${last_name} ${first_name}`
        },
        numbers(){
            let contact = this.profile.contact,
                _numbers = _.compact([contact.mobile_number, contact.mobile_number_two, contact.home_number,
                contact.office_number]).join(", ");
            return _numbers;
        }
    },
    components : {
        avatar,
        modal:SweetModal
    },
    data(){
        return {
            relative : null,
        }
    },
    methods :{
        relativeClicked(relative){
            this.relative = relative;
            this.show();
        },
        phoneNumbers(person){
            let contact = person.contact,
                _numbers = _.compact([contact.mobile_number, contact.mobile_number_two, contact.home_number,
                contact.office_number]).join(", ");
            return _numbers;
        },
        show () {
            this.$refs.modal.open(); 
        },
        hide () {
            this.$refs.modal.close(); 
        },
    }
}
</script>
<style lang="stylus"></style>
