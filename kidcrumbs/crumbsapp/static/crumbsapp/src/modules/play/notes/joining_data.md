# JOINING DATA

## entering data
**.enter** is used to request for extra data not found in a selection. It creates nodes with the data waiting to
be entered in the dom. To append this data we use **.append()**. e.g

    d3.selectAll("p")
        .data([1,2,3,4])
        .enter().append("p")
            .text( d => d)

This could do numerous things
-   if there was already existing data say `[4,5,6,7,8]`, then this replaces 4,5,6,7 with 1,2,3,4 becoming 1,2,3,4,8 and is just an update.
   This could have equally been done without .enter(<elem>).append() since no new content was added ([4,5,6,7,8] > [1,2,3,4] in
   length). i.e NO new element p is added

-   if there was already a p element with say text of *0*, then this would replace *0* with 1 and create 3 more p elements with 2,3 and 4 since really all you are doing is calling enter (extra data not found in selection) and appending it. Here new content is added.

-   if there were no existing data then this would create (enter) new p elements with data 1,2,3

*In general this just creates new elements and overwrites the existing if any*

on the other hand things get interesting when a key is used. 
    
    d3.selectAll("p")
        .data([1,2,3,4], d => d)
        .enter().append("p")
            .text( d => d )


-   if there was already existing data say `[4,5,6,7,8]`, then this becomes `[1,2,3,4,5,6,7,8]` adding to what
  already exist and merging (updating) similar items (in this case *4* ) 

-   if there was already a p element with say text of *0*, then this would create 4 more p elements with 1,2,3 and 4.
    Since the no similar key is found for updating an element.


## exiting data
**exit()** is used to request for old data, i.e data that differs from new/updated data, that is found in a selection.
it compiles all the nodes without the new data waiting to be exited. To remove this data we use **.remove()**


    d3.selectAll("p")
        .data([1,2,3,4])
        .exit().remove()

-   if there was already existing data say `[4,5,6,7,8]`, then this replaces 4,5,6,7 with 1,2,3,4 and it removes the 8.
    (default key is index)

-   if there was already a p element with say text of *0*, then this would replace *0* with 1 only. No new elements are
added.

-   if there were no existing data then this would do nothing.

*In all cases without key, a default key of index is used* 
if a key is used

    d3.selectAll("p")
       .data([1,2,3,4], d => d)
        .exit().remove()


-   if there was already existing data say `[4,5,6,7,8]`, then this becomes `[4]` removing 5,6,7,8

>   In general. If a key is used, then an update applies only to elements whose key exist on the new data. 
additions (enter) are available for keys that exist on the new data but not on the old one. And removals (exits) 
are available for keys that only exist on old data and not the new data.


** *In all cases without key, the index is used as the default key, but a key can also be specified to control data
joins* **

## Data Joining
Look at the following

    var circle = svg.selectAll("circle") // 1
      .data(data) // 2
          .style("fill", "blue"); // 3

    circle.exit().remove(); // 4

    circle = circle.enter().append("circle") // 5, 9
                .style("fill", "green") // 6
            .merge(circle) // 7
                .style("stroke", "black"); // 8
                
1. first select all circles
2. add data (update) to them
3. add a fill of blue to updated circles only
4. remove circles that were not updated (do not match the new data)
5. append the new circles 
6. fill the new circle selection with green
7. merge the new circle selection with the updated selection (from point 1)
8. style the new merge (selection now comprises of both update and new circles)
9. Store in variable circle.


