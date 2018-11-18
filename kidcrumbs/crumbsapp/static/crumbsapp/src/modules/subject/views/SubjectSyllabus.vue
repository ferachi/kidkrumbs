<template>
    <div id="subjectSyllabus">
        <div v-if="syllabus">
            <h5 class="righteous text-capitalize">{{subject.name}} Syllabus</h5>
            <p>{{syllabus.description}}</p>
            <div>
                <dl>
                    <template v-for="item in syllabus.syllabus_items" >
                        <dt class="color_5">{{item.title}} <span class="color_3"> - {{item.duration}}</span></dt>
                        <dd>
                        <p class="m-0">{{item.description}}</p>
                        </dd>
                    </template>
                </dl>
            </div>
        </div>
        <div v-else class="empty-holder d-flex align-items-center">
            <div class="col text-center " >
                <h2 class="text-capitalize color_3">Oops!!!</h2>
                <h1>
                    <span class="color_2 fa-stack fa-4x" style="vertical-align: top;">
                        <i class="far fa-circle fa-stack-2x"></i>
                        <i class="fas fa-times fa-stack-1x"></i>
                    </span>
                </h1>
                <h5>
                    No syllabus for {{subject.name}}
                </h5>
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
