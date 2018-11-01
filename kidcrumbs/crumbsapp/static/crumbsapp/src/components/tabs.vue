<template>
    <div class="crumbs-tabs">
        <ul class="d-flex list-unstyled" :class="justification">
            <li class="col-auto px-2 text-center" v-for="tab in tabs">
                <a :class="['text-capitalize',tab.isActive ? 'primary-color':'color_3'] "  @click="selectTab(tab)">{{tab.name}}</a>
            </li>
        </ul>
        <div class="tab-details">
            <slot>

            </slot>
        </div>
    </div>
</template>
<script>
export default {
    name: "",
    created(){
        this.tabs = this.$children;
    },
    data(){
        return {
            tabs :[],
        };
    },
    props:{
        justification : {
            type : String,
            default : 'justify-content-around'
        }
    },
    methods: {
      selectTab(tab) {
          this.tabs.forEach(_tab => {
              _tab.isActive = _tab.name == tab.name;
          });

      }
    }
};
</script>
<style lang="stylus" scoped>
</style>
