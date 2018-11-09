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

        <alist :selectedItem="alistSelected" >
        <alistItem :showMenu="true" id="a" :menus="[{name:'Open', icon:'fas fa-envelope-open fa-fw fa-xs'}, {name:'Close', icon: 'fas fa-door-closed fa-fw fa-xs'}]" @alist-click="alistClicked($event)">

        <div slot="menu" slot-scope="{menus, id}">

            <slideMenu :showMenu="alistSelected==id" direction="top" layout="horizontal" @menu-click="slideMenuClick($event)" :menus="menus" >
            </slideMenu>
        </div>
        <div class="d-flex align-items-center">
            <div class="col-auto p-0 px-lg-4">
                <h1 class="display-2 d-none d-lg-block">10:25 am </h1>
            </div>
            <div class="col px-2">
                <h5 class="font-weight-bold">Hello</h5>
                <p>
                Lorem cum illo iste consectetur saepe Aliquam adipisci nesciunt non quibusdam a, natus Sed reiciendis amet repellendus accusantium architecto placeat officia. Reiciendis voluptates dolorem fugiat animi officia? Molestiae numquam maxime.
                </p>
            </div>
        </div>
        </alistItem>
        <alistItem :showMenu="true" id="b" :menus="[{name:'Open', icon:'fas fa-envelope-open fa-fw fa-xs'}, {name:'Close', icon: 'fas fa-door-closed fa-fw fa-xs'}]" @alist-click="alistClicked($event)">
        <div slot="menu" slot-scope="{menus, id}">

            <slideMenu :showMenu="alistSelected==id" direction="right" @menu-click="slideMenuClick($event)" :menus="menus" >
            </slideMenu>
        </div>
        <div class="d-flex align-items-center">
            <div class="col-auto p-0 px-lg-4">
                <h1 class="display-2 d-none d-lg-block" >12:25 pm </h1>
            </div>
            <div class="col px-2">
                <h5 class="font-weight-bold primary-color">Outgoing</h5>
                <p>
                Lorem cum illo iste consectetur saepe Aliquam adipisci nesciunt non quibusdam a, natus Sed reiciendis amet repellendus accusantium architecto placeat officia. Reiciendis voluptates dolorem fugiat animi officia? Molestiae numquam maxime.
                </p>
            </div>
        </div>
        </alistItem>
        <alistItem :showMenu="true" id="c" :menus="[{name:'Open', icon:'fas fa-envelope-open fa-fw fa-xs'}, {name:'Close', icon: 'fas fa-door-closed fa-fw fa-xs'}]" @alist-click="alistClicked($event)">
        <div slot="menu" slot-scope="{menus, id}">
            <slideMenu  :showMenu="alistSelected==id" @menu-click="slideMenuClick($event)" direction="left" :menus="menus" >
            </slideMenu>
        </div>
        <div class="d-flex align-items-center">
            <div class="col-auto p-0 px-lg-4">
                <h1 class="display-2 d-none d-lg-block" >1:25 pm </h1>
            </div>
            <div class="col px-2">
                <h5 class="card-title font-weight-bold secondary-color">Home work</h5>
                <p class="card-text">
                Lorem cum illo iste consectetur saepe Aliquam adipisci nesciunt non quibusdam a, natus Sed reiciendis amet repellendus accusantium architecto placeat officia. Reiciendis voluptates dolorem fugiat animi officia? Molestiae numquam maxime.
                </p>
            </div>
        </div>
        </alistItem>
        </alist>

    </div>
</template>
<script>
import tab from "./tab.vue";
import tabs from "./tabs.vue";
import tabHead from "./tabHead.vue";
import alist from "./alist.vue";
import alistItem from "./alistItem.vue";
import slideMenu from "./slideMenu.vue";

export default {
    name : "Test",
    data: () => ({
        selectedTab : 'menu',
        alistSelected:''
    }),
    components : {
        tabs,
        tab,
        alist,
        alistItem,
        slideMenu
    },
    methods:{
        tabClicked(tab){
            this.selectedTab = tab;
        },
        slideMenuClick(name){
            console.log(name);
        },
        alistClicked(item){
            this.alistSelected = item;
            console.log(item);
        }
    }

}
</script>



