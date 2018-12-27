<template>
    <div id="basicEdit">
        <div class="form-group">
            <imageUploader v-model="profile.avatar"></imageUploader>
        </div>
        <div class="form-group ">
            <md-field class="mb-0">
                <label>Brief Description</label>
                <md-textarea md-autogrow name="description" v-validate="{max:60, regex:/^(?!.*[^a-zA-Z0-9|^\s]).*$/}" v-model="profile.description"></md-textarea>
            </md-field>
                <span v-show="errors.has('description')" class="text-danger">{{ errors.first('description') }}</span>
        </div>
        <div class="form-group ">
            <md-field class="mb-0">
                <label>Hobbies </label>
                <md-textarea md-autogrow name="hobbies" v-validate="{max:60, regex:/^(?!.*[^a-zA-Z0-9|^\s|^,]).*$/}" v-model="profile.hobbies"></md-textarea>
            </md-field>
                <span v-show="errors.has('hobbies')" class="text-danger">{{ errors.first('hobbies') }}</span>
        </div>
        <!-- <section> -->
        <!--     <modal ref="modal" :enable&#45;mobile&#45;fullscreen="false" :modal&#45;theme="getTheme" :overlay&#45;theme="getTheme" -->
        <!--            :blocking="true" icon="success"> -->
        <!--         <h4 class="color_4">Avatar updated successfully</h4> -->
        <!--     </modal> -->
        <!-- </section> -->
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
import avatar from '../../../components/avatar.vue';
import imageUploader from '../../../components/image-uploader.vue';
import { SweetModal } from 'sweet-modal-vue';
export default{
    name : "basicEdit",
    props : ['profile'],
    inject : ['$validator'],
    components : {
        imageUploader,
        modal : SweetModal
    },
    computed:{
        ...mapGetters(['getTheme']),
    },
    // watch:{
    //     'avatar'(n,o){
    //         this.$refs.modal.open(); 
    //     }
    // }
}
</script>
<style lang="stylus"></style>
