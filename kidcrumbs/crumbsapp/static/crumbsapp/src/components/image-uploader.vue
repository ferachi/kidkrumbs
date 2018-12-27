<template>
    <div class="image-uploader">
        <div class="text-center">
            <div  @click="changeImage" class="d-inline-block">
                <input v-show="false" name="avatar" id="uploadingImage" type="file" @change="uploadImage($event)">
                <div class="image" v-show="value">
                    <img :src="value" class="preview img-fluid rounded-circle" alt="preview">
                </div>
                <div class="placeholder" v-show="!value">
                    <span><i class="fas fa-user-circle fa-fw fa-8x"></i></span>
                </div>
            </div>
        </div>
        <div class="py-3 text-center">
            <button class="btn btn-secondary"  @click="changeImage" type="button" >change image</button>
        </div>
        <div>
        <section>
            <modal ref="modal" :enable-mobile-fullscreen="false" :modal-theme="getTheme" :overlay-theme="getTheme">
            <transition name='fade' mode="out-in">
            <div v-if="imageLoading" class="image-loading " key='loader'>
                <div class="d-flex align-items-center justify-content-center" >
                    <div class="col-auto">
                        <self-building-square-spinner
                         :animation-duration="4000"
                         :size="50"
                         />
                    </div>
                </div>
            </div>
            <div v-else class="image-loaded" key="editor">
                <div class="editor-container mx-auto">
                    <div v-if="uploadError" class="d-flex justify-content-center align-items-center" style="height:inherit">

                        <h4 class="primary-color text-center"><i class="fas fa-frown fa-fw fa-6x"></i> <br/>Sorry Boss! Your image is larger that 10mb. Do a resize and upload.</h4>
                    </div>
                    <img id="imageEditor" src="" alt="" class="editor" v-else>
                    <button class="btn btn-primary btn-block my-3" type="button" @click="saveImage" > Ok</button>
                </div>
            </div>
            </transition>
            </modal>
        </section>
        </div>
    </div>
</template>
<script lang="coffee">
import { SweetModal } from 'sweet-modal-vue'
import { SelfBuildingSquareSpinner  } from 'epic-spinners'
import {mapActions, mapGetters} from 'vuex'
export default
    name: "",
    props : ['value']
    model :
        prop : 'value'
        event : 'change'
    data : () ->
        imageLoading : true,
        cropper : null,
        uploadError : null,
        image : null
    computed :
        getTheme : mapGetters(['getTheme'])['getTheme'],
    methods:
        showModal : ()->
            @$refs.modal.open()
        closeModal : ()->
            @$refs.modal.close()
        updateAvatar : mapActions('person', ['updateAvatar'])['updateAvatar']
        uploadImage : (evt) ->
            input = evt.target
            @image = input.files?[0]
            unless @image
                return

            @imageLoading = true
            @uploadError = false
            @showModal()
            preview = document.querySelector(".image-uploader .preview")

            if @image.size > 9000000 # greater than 1Mb
                @uploadError = true
                @imageLoading = false
                @cropper.destroy() if @cropper
                return null

            # without the setTimeout to 1000ms, showModal = true
            # when reader almost finishes loading
            # remember that the uploadImage fn occurs when the imaged is changed!
            setTimeout () =>

                reader = new FileReader()
                reader.onload = (event) =>
                    # alert image editor that the image is now ready
                    @imageLoading = false
                    setTimeout () =>
                        try
                            imageEditor = document.querySelector("#imageEditor")
                            # pass in the image to editor
                            imageEditor.src = reader.result
                            # @value = reader.result

                            # if cropper exist destroy
                            @cropper.destroy() if @cropper

                            # new cropper
                            @cropper = new Cropper imageEditor,
                            aspectRatio : 1
                            viewMode : 1
                        catch error
                            return
                    ,1000

                reader.readAsDataURL @image
            ,1000

        saveImage : () ->
            @closeModal()
            if @cropper and @cropper.getCroppedCanvas()
                @image = @cropper.getCroppedCanvas({width : 400, height : 400}).toDataURL('image/jpeg')
                @updateAvatar(@image).then (user) =>
                    @$emit "change" ,@image
                # emit change to parent via the v-model bind

        changeImage : () ->
            $('#uploadingImage').trigger("click")

    components:
        modal : SweetModal
        SelfBuildingSquareSpinner : SelfBuildingSquareSpinner


</script>
<style lang="stylus">
.image-uploader
    img.preview
        width 100px
        height @width
    .image-loading
        postion absolute
        top 0
        right 0
        width 100%
        z-index 5
        >div
            min-height 300px
    .image-loaded
        postion absolute
        top 0
        right 0
        width 100%
        z-index 2


    .editor-fade-enter-active
    .editor-fade-leave-active
        transition opacity 0.5s ease-in-out
    .editor-fade-enter
    .editor-fade-leave-to
        opacity 0
    .editor-container
        @media screen and (max-width : 1300)
            width 500px
            height @width
        @media screen and (max-width : 641)
            width 300px !important
            height @width !important
        #imageEditor
            max-width 100%
</style>
