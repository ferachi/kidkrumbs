<template>
    <div>
        <h4>TEST</h4>
        <tabs justification="justify-content-end">
            <tab name="menu" :selected="true"><div>
    Consectetur totam aliquam aspernatur sequi fugiat dolorum? Debitis culpa ipsum magni repellendus nisi. Deleniti mollitia enim impedit dolores non Beatae dolorum corporis perferendis pariatur ab Sapiente sed consectetur aliquam autem
</div>
 </tab>
            <tab name="plots">He must have used a lorem! </tab>
        </tabs>
        <div class="d-flex">
        <p class="primary-color col-auto">Date</p>
        <tab-head class="col" :tabTitles="['menu', 'home']" justify="justify-content-end" @tab-click="tabClicked($event)"></tab-head>
        </div>
        <div class="tabs">
            <div v-if="selectedTab == 'menu'">
                <h1>Menu</h1>
            </div>
            <div v-else-if="selectedTab == 'home'">
                <h1>Home</h1>
            </div>
            <div v-else-if="selectedTab == 'away'">
                <h1>Away</h1>
            </div>
            <div v-else></div>
        </div>


    </div>
</template>
<script>
import tab from "./tab.vue";
import tabs from "./tabs.vue";
import tabHead from "./tabHead.vue";

export default {
    name : "Test",
    data: () => ({
        selectedTab : 'menu'
    }),
    components : {
        tabs,
        tab,
        tabHead
    },
    methods:{
        tabClicked(tab){
            this.selectedTab = tab;
        }
    }

}
</script>



