<template>
    <div id="schoolConcept" class="p-lg-4 p-xl-5">
        <div class="">
            <div class="d-flex flex-wrap ">
                <div class="col-lg-4 col-xl-3 col-12">
                    <p class="color_2 m-0 text-uppercase"><small class="color_3">more about us</small></p>
                    <transition name="fade-down" mode="out-in">
                    <h2 v-if="view=='about'" key="about" class="display- m-0 text-uppercase " :style="{color:`${school.color} !important`}">Our Concepts</h2>
                    <h2 v-else-if="view=='service'" key="service" class="display- m-0 text-uppercase " :style="{color:`${school.color} !important`}">Our Services</h2>
                    <h2 v-else class="display- m-0 text-uppercase " key="requirement" :style="{color:`${school.color} !important`}">Our
                        Requirements</h2>
                    </transition>
                </div>
            </div>
            <div class="d-flex align-items-center flex-wrap" style="min-height:85vh">
                <div class="col-lg-3"></div>
                <div class="col-lg">
                    <div class="text-center  my-4" >
                        <div class="d-inline-block clickable mr-3 text-center" @click="prevView">
                            <span class="fas fa-chevron-left fa-fw fa-2x" :style="{color:`${school.color} !important`}"></span>
                            <div>
                                <small class="color_2">previous</small>
                            </div>
                        </div>
                        <div class="d-inline-block clickable text-center" @click="nextView">
                            <span class="fas fa-chevron-right fa-fw fa-2x" :style="{color:`${school.color} !important`}"></span>
                            <div>
                                <small class="color_2">next</small>
                            </div>
                        </div>
                    </div>
                    <transition name="fade-right" mode="out-in">
                        <component :is="view" :school="school"></component>
                    </transition>
                    <div class="text-center my-3" >
                        <div class="d-inline-block clickable mr-3 text-center" @click="prevView">
                            <span class="fas fa-chevron-left fa-fw fa-2x" :style="{color:`${school.color} !important`}"></span>
                            <div>
                                <small class="color_2">previous</small>
                            </div>
                        </div>
                        <div class="d-inline-block clickable text-center" @click="nextView">
                            <span class="fas fa-chevron-right fa-fw fa-2x" :style="{color:`${school.color} !important`}"></span>
                            <div>
                                <small class="color_2">next</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
import about from './about-school.vue';
import service from './school-service.vue';
import requirement from './school-requirement.vue';
export default{
    name : "schoolConcept",
    props:['school'],
    computed:{
        hasServices(){
            return this.school.services.length > 0;
        },
        hasRequirements(){
            return this.school.requirements.length > 0;
        },
        views(){
            let _views = ['about'];
            if(this.hasServices) _views.push('service');
            if(this.hasRequirements) _views.push('requirement');
            return _views;
        },
    },
    data(){
        return {
            index : 0,
            view : 'about'
        }
    },
    methods:{
        nextView(){
            this.index = this.index == this.views.length - 1 ?  0 : this.index + 1
            this.view = this.views[this.index];
        },
        prevView(){
            this.index = this.index - 1 == 0 ?  this.views.length - 1 : this.index - 1
            this.view = this.views[this.index];
        }
    },
    components : {
        about,
        service,
        requirement
    }
}
</script>
<style lang="stylus">
</style>
