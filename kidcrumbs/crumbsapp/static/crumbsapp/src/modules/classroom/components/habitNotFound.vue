<template>
    <div id="habitNotFound">
            <div class="d-flex align-items-center justify-content-center" >
                <div class="col text-center editable" v-if="editable">
                    <h2 class="color_3">Hello</h2>
                    <h1 @click="addRoutine">
                        <span class="color_2 fa-stack fa-4x" style="vertical-align: top;">
                            <i class="far fa-circle fa-stack-2x"></i>
                            <i class="fas fa-plug fa-stack-1x"></i>
                        </span>
                    </h1>
                    <h6>
                        No routine has been added. <br>
                         Click the plug to add a new routine.
                    </h6>
                </div>
                <div class="col text-center non-editable" v-else>
                    <h2 class="color_3">Hi!</h2>
                    <h1>
                        <span class="color_2 fa-stack fa-4x" style="vertical-align: top;">
                            <i class="far fa-circle fa-stack-2x"></i>
                            <i class="fas fa-times fa-stack-1x"></i>
                        </span>
                    </h1>
                    <h5>
                        Did not find any Habit. 
                    </h5>
                </div>
            </div>
    </div>
</template>
<script>
export default {
    name : 'HabitNotFound',
    props : {
        editable : {
            type : Boolean,
            default : true
        }
    },
    methods:{
        addRoutine(){
            // create a routine for today
            this.$emit('add-routine');
        }
    }

}

</script>
<style lang="stylus">
#habitNotFound
    > div
        min-height 70vh


</style>
