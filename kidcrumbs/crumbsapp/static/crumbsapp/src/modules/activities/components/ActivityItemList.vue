<template>
    <div id="activityItemList">
        <alist :selectedItem="alistSelected">
        <alistItem v-for="activity in activities" :item="activity" :showMenu="showItemMenu"
                   :id="activity.id" :menus="menus" @alist-click="alistClicked($event)"
                   :key="activity.key">
        <div slot="menu" slot-scope="{menus, active}">
            <slideMenu :canShowMenu="active" @menu-click="slideMenuClick($event)" :menus="menus" >
            </slideMenu>
        </div>
        <div slot-scope="{item}"> 
            <activity-item  v-bind="item"></activity-item> 
        </div>
        </alistItem>
        </alist>
    </div>
</template>
<script>
import alist from '../../../components/alist.vue';
import alistItem from '../../../components/alistItem.vue';
import slideMenu from '../../../components/slideMenu.vue';
import activityItem from './activitySummaryItem.vue';
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
        activityItem
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
</style>
