<template>
    <div id="comments" class=" d-flex justify-content-center flex-wrap">
        <div class="comments col-xl-  px-0">
            <section>
                <div class="my-3">
                    <comment-form @form-submit="submitForm($event)"></comment-form>
                </div>
                <div class="" v-for="comment in comments" :key="comment.id">
                    <div class="bg_aux rounded border border_1 comment-item mt-1 px-1">
                        <comment :comment="comment" :canReply="true" @reply="replyComment($event)"></comment>
                        <div class="comment-replies mt-2">
                            <div v-for="reply in comment.replies" class="boder_2 ml-3 reply-item ">
                                <hr>
                                <comment :comment="reply" :rightAlign="false"></comment>
                            </div>
                        </div>
                    </div>
                </div>  
            </section>
            <section>
                <modal ref="modal" :enable-mobile-fullscreen="false" :modal-theme="getTheme" :overlay-theme="getTheme">
                    <div v-if="reply">
                        <p class="text-left"> <span class="color_3">@reply to </span> <span class="primary-color"> {{ reply.person.username }}
                            </span> 
                        </p>
                    </div>
                    <comment-form @form-submit="replyForm($event)"></comment-form>
                </modal>
            </section>
        </div>
    </div>
</template>
<script>
import { SweetModal } from 'sweet-modal-vue';
import comment from "./comment-item.vue";
import commentForm from "./comment-form.vue";
import {mapActions, mapGetters} from "vuex";

export default{
    name : "Comment",
    created(){
    }, 
    data(){
        return {
            reply:null, 
        }
    },
    props:['comments', 'objectId'],
    computed:{
        ...mapGetters([
            'getTheme',
        ])
    },
    components:{
        comment, 
        commentForm, 
        modal:SweetModal
    },
    methods : {
        submitForm(data){
            this.$emit("add-comment", data);
        }, 
        replyForm(data){
            this.$emit("reply-comment", {comment:this.reply,data:data});
            this.hide();
        },
        replyComment(data){
            this.reply = data;
            this.show()
        },
        show () {
            this.$refs.modal.open(); 
        },
        hide () {
            this.$refs.modal.close(); 
        },
    },
    watch:{
        comments(val){
        }
    }
}
</script>
<style lang="stylus">
#comments
    .comment-item
        border-left-width 5px  !important
</style>

