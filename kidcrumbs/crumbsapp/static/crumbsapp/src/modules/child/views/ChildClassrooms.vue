<template>
    <div id="childClassrooms" class="d-flex justify-content-center">
        <div class="col-xl-10 px-0">
            <section id="classroomList">
                <classrooms :classrooms="classrooms" @classroom-click="classroomClicked($event)"></classrooms>
            </section>
            <section id="classroomDetail">
                <modal ref="modal" :enable-mobile-fullscreen="true" :modal-theme="getTheme" :overlay-theme="getTheme"
                class="px-0">
                    <div class="d-flex justify-content-center"  v-if="classroom">
                        <div class="col px-0 col-lg-11 py-2 text-left">
                            <classroom-summary :classroom="classroom"></classroom-summary>
                        </div>
                    </div>
                </modal>
            </section>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions} from 'vuex';
import classrooms from '../../classroom/components/classrooms.vue';
import classroomSummary from '../../classroom/components/classroom-summary.vue';
import { SweetModal } from 'sweet-modal-vue';
export default{
    name : "childClassrooms",
    computed:{
        ...mapGetters('child', {
           classrooms : 'getChildClassrooms'
        }),
        ...mapGetters([ 'getTheme' ])
    },
    data(){
        return {
            classroom : null
        }
    },
    components:{
        classrooms,
        classroomSummary,
        modal: SweetModal
    },
    methods:{
        classroomClicked(classroom){
            this.classroom = classroom;
            this.show();
        },
        show () {
            this.$refs.modal.open(); 
        },
        hide () {
            this.$refs.modal.close(); 
        },
    }
}
</script>
<style lang="stylus">

</style>
