<template>
    <div id="slideControl" class="d-flex justify-content-center">
        <div class="text-center">
            <div class="d-inline-block clickable mr-3 text-center" @click="prevSchool">
                <span class="fas fa-chevron-left fa-fw fa-2x" ></span>
            </div>
            <div class="d-inline-block clickable text-center" @click="nextSchool">
                <span class="fas fa-chevron-right fa-fw fa-2x"></span>
            </div>
        </div>
    </div>
</template>
<script>
export default{
    name : 'slideControl',
    created(){
        this.$emit('index-change', this.index);
    },
    props : {
        schools :{
            type : Array,
            required : true
        },
    },
    computed:{
    },
    data(){
        return{
            index : 0,
        }
    },
    methods : {
        nextSchool(){
            this.index = this.index == this.schools.length - 1 ?  0 : this.index + 1
            this.$emit('index-change', this.index);
        },
        prevSchool(){
            this.index = this.index == 0 ?  this.schools.length - 1 : this.index - 1;
            this.$emit('index-change', this.index);
        }
    }
}
</script>
<style lang='stylus'>
</style>

