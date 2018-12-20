<template>
    <div id="activityItems">
        <section v-if="canEdit">
            <div class="add-btn" v-if="showBtn">
                <md-button class="md-fab md-mini" @click="addActivity">
                    <md-icon class="fas fa-plus"></md-icon>
                </md-button>
            </div>
        </section>
        <section >
            <itemList :showItemMenu="canEdit" :activities="activities" @list-select="listSelected($event)"></itemList>
        </section>
        <section >
            <modal ref="modal" :enable-mobile-fullscreen="true" @close="$emit('hide-modal')" :modal-theme="getTheme" :overlay-theme="getTheme" class="px-0">
                <div class="d-flex justify-content-center">
                    <div class="col col-lg-10 py-3 ">
                        <section class="edit" v-if="detailType == 'edit'">
                            <itemEdit :activity="activity" @form-submit="formSubmit($event)"></itemEdit>
                        </section>
                        <section class="remove" v-else-if="detailType=='delete'">
                            <confirm-action @confirm="deleteActivity($event)">
                                <h4>Are you sure you want to delete</h4>
                                <h1>{{activity.title}}</h1>
                            </confirm-action>
                        </section>
                        <section class="add" v-else-if="detailType== 'add'">
                            <itemAdd @form-submit="formSubmit($event)"></itemAdd>
                        </section>
                        <section class="view" v-else-if="detailType== 'view'">
                            <itemView :activity="activity" ></itemView>
                        </section>
                        <section v-else></section>
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
import confirmAction from '../../../components/confirm-action';
import { SweetModal } from 'sweet-modal-vue';
import ROLES from '../../../data_models/permissions';
import {mapGetters, mapActions} from 'vuex';
export default {
    name: "activityItems",
    mounted(){
        setTimeout(() => {
            this.showBtn = true;
        }, 400);
    },
    beforeDestroy(){
        $('.add-btn').hide();
    },
    components:{
        confirmAction,
        itemList: activityItemList,
        itemView: activityItemView,
        itemEdit: activityItemEdit,
        itemAdd: activityItemAdd,
        modal : SweetModal
    },
    data () {
        return {
            isList : true,
            detailType : '',
            showBtn : false,
            activity :this.activities[0]
        }
    },
    props:{
        activities : {
            type : Array,
            required : true
        },
        activityId : {
            type : String, 
            required : true
        },
        school : {
            type : String,
            required : true
        },
        canEdit : {
            type : Boolean,
            default : false
        },
    },
    computed:{
        ...mapGetters(['getTheme']),
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
            this.$refs.modal.open(); 
        },
        hide () {
            this.$refs.modal.close(); 
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
#activityItems
    .add-btn
        position fixed
        bottom 50px
        right 5px
</style>
