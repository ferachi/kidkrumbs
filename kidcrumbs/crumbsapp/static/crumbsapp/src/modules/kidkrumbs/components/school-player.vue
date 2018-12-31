<template>
    <div id="schoolPlayer" class="p-2">
        <div class="d-none d-lg-block">
            <transition-group name="play-list" tag="div">
                <div v-for="school in playList" :key="school.id" class="schools">
                    <school :school="school"></school>
                </div>
            </transition-group>
        </div>
        <div class="px-xl-5 d-flex align-items-center">
            <div class="col-auto px-1">
                <div class="clickable">
                    <transition-group name="logo-list" tag="div">
                        <div v-for="school in playList" :key="school.id" class="schools">
                            <avatar :image="school.logo" size="large"></avatar>
                        </div>
                    </transition-group>
                </div>
            </div>
            <div class="controls col-auto d-flex px-0 align-items-end">
                <!-- <div class="col&#45;auto px&#45;2"> -->
                <!--     <div class="clickable d&#45;inline&#45;block"> -->
                <!--         <span class="fa&#45;layers fa&#45;fw fa&#45;2x color_black"> -->
                <!--             <span class="fas fa&#45;circle" data&#45;fa&#45;transform="grow&#45;6"></span> -->
                <!--             <span class="fas fa&#45;play fa&#45;inverse" data&#45;fa&#45;transform="shrink&#45;6"></span> -->
                <!--         </span> -->
                <!--     </div> -->
                <!-- </div> -->
                <div class="col-auto px-2">
                    <div class="clickable d-inline-block" @click="previous">
                        <span class="fas fa-angle-left fa-2x color_black"></span>
                    </div>
                </div>
                <div class="col-auto px-2">
                    <div class="clickable d-inline-block " @click="next">
                        <span class="fas fa-angle-right fa-2x color_black"></span>
                        <!-- <span class="fa&#45;layers fa&#45;fw fa&#45;lg color_black "> -->
                        <!--     <span class="fas fa&#45;circle" data&#45;fa&#45;transform="grow&#45;6"></span> -->
                        <!--     <span class="fas fa&#45;step&#45;forward fa&#45;inverse" data&#45;fa&#45;transform="shrink&#45;6"></span> -->
                        <!-- </span> -->
                    </div>
                </div>
                <div class="col-auto px-2">
                    <div class="clickable d-inline-block">
                        <span class="fas fa-glasses fa-2x color_black"></span>
                    </div>
                </div>
            </div>
            <hr class="border_1 border-width-3">
        </div>
    </div>
</template>
<script>
import school from './school-item';
import avatar from '../../../components/avatar.vue';
export default{
    name : 'SchoolPlayer',
    created(){
        this.index = 0;
        this.changeIndex();
        this.play();
    },
    props : {
        schools :{
            type : Array,
            required : true
        },
        speed : {
            type : Number,
            default : 5000
        }
    },
    computed : {
    },
    methods:{
        previous(){
            this.index = this.index == 0 ? this.schools.length - 1 : this.index - 1;
            this.timer();
        },
        next(){
            this.index = this.index + 1 == this.schools.length ? 0 : this.index + 1;
            this.timer();
        },
        timer(){
            this.clearTimer();
            let _timer = setTimeout(() => { this.play(); clearTimeout(_timer); });
        },
        clearTimer(){
            clearInterval(this.timeId);
        },
        play(){
            this.timeId = setInterval( () => {
                this.index = this.index + 1 == this.schools.length ? 0 : this.index + 1;
            },this.speed);
        },
        changeIndex(){
            let school =  this.schools[this.index];
            this.$emit('school-change', school);
            this.playList.unshift(school);
            this.playList.pop();
        }
    },
    data(){
        return{
            playList : [{}],
            index : 0,
            timeId : 0,
        }
    },
    components : {
        school,
        avatar
    },
    watch:{
        index(newVal, oldVal){
            this.changeIndex();
        }
    }
}
</script>
<style lang='stylus'>
#schoolPlayer
    .schools
        transition: all 0.6s;
        display : inline-block
        width : 100%
        margin-right: 10px

    .play-list-enter
        opacity 0
        transform translateX(-30px)

     .play-list-leave-to
        opacity 0
        transform translateX(30px)

    .play-list-enter-active, .logo-list-enter-active
        transition-delay .4s

    .logo-list-enter, .logo-list-leave-to
        opacity 0

    .play-list-leave-active,.logo-list-leave-active
        position absolute
</style>

