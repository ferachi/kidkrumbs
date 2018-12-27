<template>
    <div id="aboutProfile" class="">
        <h5 class="m-0"><strong>About me</strong></h5>
        <hr>
        <section class="d-flex flex-wrap">
            <div class="py-1 col-6 px-0">
                <p class="color_3 m-0"> First Name </p>
                <p class="m-0 text-capitalize">{{profile.first_name}}</p>
            </div>
            <div class="py-1 col-6">
                <p class="color_3 m-0"> Last Name </p>
                <p class="m-0 text-capitalize">{{profile.last_name}}</p>
            </div>
            <div class="py-1 col-12 px-0" v-if="profile.other_names">
                <p class="color_3 m-0"> Other Names </p>
                <p class="m-0 text-capitalize">{{profile.other_names}}</p>
            </div>
        </section>
        <hr>
        <section class="d-flex flex-wrap">
            <div class="py-2 col-6 px-0">
                <p class="color_3 m-0"> Gender </p>
                <p class="m-0">{{gender}}</p>
            </div>
            <div class="py-2 col-6 px-0">
                <p class="color_3 m-0"> Birth Date </p>
                <p class="m-0">{{birthDate}}</p>
            </div>
            <div class="py-2 col-6 px-0" v-if="profile.occupation">
                <p class="color_3 m-0"> Occupation </p>
                <p class="m-0">{{profile.occupation}}</p>
            </div>
            <div class="py-2 col-6 px-0" v-if="profile.qualifications">
                <p class="color_3 m-0"> Qualifications </p>
                <p class="m-0">{{profile.qualifications}}</p>
            </div>
            <div class="py-2 col-12 px-0" v-if="profile.hobbies">
                <p class="color_3 m-0"> Hobbies </p>
                <p class="m-0">{{profile.hobbies}}</p>
            </div>
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
