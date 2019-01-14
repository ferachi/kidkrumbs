<template>
    <div id="schoolsCarousel" class="p-2">
        <div class="d-flex">
            <transition-group :name="anim" tag="div" class="col d-flex justify-content-center justify-content-lg-end">
                <div class="col-auto school-item px-0 clickable" v-for="school in schoolList" :key="school.id" >
                    <avatar @click.native="logoClicked(school)" :image="school.logo" :alt="school.name"
                    size="normal" class="logo" :class="{'fade-elem':!school.isActive}"></avatar>
                </div>
            </transition-group>
        </div>
    </div>
</template>
<script>
import avatar from '../../../components/avatar.vue';
import {mapGetters} from 'vuex';
export default{
    name : 'SchoolsCarousel',
    created(){
        this._schools = _.map(_.cloneDeep(this.schools), (school,index) => {
            school.index = index;
            return school;
        });
        this.setActive();
        console.log(this.index, 'indexxx');
    },
    props : {
        schools :{
            type : Array,
            required : true
        },
        direction :{
            type : String,
            required : true
        },
        index:{
            type : Number,
            required : true
        },
        speed : {
            type : Number,
            default : 5000
        }
    },
    computed : {
        ...mapGetters({'device':'getDevice'}),
        schoolList(){
            this._index = this.index;
            return _.take(this._schools, 4);
        },
        anim(){
            return this.direction == 'right' ? 'fade-list-right' : 'fade-list-left';
        }
    },
    methods:{
        changeIndex(newVal, oldVal){
            let  school ;
            let len = this.schools.length - 1;
             
            if(this.isLogoClicked){
                let nums;
                if(newVal > oldVal)
                    nums = newVal - oldVal;
                else
                    nums = newVal + len + 1 - oldVal;

                let schools = this._schools.splice(0,nums);
                this._schools.push(...schools);
                console.log(schools, newVal, oldVal, nums);
                console.log(this._schools);
            }
            else{
                if(this.direction == 'right'){
                    school = this._schools.shift();
                    this._schools.push(school);
                }
                else 
                {
                    school = this._schools.pop();
                    this._schools.unshift(school);
                }
            }
            this._schools = _.map( this._schools , school => {
                school.isActive = false;
                return school;
            });
            this.setActive();
        },
        logoClicked(school){
            if(school.isActive){
                this.$router.push({name:'kidkrumbsSchoolDetail', params:{id : school.id}});
            }
            else{
                this.isLogoClicked = true;
                this.$emit('click-index', school.index);
            }
        },
        setActive(){
            this._schools[0].isActive = true;
            this.isLogoClicked = false;
        }
    },
    data(){
        return{
            playList : [{}],
            timeId : 0,
            isLogoClicked : false,
            midScreens : ['md','lg','xl'],
            _index : 0,
            _schools:[],
        }
    },
    components : {
        avatar
    },
    watch:{
        // schools(val){
        //     this._schools = _.cloneDeep(val);
        //     this._schools[0].isActive = true;
        // },
        index(newVal, oldVal){
            this.changeIndex(newVal, oldVal);
        }
    }
}
</script>
<style lang='stylus'>
#schoolsCarousel
    .logo
        transition all 0.4s ease-in-out

    .fade-elem
        opacity 0.3

    .school-item
        transition: all 0.4s ease-in-out;

    .fade-list-right-leave-to
    .fade-list-left-enter
        opacity: 0;
        transform: translateX(-30px);

    .fade-list-right-enter
    .fade-list-left-leave-to
        opacity: 0;
        transform: translateX(30px);
        
    .fade-list-right-leave-active
    .fade-list-left-leave-active
        position absolute

</style>

