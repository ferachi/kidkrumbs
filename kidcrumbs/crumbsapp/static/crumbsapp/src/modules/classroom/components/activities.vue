<template>
    <transicion :isLoading="isLoading">
    <div id="activities" class="mx-lg-3 m-0">
        <div class="">
            <section >
                <div class="add-btn">
                    <md-button class="md-fab md-mini" @click="addActivity">
                        <md-icon class="fas fa-plus"></md-icon>
                    </md-button>
                </div>
            </section>
            <section class="filters d-flex flex-wrap align-items-center">
                <div class="col">
                    <dtpicker :disable-time="true" :dark="isDark" :without-header="true" v-model="date" format="YYYY-MM-DD" :auto-close="true" formatted="dddd, MMMM DD, YYYY" label="Select date"></dtpicker>
                </div>
                <div class="col-lg-auto col-12">
                    <md-checkbox class="md-primary" v-model="showAll">Show All</md-checkbox>
                </div>
            </section>
            <section class="list-activity">
                <activity-list :showItemMenu="editable" :activities="activities" @list-select="itemSelected($event)"></activity-list>
            </section>
            <section class="edit-activity" >
                <modal ref="modal" :enable-mobile-fullscreen="true" :modal-theme="getTheme" :overlay-theme="getTheme">
                <div class="d-flex justify-content-center">
                    <div class="col col-lg-11 py-2 ">
                        <section class="edit" v-if="detailType=='edit'">
                            <edit-activity :activity="selectedActivity"  @form-submit="formSubmitted($event)"></edit-activity>
                        </section>
                        <section class="add" v-else-if="detailType=='add'">
                            <add-activity  @form-submit="formSubmitted($event)"></add-activity>
                        </section>
                        <section class="remove" v-else-if="detailType == 'delete'">
                            <confirm-action @confirm="removeActivity($event)">
                                <h4>Are you sure you want to to delete this activity</h4>
                                <h1>{{selectedActivity.date}}</h1>
                            </confirm-action>
                        </section>
                        <section class="view" v-else></section>
                    </div>
                </div>
                </modal>
            </section>
        </div>
    </div>
    </transicion>
</template>
<script>
import { SweetModal } from 'sweet-modal-vue';
import {mapActions, mapGetters } from 'vuex';
import activityList from '../../activities/components/ActivityList.vue';
import addActivity from '../../activities/components/addActivity.vue';
import editActivity from '../../activities/components/editActivity.vue';
import confirmAction from '../../../components/confirm-action.vue';
import ROLES from '../../../data_models/permissions';
import transicion from '../../../components/transicion.vue';
export default{
    name : "Activities",
    created(){
        // this.fetchData();
    }, 
    mounted(){
        this.isLoading = false;
    },
    beforeDestroy(){
        $('.add-btn').hide();
    },
    computed:{
        ...mapGetters("activity",[ 
            "getActivities"
        ]),
        ...mapGetters([ 'getTheme' ]),
        ...mapGetters('profile',{
            profile:"getProfile",
            roles : "getRolesBySchool"
        }),
        isDark(){
            return this.getTheme == "dark";
        },
        activities(){
            if(this.showAll) 
                return this.getActivities;
            else 
                return _.filter(this.getActivities, {date : this.date});
        },
        hasEditPermissions(){
            let permittedRoles = [ROLES.TEACHER,ROLES.SUPERADMINISTRATIVE];

            // TODO: get the school from the group
            return !_.isEmpty(_.intersection(this.roles(this.schoolSlug), permittedRoles));
        }
    },
    data : () => ({
        isLoading : true,
        detailType:'view',
        date : moment().format("YYYY-MM-DD"),
        showAll: true,
        selectedActivity:{},
    }),
    props:{
        groupId:{
            type : String,
            required : true
        },
        schoolSlug:{
            type : String,
                required : true
        },
        editable:{
            type :Boolean,
            default: true
        },
        isComponent:{
            type :Boolean,
            default: true
        }
    },
    components:{
        activityList,
            addActivity,
            editActivity,
            confirmAction,
            transicion,
            modal: SweetModal,
    },
    methods:{
        ...mapActions("activity", [
            "pullActivities",
            "saveActivity",
            "updateActivity",
            "deleteActivity"
        ]),
            addActivity(){
                this.detailType = 'add';
                this.$refs.modal.open(); 
            },
            show () {
                this.$refs.modal.open(); 
            },
            hide () {
                this.$refs.modal.close(); 
            },
            removeActivity(canDelete){
                if(this.hasEditPermissions && canDelete){
                    this.deleteActivity(this.selectedActivity).then(res => {
                        this.$toasted.show("Activity deleted");
                    });
                }
                this.$refs.modal.close(); 
            },
            itemSelected(item){
                this.selectedActivity = item.activity;
                this.detailType = item.detailType;
                if(this.detailType == 'view'){
                    if(this.isComponent)
                        this.$emit('view-click', item.activity);
                    else
                        this.$router.push( {name:'activityDetail', params:{id:item.activity.id}});
                }
                else{
                    this.show()
                }
            },
            formSubmitted(item){
                this.selectedActivity = item;
                this.saveSelectedActivity();
                this.hide()
            },
            saveSelectedActivity(){
                // make sure only teachers and super admins can save this
                // if the user profile has permissions then save it
                if(this.hasEditPermissions){

                    // code to save to db
                    // is this a save or an update
                    if(this.selectedActivity.id){
                        // its an edit
                        this.updateActivity(this.selectedActivity).then(item => {
                            this.$toasted.show("Activity has been updated");
                        });
                    }
                    else{
                        this.selectedActivity.group = this.groupId;
                        this.selectedActivity.created_by = this.profile.user;
                        this.saveActivity(this.selectedActivity).then(item => {
                            this.$toasted.show("Activity saved");
                        });
                    }

                }
            },
            // fetchData(){
            //     this.pullActivities(this.groupId).then( activities => {
            //         this.isLoading = false;
            //     });
            // }
    },
    watch : {
        '$route'(){
            // this.fetchData();
        }
    }

}
</script>
<style lang="stylus">
</style>

