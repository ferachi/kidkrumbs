<template>
    <div id="profileSummary" class="">
        <section class="d-flex align-items-stretch flex-wrap">
        <div class=" mb-1 col-12 d-flex px-1">
            <div class="col bg_0 h-100 border border_1 p-5 d-flex align-items-center">
                <div class="col text-center">
                    <div>
                        <avatar :image="profile.avatar" :alt="profile.names" size="large"></avatar>
                    </div>
                    <hr>
                    <div>
                        <h5 class="m-0 color_3">{{profile.title}}</h5>
                        <h4 class="font-weight-bold ">{{names}}</h4>        
                        <p class="m-0">{{profile.description}}</p>
                        <p class="color_3">{{birthDate}}</p>
                    </div>
                    <hr>
                </div>
            </div>
        </div>
        <div class="col-12 px-1">
            <div class="bg_0 border border_1 p-2 h-100">
                <div class="py-2">
                    <h6 class="color_4 m-0"><strong>About me</strong></h6>
                    <hr class="my-1">
                    <div class="py-1">
                        <p class="color_3 m-0"> Names </p>
                        <p class="m-0">{{profile.names}}</p>
                    </div>
                    <div class="py-1">
                        <p class="color_3 m-0"> Birth Date </p>
                        <p class="m-0">{{birthDate}}</p>
                    </div>
                    <div class="py-1">
                        <p class="color_3 m-0"> Gender </p>
                        <p class="m-0">{{gender}}</p>
                    </div>
                    <div class="py-1" v-if="profile.hobbies">
                        <p class="color_3 m-0"> Hobbies </p>
                        <p class="m-0">{{profile.hobbies}}</p>
                    </div>
                </div>
                <div class="py-2" v-if="profile.contact">
                    <h6 class="color_4 m-0"><strong>Contact me</strong></h6>
                    <hr class="my-1">
                    <div class="py-1">
                        <p class="color_3 m-0"> email </p>
                        <p class="m-0">{{profile.email}}</p>
                    </div>
                    <div class="py-1">
                        <p class="color_3 m-0"> telephone numbers </p>
                        <p class="m-0">{{numbers}}</p>
                    </div>
                </div>
            </div>
        </div>
        </section>
        <section class="d-flex flex-wrap py-1">
            <div class="col-12 px-1">
                <div class="bg_0 border border_1 p-2 h-100">
                    <h6 class="color_4 m-0"><strong>Medical Information</strong></h6>
                    <hr>
                    <div v-if="profile.medical_info">
                        <div class="py-1">
                            <p class="color_3 m-0"> Physician Name </p>
                            <p class="m-0">{{profile.medical_info.physician_name}}</p>
                        </div>
                        <div class="py-1" >
                            <p class="color_3 m-0"> Phone Numbers </p>
                            <p class="m-0">{{profile.medical_info.mobile_numbers}}</p>
                        </div>
                        <div class="py-1" v-if="profile.medical_info.allergies">
                            <p class="color_3 m-0"> Allergies </p>
                            <p class="m-0">{{profile.medical_info.allergies}}</p>
                        </div>
                        <div class="py-1" v-if="profile.medical_info.medications">
                            <p class="color_3 m-0"> Medications </p>
                            <p class="m-0">{{profile.medical_info.medications}}</p>
                        </div>
                    </div>
                    <div v-else class="no-medical text-center d-flex justify-content-center align-items-center"
                        style="height:200px;">
                       <h1 class="color_3">No Medical Information</h1>
                    </div>
                </div>
            </div>
            <div class="col-12 px-1 py-1">
                <div class="bg_0 border border_1 p-2 h-100">
                    <h6 class="color_4 m-0"><strong>Relatives</strong></h6>
                    <hr>
                    <div class="d-flex flex-wrap" v-if="profile.relatives.length > 0">
                        <div v-for="relative in profile.relatives" class="col-6 px-1 text-center py-2 clickable"
                        :key="relative.user" @click="relativeClicked(relative)">
                            <avatar :image="relative.avatar" :alt="relative.names"></avatar>
                            <h6><small class="font-weight-bold color_5">{{relative.last_name}}
                                    {{relative.first_name}}</small> <br/> <small class="color_3">{{relative.relation.relationship}}</small></h6>
                        </div>
                    </div>
                    <div v-else class="no-relatives text-center d-flex justify-content-center align-items-center"
                        style="height:200px;">
                       <h1 class="color_3">No Relatives</h1>
                    </div>
                </div>
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
