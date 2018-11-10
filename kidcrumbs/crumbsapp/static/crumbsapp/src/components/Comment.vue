<template>
    <div id="comments" class=" d-flex justify-content-center flex-wrap">
        <div class="comments col-xl-9  px-0">
            <div class="my-3">
                <comment-form @form-submit="submitForm($event)"></comment-form>
            </div>
            <div class="" v-for="comment in comments" :key="comment.id">
                <div class="bg_aux rounded border border_1 comment-item mt-1 px-1">
                    <comment :comment="comment" :canReply="true"></comment>
                    <div class="comment-replies mt-2">
                        <div v-for="reply in comment.replies" class="boder_2 ml-3 reply-item ">
                            <hr>
                            <comment :comment="reply" :rightAlign="false"></comment>
                        </div>
                    </div>
                </div>
            </div>  
        </div>
    </div>
</template>
<script>
import comment from "./comment-item.vue";
import commentForm from "./comment-form.vue";
import {mapActions} from "vuex";

export default{
    name : "Comment",
    created(){
    }, 
    props:['comments', 'objectId'],
    components:{
        comment, 
        commentForm
    },
    methods : {
        submitForm(data){
            this.$emit("add-comment", data);
        }
    },
    watch:{
        comments(val){
            console.log('has val changed', val);
        }
    }
}
</script>
<style lang="stylus">
#comments
    .comment-item
        border-left-width 5px  !important
</style>

