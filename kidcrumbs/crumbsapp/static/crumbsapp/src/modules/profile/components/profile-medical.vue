<template>
    <div id="profileMedical" class="" >
        <div v-if="profile.medical_info" >
            <h5 class="m-0"><strong>Medical</strong></h5>
            <hr>
            <section class="d-flex flex-wrap">
                <div class="py-1 col-12 px-0">
                    <p class="color_3 m-0"> Physician Name </p>
                    <p class="m-0">{{profile.medical_info.physician_name}}</p>
                </div>
                <div class="py-1 col-12 px-0">
                    <p class="color_3 m-0"> Phone Numbers </p>
                    <p class="m-0">{{profile.medical_info.mobile_numbers}}</p>
                </div>
                <div class="py-1 col-12 px-0">
                    <p class="color_3 m-0"> Allergies </p>
                    <p class="m-0" v-if="profile.medical_info.allergies">{{profile.medical_info.allergies}}</p>
                    <p class="m-0" v-else>None</p>
                </div>
                <div class="py-1 col-12 px-0" >
                    <p class="color_3 m-0"> Medications </p>
                    <p class="m-0" v-if="profile.medical_info.medications">{{profile.medical_info.medications}}</p>
                    <p class="m-0">None</p>
                </div>
            </section>
        </div>
        <div v-else class="d-flex justify-content-center align-items-center" > 
            <div class="text-center col-auto py-4">
                <h3 class="color_3 text-uppercase">No Medical Information</h3>
                <h1 class="display-4 color_2"><i class="fas fa-tint-slash fa-2x"></i></h1>
                <h6 class="color_3 text-upperase" style="line-height : 1.3em !important"><span class="text-uppercase">{{profile.names}}</span> <br/> does not have any medical information </h6>
            </div>
        </div>
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
<style lang="stylus">
#profileContact
    .no-contact
        min-height 40vh 

</style>
