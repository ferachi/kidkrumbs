<template>
    <div class="activity-item">
        <div class="d-flex align-items-center">
            <div class="col-auto p-0 px-lg-4">
                <h1 class="display-2 d-none d-lg-block" >{{_time}} </h1>
            </div>
            <div class="col px-2">
                <h5 class="font-weight-bold" :style="{color:`${color.toLowerCase()} !important` }">{{title}}</h5>
                <p>{{description | truncate(100)}} </p>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: "",
    props :['_time', 'title', 'description', 'created_by','color']

};
</script>
<style lang="stylus">
</style>
