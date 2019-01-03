<template>
    <div class="announcements">
        <h3 class="font-weight-bold text-uppercase m-0 color_4 text-center">Announcements</h3>
        <search-list :items="announcements" :search="search" :searchFields="['title', 'content','overview']">
            <section slot="controls" class="d-flex justify-content-center"> 
                <div class="col-xl-6 col-lg-8 col-12">
                <md-field>
                    <label><i class="fas fa-search fa-fw"></i> search announcements</label>
                    <md-input v-model='search'></md-input>
                </md-field>
                </div>
            </section>
            <section slot="items" slot-scope="{items}">
                <div class="d-flex flex-wrap">
                    <div class="clickable col-xl-3 col-lg-4 col-12 bg_0 py-3 border border_aux announcement" v-for="announcement in items" @click="$emit('announcement-click',announcement)">
                        <div class="d-flex h-100 align-items-center">
                            <div class="col text-center">
                                <h6 class="m-0 "><small class="color_3">{{announcement.school}}</small></h6>
                                <h6 class="ont-weight-bold text-capitalize">{{announcement.title}}</h6>
                                <p class="">{{announcement.overview}}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </search-list>
    </div>
</template>
<script>
import searchList from '../../../components/alterlists.vue';
export default{
    name : "Announcements",
    props : {
        announcements : {
            type : Array,
            required : true
        }
    },
    data(){
        return {
            search : '',
        }
    },
    components : {
        searchList,
    }
}
</script>
<style lang="stylus">
.announcements
    .announcement
        min-height 200px

</style>
