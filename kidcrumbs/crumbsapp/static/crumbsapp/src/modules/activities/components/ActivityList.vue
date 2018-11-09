<template>
    <div id="activityList">
        <div class="activities" v-if="hasActivities">
            <alist :selectedItem="alistSelected">
            <alistItem v-for="activity in activities" :item="activity" :showMenu="showItemMenu"
                       :id="activity.id" :menus="menus" @alist-click="alistClicked($event)"
                       :key="activity.id">
            <div slot="menu" slot-scope="{menus, active}">
                <slideMenu :canShowMenu="active" @menu-click="slideMenuClick($event)" :menus="menus" >
                </slideMenu>
            </div>
            <div slot-scope="{item}"> 
                <activity-caption  :activity="item"></activity-caption> 
            </div>
            </alistItem>
            </alist>
        </div>
        <div class="empty d-flex justify-content-center align-items-center" v-else>
            <div class="col-auto">
                <h1 class="display-4 color_3">Add Items by clicking the add button.</h1>
            </div>
        </div>
    </div>
</template>
<script>
import alist from '../../../components/alist.vue';
import alistItem from '../../../components/alistItem.vue';
import slideMenu from '../../../components/slideMenu.vue';
import activityCaption from '../components/activityCaption.vue';
export default {
    name: "activityItemsList",
    data : ()=> ({
        alistSelected:{},
        menus : [{name:'view', icon:'fas fa-eye fa-fw fa-sm'}, {name:'edit', icon: 'fas fa-edit fa-fw fa-sm'},
       {name:'delete', icon: 'fas fa-trash fa-fw fa-sm'} ]
    }),
    components : {
        alist,
        alistItem,
        slideMenu,
        activityCaption
    },
    computed:{
        hasActivities(){
            return this.activities.length > 0;
        }
    },
    props:{
        activities:{
            type : Array,
            required: true
        },
        showItemMenu : {
            type: Boolean,
            default : false
        }
    },
    methods:{
        slideMenuClick(name){
            this.$emit('list-select', {activity : this.alistSelected , detailType : name});
        },
        alistClicked(item){
            this.alistSelected = item;
            if(!this.showItemMenu)
                this.$emit('list-select', {activity : item , detailType : 'view'})
        }
    }
};
</script>
<style lang="stylus">
#activityList
    .empty
        min-height 50vh
</style>
