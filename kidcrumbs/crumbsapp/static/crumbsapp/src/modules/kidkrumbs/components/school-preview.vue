<template>
    <div id="schoolPreview" class="d-flex justify-content-center">
        <div class="col-lg-10 col-xl-8 px-0">
            <transition :name="anim" mode="out-in">
            <div class="d-inline-block"  v-if="isSchool">
                <div class="clickable" @click="previewClicked">
                    <h5 class="display- m-0 font-weight-bold text-uppercase" >{{school.name}}</h5>
                    <p class="color_3 text-capitalize" >{{school.contact.city}},{{school.contact.state}}</p>
                </div>
                    <hr class="mt-0">
                    <p class="color_3" :style="{color:`${school.color} !important`}">{{school.brief_description}}</p>
            </div>
            </transition>
        </div>     
    </div>
</template>
<script>
export default{
    name : 'SchoolPreview',
    created(){
        this.preschool = this.school;
    },
    props : {
        school :{
            type : Object,
            required : true
        }
    },
    computed : {
        isSchool(){
            return this.preschool.id === this.school.id;
        },
        anim(){
            return 'fade-up';
        }
    },
    methods:{
        previewClicked(){
            this.$router.push({name:'kidkrumbsSchoolDetail', params:{id : this.school.id}});
        }
    },
    data(){
        return{
            preschool:{}
        }
    },
    components : {
    },
    watch : {
        school(newVal, oldVal){
            setTimeout(() => {
                this.preschool = this.school;
            }, 300);
        }
    }
}

</script>
<style lang='stylus'>
</style>

