<template>
    <div class="comment p-1">
        <div class="d-flex">
            <div class="col-xl-1 col-2 person-avatar px-xl-1 pt-2 px-0" :class="{'order-1' : rightAlign}">
                <avatar :showBg="false" size="fa-2x" :image="comment.person.avatar" :rounded="true"></avatar>
            </div>
            <div class="col px-1" :class="{'order-0 text-right' : rightAlign}">
                <div class="person-info" >
                    <slot name="header">
                    <h6 class="font-weight-bold m-0">
                        <small class="font-weight-bold color_5">{{comment.person.username}}</small>
                        <br>
                        <span class="font-weight-normal">
                            <small class="color_3"> {{comment.date}} </small>
                        </span>
                    </h6>
                    </slot>
                </div>
                <div class="person-comment">
                    <slot>
                    <p class="m-0 color_5">
                        {{comment.comment}}
                    </p>
                    </slot>
                </div>
                <div v-if="canReply" class="controls">
                    <div class="d-flex">
                    <p class="col-auto px-0" @click="$emit('reply', comment)"><small><span class="primary-color">reply</span> </small></p>
                    <p class="px-5"><small><span class="secondary-color"> view replies </span></small></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import avatar from "./avatarHolder.vue";
export default {
    name : "CommentItem",
    props : {
        comment :{
            type : Object,
            required : true
        },
        rightAlign : {
            type : Boolean,
            default : false
        },
        canReply : {
            type : Boolean,
            default : false
        }
    },
    components:{
        avatar
    }

}

</script>
