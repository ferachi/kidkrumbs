<template>
    <div class="comment-form">
        <form @submit.prevent="validateBeforeSubmit">
            <div class="form-group">
                <textarea v-model="comment" v-validate="'required|min:2|max:300'" id="comment" name="comment" class="form-control" placeholder="comment" rows="2">
                </textarea>
                <i v-show="errors.has('comment')" class="fa fa-warning"></i>
                <span class="text-danger">{{ errors.first('comment') }}</span> 
            </div>
            <div class="form-group clearfix">
                <button type="submit" class="btn btn-primary float-right">Submit</button>
            </div>
        </form>
    </div>
</template>
<script>
export default {
    name : "CommentForm",
    data: () =>({
        comment: '',
    }),
    methods:{
        validateBeforeSubmit() {
            this.$validator.validateAll().then((result) => {
                if (result) {
                    this.$emit("form-submit", this.comment);
                    this.comment = '';
                    this.$nextTick(() => {
                        this.$validator.reset();
                        this.$validator.resume();
                    });
                    return;
                }
            });
        }
    }

}
</script>
<style lang="stylus">

</style>
