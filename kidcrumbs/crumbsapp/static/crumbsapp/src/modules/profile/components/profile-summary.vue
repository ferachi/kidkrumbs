<template>
    <div id="profileSummary" class="d-flex align-items-stretch flex-wrap">
        <div class=" mb-1 col-12 col-lg-6 d-flex px-1">
            <div class="col bg_0 h-100 border border_1 p-5 d-flex align-items-center">
                <div class="col">

                    <h5 class="m-0 color_3">{{profile.title}}</h5>
                    <h2 class="font-weight-bold m-0">{{profile.names}}</h2>        
                    <p class="m-0">{{profile.description}}</p>
                    <p class="m-0">{{birthDate}}</p>
                    <hr>
                </div>
            </div>
        </div>

        <div class="col-12 col-lg-6 px-1">
            <div class="bg_0 border border_1 p-2 ">
                <div class="py-2">
                    <h6 class="color_3 m-0 ">About me</h6>
                    <hr class="my-1">
                    <div class="py-1">
                        <p class="color_3 m-0"> names </p>
                        <p class="m-0">{{profile.names}}</p>
                    </div>
                    <div class="py-1">
                        <p class="color_3 m-0"> birth date </p>
                        <p class="m-0">{{birthDate}}</p>
                    </div>

                    <!-- <div class="d&#45;flex flex&#45;wrap"> -->
                    <!--     <div class="col&#45;3 px&#45;0"><p class="m&#45;0 text&#45;right color_3">username</p></div> -->
                    <!--     <div class="col&#45;9"><p class="m&#45;0">{{profile.username}}</p></div> -->
                    <!--     <div class="col&#45;3 px&#45;0"><p class="m&#45;0 text&#45;right color_3">first name</p></div> -->
                    <!--     <div class="col&#45;9"><p class="m&#45;0">{{profile.first_name}}</p></div> -->
                    <!--     <div class="col&#45;3 px&#45;0"><p class="m&#45;0 text&#45;right color_3">last name</p></div> -->
                    <!--     <div class="col&#45;9"><p class="m&#45;0">{{profile.last_name}}</p></div> -->
                    <!--     <div class="col&#45;3 px&#45;0"><p class="m&#45;0 text&#45;right color_3">email</p></div> -->
                    <!--     <div class="col&#45;9"><p class="m&#45;0">{{profile.email}}</p></div> -->
                    <!-- </div> -->
                </div>
                <div class="py-2">
                    <h6 class="color_3 m-0">Contact me</h6>
                    <hr class="my-1">
                    <div class="py-1">
                        <p class="color_3 m-0"> email </p>
                        <p class="m-0">{{profile.email}}</p>
                    </div>
                    <div class="py-1">
                        <p class="color_3 m-0"> birth date </p>
                        <p class="m-0">{{birthDate}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : "ProfileDetail",
    props : ['profile'],
    computed : {
        birthDate(){
            return moment(this.profile.dob).format("Do MMMM, YYYY");
        }
    }

}
</script>
<style lang="stylus"></style>
