<template>
    <div id="schoolDisplay" class="d-flex justify-content-lg-center">
        <div class="col-12 col-lg-10 col-xl-9 px-0 ">
            <div class="d-flex flex-wrap">
                <div class="col-12 col-lg-6 col-xl-5 px-lg-5 text-center">
                    <transition name="left-right" mode="out-in">
                        <div class="mx-auto w-75" v-if="isSchool">
                            <img :src="school.logo" :alt="school.name" class="rounded-circle image-fluid clickable"
                            @click="goToSchool">
                        </div>
                    </transition>
                </div>
                <div class="col-12 col-lg-6">
                    <transition name="fade" mode="out-in">
                        <div class="desc-pane" v-if="isSchool">
                            <div class="fade-logo d-none d-lg-block">
                                <h1 class="m-0 color_1 font-weight-bold text-uppercase"
                                    style="font-size:10rem;">KC {{nIndex}}</h1>
                            </div>
                            <div class="description pr-xl-5 py-3">
                                <h2 class="font-weight-bold d-none d-lg-block clickable" :style="{color : `${color}
                                    !important`}" @click="goToSchool">{{name}}</h2>
                                <h5 class="font-weight-bold d-lg-none" :style="{color : `${color} !important`}"
                                @click="goToSchool">{{name}}</h5>
                                <p class="color_4" >{{description}}</p>
                            </div>
                        </div>
                    </transition>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
export default{
    name : 'SchoolDisplay',
    props : ['school', 'index'],
    created(){
        this.preschool = this.school;
    },
    mounted(){
        let school = this.getSchool;
    },
    data(){
        return {
            preschool : '',
            animIndex : -1,
            animations : ['right', 'up', 'right', 'down','upright','right', 'downright']
        }
    },
    computed : {
        isSchool(){
           return  this.preschool.id === this.school.id; 
        },
        ...mapGetters('home',['getSchool']),
        color(){
            return this.school.color;
        },
        description(){
            return this.preschool.description;
        },
        name(){
            return this.preschool.name;
        },
        anim(){
            let school = this.school;

            this.animIndex = this.animIndex + 1 == this.animations.length ? 0 : this.animIndex + 1;
            return this.animations[this.animIndex];
        },
        nIndex(){
            return (Array(2).join("0") + (this.index + 1)).slice(-2);
        }
    },
    methods : {
        fillPad(num,len){
            return (Array(len).join("0") + num).slice(-len);
        },
        goToSchool(){
            this.$router.push({name:'kidkrumbsSchoolDetail', params:{id : this.school.id}});
        }
    },
    watch : {
        school(newVal, oldVal){
            setTimeout(() => {
                this.preschool = this.school;
            }, 500);
        }
    }
}
</script>
<style lang='stylus'>
#schoolDisplay
    transition all 0.4s ease-in-out
    .desc-pane
        .description
        .fade-logo
            position relative
            top 0
            left 0
            z-index 100
        .fade-logo
            top 100px
            z-index 10

    .left-right-enter-active
    .left-right-leave-active
    .right-enter-active
    .up-enter-active
    .down-enter-active
    .upright-enter-active
    .downright-enter-active
    .right-leave-active
    .up-leave-active
    .down-leave-active
    .upright-leave-active
    .downright-leave-active
        transition all 0.3s ease-in-out

    .right-enter
    .right-leave-to
        transform translateX(40px)
        opacity 0

    .left-right-enter
        transform translateX(40px)
        opacity 0
        
    .left-right-leave-to
        transform translateX(-40px)
        opacity 0

    .up-enter
    .up-leave-to
        transform translateY(-40px)
        opacity 0

    .upright-enter
    .upright-leave-to
        transform translate(40px, -40px)
        opacity 0

    .down-enter
    .down-leave-to
        transform translateY(40px)
        opacity 0

    .downright-enter
    .downright-leave-to
        transform translate(40px, 40px)
        opacity 0

</style>


