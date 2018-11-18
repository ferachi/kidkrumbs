<template>
    <div id="subjectDetail" class="bg_0 border border_1">
        <transition name="fade">
        <div v-if="isLoading" class="loading" key="loading">

        </div>
        <div v-else key="loaded">
            <section class="header d-flex align-items-center flex-wrap" >
                <div class="col-auto first-char d-flex justify-content-center align-items-center" :style="{background:color}">
                    <div class="text-center">
                        <h1 class="display-1 rammeto m-0 color_white" >{{firstChar}}</h1>
                        <div class="d-xs-block d-sm-none">
                            <h2 class="font-weight-bold m-0 righteous color_white"> {{subject.name}}</h2>
                            <h5 class="m-0 font-weight-bold "><span class="color_white">{{subject.subject_code}} {{subject.session}}</span></h5>
                        </div>
                    </div>
                </div>
                <div class="col d-none d-sm-block">
                    <h2 class="font-weight-bold m-0 righteous"> {{subject.name}}</h2>
                    <h5 class="m-0 font-weight-bold "><span class="color_3">{{subject.subject_code}} {{subject.session}}</span></h5>
                    <p>{{subject.overview}}</p>
                </div>
            </section>
            <section class="menus">
                <div class="d-flex align-items-center  col-12 justify-content-around">
                    <router-link class="col p-0 py-3 m-0 text-center color_0" :to="{name:'subjectDetail'}"><small
                                 class="">About</small></router-link>
                         <router-link class="col p-0 text-center color_0" :to="{name:'subjectSyllabus'}"><small class="">Syllabus</small></router-link>
                         <router-link class="col p-0 text-center color_0" :to="{name:'subjectTeacher'}"><small
                                      class="">Teachers</small></router-link>
                              <router-link class="col p-0 text-center color_0" :to="{name:'subjectResult'}"><small class="">Results</small></router-link>
                </div>
            </section>
            <section class="p-3">
                <router-view></router-view>
            </section>
        </div>
        </transition>
    </div>
</template>
<script>
import {mapActions, mapGetters} from 'vuex';
export default{
    name : "SubjectDetail",
    created(){
        this.init();
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
            subject:null,
            isLoading : true
        }
    },
    methods:{
        ...mapActions('subject',[
            'fetchSubject'
        ]),
        init(){
            this.fetchSubject(this.$route.params.id).then( subject => {
                this.subject = subject;
                this.isLoading = false;
            });
        }
    },
    watch:{
        '$route'(){
            this.init();
        }
    }
}
</script>
<style lang="stylus">
#subjectDetail
    .first-char
        width 250px
        height @width
        @media screen and (max-width: 600px)
            width 100vw
            height @width
</style>
