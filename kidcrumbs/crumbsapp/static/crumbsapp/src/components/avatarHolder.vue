<template>
    <div class="avatar-holder">
        <div v-if="image" class="image">
            <img :src="image" :alt="alt" class="img-fluid" :class="{'rounded-circle':rounded}">
        </div>
        <div v-else class="image d-flex align-items-center justify-content-center" :class="{'bg_1':showBg}">
            <p class="color_5" v-if="rounded"><i class="fas fa-user-circle fa-7x fa-fw"></i></p>
            <p class="color_5" v-else><i class="fas fa-user fa-7x fa-fw"></i></p>
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
        }
    }
}
</script>
<style lang="stylus" scoped>
</style>
