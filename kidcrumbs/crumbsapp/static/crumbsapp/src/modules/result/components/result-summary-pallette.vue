<template>
    <div class="resultPallete text-center" >
        <div class="header">
            <h6 class="my-1 color_4 text-capitalize" > {{title}}</h6>
            <p class="primary-color m-0">{{session.start}} - {{session.end}}</p>
        </div>
        <div class="score d-flex flex-column justify-content-center">
            <div class="col-auto">
                <h1 class="display-2 color_4 font-weight-bold">{{score}}</h1>
                <h4 class="m-0" v-if="!subject">of <span class="primary-color">{{maxScore}}</span></h4>
                <p class="m-0" v-if="subject">Obtained in {{subject}}</p>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name : "ResultPallete",
    props:{
        title : {
            type : String,
            required:true
        },
        session : {
            type : Object,
            required:true
        },
        score : {
            type : Number,
            required:true
        },
        maxScore : {
            type : Number,
            required:true
        },
        subject : {
            type : String,
            default : ''
        }
        
    }
}
</script>
<style lang="stylus">
.resultPallete
    .score
        height 300px
</style>
