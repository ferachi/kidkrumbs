<template>
    <div id="comment">
        <div class="comments">
            <div class="comment" v-for="chat in comments" :key="chat.id">
                <div class="d-flex">
                    <div class="col-xl-1 person-avatar">
                        <avatar :showBg="false" :image="chat.person.avatar" :rounded="true"></avatar>
                    </div>
                    <div class="col">
                        <div class="person-info">
                            <h6 class="font-weight-bold">
                                {{chat.person.fullname}} {{chat.date}} 
                            </h6>
                        </div>
                        <div class="person-comment">
                            {{chat.comment}}
                        </div>
                    </div>
                </div>
            </div>  
        </div>
    </div>
</template>
<script>
import avatar from "./avatarHolder.vue";

export default{
    name : "Comment",
    created(){
    }, 
    props:['comments'],
    components:{
        avatar
    }
}
</script>
<style lang="stylus">
</style>

