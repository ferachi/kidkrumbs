<template>
    <div id="AnnouncementList">
        <h3>Announcements</h3>
            <section id="announcementList">
                <announcements :announcements="announcements" @announcement-click="annoucementClicked($event)"></announcements>
            </section>
            <section id="announcementDetail">
                <modal ref="modal" :enable-mobile-fullscreen="true" :modal-theme="getTheme" :overlay-theme="getTheme"
                class="px-0">
                    <div class="d-flex justify-content-center"  v-if="announcement">
                        <div class="col px-0 col-lg-11 py-2 text-left">
                            <div>
                                <h4 class="font-weight-bold">{{announcement.title}}</h4>
                                <p>{{announcement.content}}</p> 
                                <p><small class="color_3"> announcer : {{announcement.announcer.names}}</small></p>                    
                            </div>
                        </div>
                    </div>
                </modal>
            </section>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
import announcements from '../components/announcements.vue';
import { SweetModal } from 'sweet-modal-vue';

export default{
    name : "AnnouncementList",
    data(){
        return {
            announcement : null
        }
    },
    computed : {
        ...mapGetters([ 'getTheme' ]),
        ...mapGetters('profile', {
            announcements : 'getAnnouncements'
        })
    },
    components : {
        announcements,
        modal : SweetModal
    },
    methods : {
        annoucementClicked(announcement){
            this.show();
            this.announcement = announcement;
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
