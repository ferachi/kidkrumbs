<template>
    <div class="scale">
        <input type="" v-model="inp">
        {{result}}
    </div>
</template>
<script lang="coffee">
export default
    name : 'scales'
    data : () ->
        inp : 0

    computed : 
        result : () ->
            scale = d3.scaleLinear()
                    .domain([-1,1])
                    .range([0,96])
            console.log scale.ticks()
            console.log scale.ticks(5)

            scale(@inp)


</script>
