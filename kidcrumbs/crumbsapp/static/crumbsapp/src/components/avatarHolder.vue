<template>
    <div class="avatar-holder">
        <div v-if="image" class="image">
            <img :src="image" :alt="alt" class="img-fluid" :class="{'rounded-circle':rounded}">
        </div>
        <div v-else class="image d-flex align-items-center justify-content-center" :class="{'grey_bg_2':showBg}">
            <p class="grey_5" v-if="rounded"><i class="fas fa-user-circle fa-fw" :class="size"></i></p>
            <p class="grey_5" v-else><i class="fas fa-user fa-fw" :class"size"></i></p>
        </div>
    </div>
</template>
<script>
export default {
    name: "",
    mounted() {
        let $image = $(".avatar-holder .image");
        $image.css('height', $image.css('width'));
    },
    props:{
        image:{
            type:String,
            default:''
        },
        alt:{
            type:String,
            default:''
        },
        rounded:{
            type:Boolean,
            default:false
        },
        showBg:{
            type:Boolean,
            default : true
        },
        size : {
            type : String,
            default : "fa-5x"
        }
    }
}
</script>
<style lang="stylus" scoped>
</style>
