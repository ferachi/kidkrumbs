<template>
    <div id="schoolItem" class="px-3 pb-3">
        <div class="px-xl-5">
            <h5 class="font-weight-bold m-0 color_black pr-3">{{school.name}}</h5>
            <p class="color_black"><small class="color_black">{{school.motto}}</small></p>
        </div>
    </div>
</template>
<script>
export default{
    name : 'SchoolItem',
    props : ['school'],
    computed : {
    }
}
</script>
<style lang='stylus'>
#schoolItem
    height 100px
    overflow-y hidden
</style>

