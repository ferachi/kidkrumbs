<!-- DASH LIST COMPONENT -->
<!-- This component helps to sort, filter and search for items in a list on the views -->
<!-- Requires
    items : a list of items to search, sort and filter
    filters: a list of field(s) with the interface {filterField:filter} to display off the items, or a  single string 'all' to filter all the fields in the list.
    searchFields: list of fields to search from.
 -->
<template>
    <div class='search-list'>
        <div class="list-controls">
            <slot name='controls' >
                <input type="text" class="form-control" v-model='searchWord' placeholder="search">
            </slot>
        </div>
        <div class="list-items">
            <div v-if="listItems.length > 0" key='list'>
                <slot name='items' :items='listItems'>
                </slot>
            </div>
            <div v-else key="empty">
                <slot name='empty'>
                    <h1 class="text-center">
                        Not Found
                    </h1>
                </slot>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "",
    created(){
    },
    data(){
        return {
            searchWord : this.search
        };
    },
    computed:{
        listItems(){
            // first filter the items
            

            // setup the initial items that 
            // would eventually be returned after 
            // filtering, ordering and sorting
            let _items = this.items;


            // if the filter is not a string
            // then it is an array of objects with interface
            // {FilterField : filter} e.g {color : 'green'}
            // this filters items with respect to the fields that 
            // have the filter values e.g filter objects with 
            // color field of value green.
            if(typeof this.filters !== 'string'){
                // for each filter object in the filters list
                // filter each object in the _items with respect
                // to the filter objects' value
                _.forEach(this.filters, filter =>{
                    // filter the items list with the filter object
                    _items = _.filter(_items, item => {

                        // get the key and value of the filter object
                        // the key is field on the item that we need to filter;
                        // e.g filter = {type:'classroom'}
                        let filterKey = _.keys(filter)[0],
                            filterVal = _.values(filter)[0];

                        // filter the object e.g if item[type] == 'classroom'
                        return _.includes(item[filterKey].toLowerCase(),filterVal.toLowerCase());
                    });
                });
            }

            // After the filtering now search for string specified
            let _searchFields = this.searchFields;

            // if searchFields is a single string, convert it to a list with a single item
            // this will make it easier to filter when i use reduce later.
            // e.g searchFields = "color" => _searchFields = ["color"]
            if(typeof _searchFields == 'string' && _searchFields != 'all')
                _searchFields = [_searchFields];
            else if(typeof _searchFields == 'string' && _searchFields == 'all'){
                // if search fields is all, then use all the keys in the item
                // this assumes the list is homogenous! hence I'm using the first item.
                _searchFields = _.keys(_items[0]);
            }


            // if there's a search word specified
            if(!!this.search || !!this.searchWord){

                // filter the items where the search word is found in the specied fields.
                _items = _.filter(_items , item =>{
                    //creating one single string from all the search fields to search in.
                    let concatWords = _.reduce(_searchFields, (acc, field) => {
                        acc += item[field];
                        return acc;
                    },"");
                    return _.includes(concatWords.toLowerCase(), this.search.toLowerCase());
                });
            }

            // emit the change event
            this.$emit('items-change');

            // sort and return the items
            return _.orderBy(_items,this.sortFields,this.order);
        }
    },
    props:{
        filters:{
            type:[Array, String], // an array with objects of interface {filterField:filter} or 'all'e.g [{type:classroom},{color:green},{school:myschool}]
            default:'all'
        },
        searchFields:{
            type:[Array, String], // the fields in the items list where the search shall be applied
            default:'all'
        },
        sortFields:{
            type:Array,
            default:()=>{
                return [];
            }
        },
        search:{
            type:String,
            default:''
        },
        items:{
            type:Array,
            required:true
        },
        order:{
            type:Array,
            default:()=>{
                return []
            }
        }
    }
};
</script>
<style lang="stylus">
</style>
