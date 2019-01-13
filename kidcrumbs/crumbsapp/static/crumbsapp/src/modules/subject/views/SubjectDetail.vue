<template>
    <div id="subjectDetail" class="bg_0 ">
        <transicion :isLoading="loading">
            <section class='text-center'>
                <div class="subject-caption bg_1 mx-auto text-center rounded-circle d-flex align-items-center
                    justify-content-center" >
                    <h1 class=" m-0 display-3 font-weight-bold" :style="{color:` ${color} !important`}">{{firstChar}}</h1>
                </div>
                <h4 class="mt-3 m-0 font-weight-bold text-uppercase">{{subject.name}}</h4>
                <p class="m-0"><span class="color_3">{{subject.core_subject.name}} - {{subject.session}}</span></p>
            </section>
            <hr>
            <section class="menus">
                <div class="d-flex align-items-center  col-12 justify-content-around mt-3">
                    <router-link v-for="menu in menus" :key="menu.name"
                     class="col p-0 m-0 text-center color_0" :to="{name:menu.link}"><small
                     class="primary-color" :style="{color : menu.isActive ? `${subject.color} !important` : ''}">{{menu.title}}</small></router-link>
                </div>
            </section>
                <hr/>
            <section class="px-lg-2 px-xl-4">
                <transition name="fade-up" mode="out-in">
                    <router-view></router-view>
                </transition>
            </section>
        </transicion>
    </div>
</template>
<script>
import {mapActions, mapGetters} from 'vuex';
import transicion from '../../../components/transicion.vue';
let menus = [
    { name : '', title : 'About', link : 'subjectDetail', isActive:true},
    { name : 'syllabus', title : 'Syllabus', link : 'subjectSyllabus', isActive:false},
    { name : 'teachers', title : 'Teachers', link : 'subjectTeacher', isActive:false},
    { name : 'results', title : 'Results', link : 'subjectResult', isActive:false}
]
export default{
    name : "SubjectDetail",
    created(){
        this.init();
        this.activateRoute();
    },
    components:{
        transicion
    },
    computed:{
        firstChar(){
            return this.subject.name.charAt(0);
        },
        color(){
            return this.subject.color;
        }
    },
    data(){
        return {
            subject:{name:'', core_subject:{}},
            loading : true,
            menus : menus
        }
    },
    methods:{
        ...mapActions('subject',[
            'fetchSubject'
        ]),
        init(){
            this.fetchSubject(this.$route.params.id).then( subject => {
                this.subject = subject;
                this.loading = false;
            });
        },
        activateRoute(){
            let menu = _.find(this.menus, menu => menu.link == this.$route.name)
            this.menus.forEach(menu => { menu.isActive = false; });
            menu.isActive = true;
        }
    },
    watch:{
        '$route'(val){
            this.activateRoute();
        }
    }
}
</script>
<style lang="stylus">
#subjectDetail
    .subject-caption
        width 100px
        height @width
        //@media screen and (max-width: 600px)
        //    width 100vw
        //    height @width
    .sub-views
        min-height 75vh
        max-height 75vh
        overflow-y auto
</style>
