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
            type : String,
            required : true
        }
    },
    data(){
        return {
            list :[],
        };
    },
    methods: {
      selectTab(item) {
          this.list.forEach(_item => {
              console.log(_item.id,"hello" ,item, _item.isActive);
              _item.isActive = _item.id == item;
              console.log(_item,_item.isActive);
          });

      }
    },
    watch:{
        selectedItem(n,o){
            this.selectTab(n);
        }
    }
};
</script>
<style lang="stylus" scoped>
</style>
