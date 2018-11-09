<template>
    <div id="activities ">
        <div class="is-loading col" v-if="isLoading">
            ... 
        </div>
        <div v-else class="">
            <section class="header clearfix">
                <button class="btn btn-primary float-right" @click="addActivity">Add activity</button>
            </section>
            <section class="list-activity">
                <activity-list :showItemMenu="true" :activities="activities" @list-select="itemSelected($event)"></activity-list>
            </section>
            <section class="edit-activity" >
                <modal ref="modal" :enable-mobile-fullscreen="false" :modal-theme="getTheme" :overlay-theme="getTheme">
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
</template>
<script>
import { SweetModal } from 'sweet-modal-vue';
import {mapActions, mapGetters } from 'vuex';
import activityList from '../components/ActivityList.vue';
import addActivity from '../components/addActivity.vue';
import editActivity from '../components/editActivity.vue';
import confirmAction from '../../../components/confirm-action.vue';
import ROLES from '../../../data_models/permissions';
export default{
    name : "Activities",
    created(){
        this.pullActivities(this.testGroup).then( activities => {
            this.isLoading = false;
        });
    }, 
    computed:{
        ...mapGetters("activity", {
            activities : "getActivities"
        }),
        ...mapGetters([ 'getTheme' ]),
        ...mapGetters('profile',{
            profile:"getProfile",
            roles : "getRolesBySchool"
        }),
        hasEditPermissions(){
            let permittedRoles = [ROLES.TEACHER,ROLES.SUPERADMINISTRATIVE];

            // TODO: get the school from the group
            return !_.isEmpty(_.intersection(this.roles(this.testSchool), permittedRoles));
        }
    },
    data : () => ({
        isLoading : true,
        detailType:'view',
        testGroup : "944e18be-0b51-4ab5-a584-a87811cf1886",
        testSchool : "blue-international-primary-secondary-school",
        selectedActivity:{},
    }),
    components:{
        activityList,
        addActivity,
        editActivity,
        confirmAction,
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
                    this.selectedActivity.group = this.testGroup;
                    this.selectedActivity.created_by = this.profile.user;
                    this.saveActivity(this.selectedActivity).then(item => {
                        this.$toasted.show("Activity saved");
                    });
                }

            }
        }
    }
}
</script>
<style lang="stylus">
</style>

