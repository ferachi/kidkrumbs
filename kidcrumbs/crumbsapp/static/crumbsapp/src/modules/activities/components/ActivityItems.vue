<template>
    <div id="activityItems">
        <section class="clearfix">
            <button class="btn btn-primary float-right" @click="addActivity">add an activity </button>
        </section>
        <section >
            <itemList :showItemMenu="true" :activities="activities" @list-select="listSelected($event)"></itemList>
        </section>
        <section >
            <modal class=""  name="activityModal" height="auto" :scrollable="true" >
                <div class="d-flex justify-content-center">
                    <div class="col col-lg-10 py-3 ">
                        <section class="edit" v-if="detailType == 'edit'">
                            <itemEdit :activity="activity" @form-submit="formSubmit($event)"></itemEdit>
                        </section>
                        <section class="remove" v-else-if="detailType=='delete'">
                            <itemDelete :activity="activity" @delete-item="deleteActivity($event)"></itemDelete>
                        </section>
                        <section class="add" v-else-if="detailType== 'add'">
                            <itemAdd :activity="activity" @form-submit="formSubmit($event)"></itemAdd>
                        </section>
                        <section class="view" v-else>
                            <itemView :activity="activity" ></itemView>
                        </section>
                    </div>
                </div>
            </modal>
        </section>
    </div>
</template>
<script>
import activityItemList from './ActivityItemList.vue';
import activityItemView from './ActivityItemView.vue';
import activityItemAdd from './ActivityItemAdd.vue';
import activityItemEdit from './ActivityItemEdit.vue';
import activityItemDelete from './ActivityItemDelete.vue';
import ROLES from '../../../data_models/permissions';
import {mapGetters, mapActions} from 'vuex';
export default {
    name: "activityItems",
    components:{
        itemList: activityItemList,
        itemView: activityItemView,
        itemEdit: activityItemEdit,
        itemDelete: activityItemDelete,
        itemAdd: activityItemAdd,
    },
    data : () => ({
        isList : true,
        detailType : 'view',
        activity : null
    }),
    props:['activities','activityId', 'school'],
    computed:{
        ...mapGetters('profile',{
            profile:"getProfile",
            roles : "getRolesBySchool"
        }),
        hasEditPermissions(){
            let permittedRoles = [ROLES.TEACHER,ROLES.SUPERADMINISTRATIVE];
            return !_.isEmpty(_.intersection(this.roles(this.school), permittedRoles));
        }
    },
    methods:{
        ...mapActions('activity', {
            saveItem : "saveActivityItem",
            updateItem: "updateActivityItem",
            deleteItem: "deleteActivityItem"
        }),
        listSelected(item){
            this.activity = item.activity;
            this.detailType = item.detailType;
            this.show();
        },
        addActivity(){
            this.detailType = 'add';
            this.show();
        },
        show () {
            this.$modal.show('activityModal');
        },
        hide () {
            this.$modal.hide('activityModal');
        },
        formSubmit(item){
            this.activity = item;
            this.saveActiveItem();
            this.hide();
        },
        deleteActivity(canDelete){
            if(this.hasEditPermissions && canDelete){
                this.deleteItem(this.activity).then(res => {
                    this.$toasted.show("Activity Item deleted");
                });
            }
            this.hide();
        },
        saveActiveItem(){
            // make sure only teachers and super admins can save this
            // if the user profile has permissions then save it
            if(this.hasEditPermissions){
                
                // on edit, created_by is an object
                // and can only be saved to db by 
                // converting to a string with the user Id
                this.activity.created_by = this.profile.user;

                // code to save to db
                // is this a save or an update
                if(this.activity.id){
                    // its an edit
                    this.updateItem(this.activity).then(item => {
                        this.$toasted.show("Activity Item has been updated");
                    });
                }
                else{
                    this.activity.activity = this.activityId;
                    this.saveItem(this.activity).then(item => {
                        this.$toasted.show("Activity Item saved");
                    });
                }

            }
        }
    }
};
</script>
<style lang="stylus">
</style>
