<template>
    <div id="schoolContact" class="bg_aux">
        <div class="d-flex flex-wrap align-items-center justify-content-center">
            <div class="d-flex flex-wrap col-lg-10 px-0 align-items-center justify-content-between">
                <div class="col-lg-8 ">
                    <h1 class="display- font-weight-bold">Contact us</h1>
                    <div class="d-flex flex-wrap ">
                        <div class="col-lg py-3">
                            <p class="m-0 color_3">
                                Address
                            </p>
                            <p class="m-0" v-for="address in addresses">
                                <small class="color_5">{{address}}</small>
                            </p>
                        </div>
                        <div class="col-lg py-3">
                            <p class=" m-0 color_3">
                                Phones
                            </p>
                            <p class="m-0" v-for="phone in phones">
                                <small class="color_5">{{phone}}</small>
                            </p>
                        </div>
                        <div class="col-lg py-3">
                            <p class=" m-0 color_3">
                                Email
                            </p>
                            <p class="m-0">
                                <small class="color_5">{{contact.email}}</small>
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-auto" v-if="socials.length > 0">
                    <h6 class="font-weight-bold text-uppercase" >SOCIALS</h6>
                    <div class="d-flex">
                        <div class="col-auto px-0 pr-3 " v-for="social in socials" @click="socialClicked(social.link)">
                            <span v-html="social.icon" :style="{color : `${school.color} !important`}" class="clickable"></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
export default{
    name : "SchoolHome",
    props:['school'],
    computed : {
        contact(){
            return this.school.contact;
        },
        phones(){
            let contact = this.contact;
            return _.compact([contact.phone_number,contact.phone_number2, contact.phone_number3]);
        },
        addresses(){
            let contact = this.contact;
            return _.compact([contact.address,contact.city, `${contact.state}, ${contact.country}`]);
        },
        socials(){
            let contact=this.contact,
                contacts = [
                    {
                        link : contact.googleplus_link,
                        icon : `<span class="fab fa-2x fa-google-plus-square fa-fw"></span>`
                    },
                    {
                        link : contact.facebook_link,
                        icon : `<span class="fab fa-2x fa-facebook-square fa-fw"></span>`
                    },
                    {
                        link : contact.instagram_link,
                        icon : `<span class="fab fa-2x fa-instagram fa-fw"></span>`
                    },
                    {
                        link : contact.website,
                        icon : `<span class="fas fa-2x fa-globe fa-fw"></span>`
                    },
                ]
            contacts = _.filter(contacts,_contact => !!_contact.link);
            return contacts;
        }
    },
    methods : {
        socialClicked( link){
            window.location = link;
        }
    }
}
</script>
<style lang="stylus">
#schoolContact
    >div
        min-height 85vh
</style>
