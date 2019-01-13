<template>
    <div id="subjectSyllabus">
        <div v-if="syllabus">
            <h4 class="font-weight-bold my-3">Syllabus</h4>
            <p><small class="color_4">{{syllabus.description}}</small></p>
            <div>
                <template v-for="item in syllabus.syllabus_items" >
                    <hr>
                    <h6 class="color_5 font-weight-bold m-0">{{item.title}} </h6>
                    <p class="m-0"><span class="color_3">{{item.duration}}</span></p>
                    <p class="my-3"><small class="color_4">{{item.description}}</small></p>
                </template>
            </div>
        </div>
        <div v-else class="d-flex justify-content-center align-items-center" > 
            <div class="text-center col-auto py-4">
                <h1 class="color_2 mb-5">
                    <span class="color_2 fa-layers fa-fw fa-3x" style="vertical-align: top;">
                        <i class="fas fa-ban" data-fa-transform="grow-7"></i>
                        <i class="fas fa-book-open" data-fa-transform="shrink-7"></i>
                    </span>
                </h1>
                <h3 class="color_3 text-uppercase">No Syllabus</h3>
                <h6 class="color_3 text-upperase" style="line-height : 1.3em !important">{{subject.name}} does not have
                any syllabus yet</h6>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
export default{
    name : "SubjectSyllabus",
    components:{
    },
    computed : {
        ...mapGetters('subject', {
            subject : 'getSubject',
        }), 
        syllabus(){
            return this.subject.syllabus;
        }
    }
}
</script>
<style lang="stylus">
#subjectSyllabus
    .empty-holder
        min-height 40vh

</style>
