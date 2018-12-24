<template>
    <div class="childList">
            <page>
            <div slot="header">
                <page-header class="primary-bg border-bottom border_0 py-3">
                    <div slot="pageTitle" >
                        <h4 class="m-0 color_white">Select Children</h4>
                    </div>
                    <div slot="pageMenu"></div>
                </page-header>
            </div>
            <div class="list-content">
                <section>
                <div class="p-3 d-flex align-items-center justify-content-between">
                    <div class="col-auto p-0">
                        <h3 class="font-weight-bold text-uppercase m-0 color_4">My Children</h3>
                    </div>
                    <div class="col-auto p-0">
                        <h1 class="m-0 font-weight-bold color_5 display-3 text-right" style="margin-bottom : -15px
                        !important; margin-top:-15px !important;">{{childCount}}</h1>
                        <p class="m-0 color_3" style="margin-top:-5px !important">{{childCount |
                        pluralize('child','children')}}</p>
                    </div>
                </div>
                </section>
                <section class="px-2">
                    <div class="children-list">
                        <people :people='children' @person-click="personClicked($event)"></people>
                    </div>
                </section>
            </div>
            </page>
    </div>
</template>
<script>
import {mapGetters} from 'vuex';
import ROLES from '../../../data_models/permissions';
import people from '../../../components/People.vue';
import transicion from '../../../components/transicion.vue';
import page from '../../../components/page.vue';
import pageHeader from '../../../components/pageHeader.vue';
export default{
    name : "Children",
    created(){
    },
    computed : {
        ...mapGetters("profile", {
            profile : "getProfile"
        }),
        children(){
            // still confirming that this person has an external role
            if(this.profile.roles.indexOf(ROLES.EXTERNAL) > -1){
                // get all relatives that are children
                return _.filter(this.profile.relatives, relative => {
                    return relative.relationship_type == "child";
                });
            }
        },
        childCount(){
            return this.children.length;
        }
    },
    components:{
        transicion,
        page,
        pageHeader,
        people
    },
    methods:{
        personClicked(child){
            this.$router.push({name:'child', params:{username: child.username}});
        }
    }
}
</script>
<style lang="stylus">
</style>
