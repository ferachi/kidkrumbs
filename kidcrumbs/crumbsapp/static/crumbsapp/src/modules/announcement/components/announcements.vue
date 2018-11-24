<template>
    <div class="announcements">
        <search-list :items="announcements" :search="search" :searchFields="['title', 'content','overview']">
            <section slot="controls"> 
                <md-field>
                    <label >search</label>
                    <md-input v-model='search'></md-input>
                </md-field>
            </section>
            <section slot="items" slot-scope="{items}">
                <div class="card-columns">
                    <div class="card" v-for="announcement in items" @click="$emit('announcement-click',announcement)">
                        <div class="card-body">
                            <h6 class="card-title font-weight-bold">{{announcement.title}}</h6>
                            <h6 class="card-subtitle mb-2 color_3"><small>{{announcement.school}}</small></h6>
                            <p class="card-text">{{announcement.overview}}</p>
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

</style>
