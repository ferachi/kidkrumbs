<template>
    <div class="avatar-case">
        <div v-if="image" class="image px-2">
            <md-avatar :class="mdSize">
                <img :src="image" :alt="alt" class="img-fluid" >
            </md-avatar>
        </div>
        <div v-else class="image d-flex align-items-center justify-content-center">
            <md-avatar classs="md-avatar-icon" :class="mdSize">
                <md-icon class="fas fa-fw fa-user-circle" :class="{'md-size-3x':size=='large',
                'md-size-2x':size=='normal'}"></md-icon>
            </md-avatar>
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
        size : {
            type : String,
            default : "normal"
        },
    },
    computed : {
        mdSize(){
            let size = '';
            switch(this.size) {
                case 'small':
                    size = "md-small";
                    break;
                case 'large':
                    size = 'md-large';
                    break;
                default :
                    size = '';
            }
            return size;
        }
    }
}
</script>
<style lang="stylus" scoped>
</style>
