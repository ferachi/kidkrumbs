<template>
    <div>
        <div id="comp">
            <p>0</p>             
            <p>1</p>             
        </div>
        <div class="controls">
            <button class="btn" @click="addCount">add count</button>
            <button class="btn" @click="removeCount">remove count</button>
            <button class="btn" @click="shuffleCount">shuffle count</button>
        </div>
    </div>
</template>
<script lang="coffee">
export default
    mounted : () ->
        d3.select("#comp")
          .selectAll("p")
          .data @c_data
          .enter().append("p")
            .text (d, i) ->
                d
    methods : 
        addCount : () ->
           @c_data = [2, 1, 4, ] 
        removeCount : () ->
            @c_data.splice @c_data.length - 1, 1

        shuffleCount : () ->
            @c_data = _.shuffle @c_data
        
    data : () =>
        c_data :[4, 42, 15, 16, 23, 8]
    watch : 
        c_data : (c_data) ->
            x = d3.select("#comp")
                  .selectAll("p")
                  .data @c_data
                    .text (d) ->
                        d
            x.enter().append("p")
               .text (d) -> d
            x.exit().remove()

            console.log x

</script>
