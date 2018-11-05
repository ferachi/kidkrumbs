<template>
    <div id="aList">
        <header>
            <slot name='header'>
            </slot>
        </header>
        <div class="content">
            <slot>
            </slot>
        </div>
    </div>
</template>
<script>
export default {
    name: "aList",
    created(){
        this.list = this.$children;
    },
    props:{
        selectedItem : {
            type : Object,
            required : true
        }
    },
    data(){
        return {
            list :[],
        };
    },
    methods: {
      selectItem(item) {
          this.list.forEach(_item => {
              _item.isActive = _item.id == item.id;
          });

      }
    },
    watch:{
        selectedItem(n,o){
            this.selectItem(n);
        }
    }
};
</script>
<style lang="stylus" scoped>
</style>
