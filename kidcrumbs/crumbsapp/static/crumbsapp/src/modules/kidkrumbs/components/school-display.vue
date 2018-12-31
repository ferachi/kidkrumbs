<template>
    <div id="schoolDisplay" class="h-100 d-flex flex-wrap p-3" :style="{background:color}" >
        <div class="col-12 col-lg-8 order-lg-1 h-100 px-0">
            <div class="d-flex flex-wrap h-100 align-items-center">
                <div class="col-12 col-lg px-0 order-lg-1 text-center">
                    <transition :name="anim" mode="out-in">
                        <div class="icon-pane" v-if="isSchool">
                            <h1 class="display-2" v-html="icon"></h1>
                        </div>
                    </transition>
                </div>
                <div class="col-12 col-lg px-0 order-lg-0">
                    <transition name="fade" mode="out-in">
                        <div class="desc-pane" v-if="isSchool">
                            <h4 class="font-weight-bold color_black">{{name}}</h4>
                            <p class="color_black">{{description}}</p>
                        </div>
                    </transition>
                </div>
            </div>
        </div>
        <div class="col-lg order-lg-0">
        </div>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
export default{
    name : 'SchoolDisplay',
    props : ['school'],
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
            return this.preschool.brief_description;
        },
        name(){
            return this.preschool.name;
        },
        anim(){
            let school = this.school;
            //animIndex = _.random(0, animations.length-1);

            this.animIndex = this.animIndex + 1 == this.animations.length ? 0 : this.animIndex + 1;
            return this.animations[this.animIndex];
        },
        icon(){
            return `<div class="fa-2x color_white"><span class="fa-layers fa-fw">
                <span class="fas fa-pencil-ruler" data-fa-transform="shrink-4"></span>
                <span class="far fa-circle" data-fa-transform="grow-10"></span>
                </span> </div>`;
        }
    },
    methods : {
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
    width 100vw
    overflow-y auto
    overflow-x hidden
    transition background 0.4s ease-in-out

    .right-enter-active
    .up-enter-active
    .down-enter-active
    .upright-enter-active
    .downright-enter-active
        transition all 0.5s

    .right-enter
    .right-leave-to
        transform translateX(40px)
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


