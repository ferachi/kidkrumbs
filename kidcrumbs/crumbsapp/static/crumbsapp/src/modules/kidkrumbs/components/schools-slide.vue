<template>
    <div id="schoolsSlide" class="p-2">
        <div class="d-flex">
            <transition-group :name="anim" tag="div" class="d-flex">
                <div class="col-auto school-item " :class="{clickable:school.isActive}" v-for="school in schoolList" :key="school.id" >
                    <avatar @click.native="logoClicked(school)" :image="school.logo" :alt="school.name"
                    :size="school.isActive ? 'large' : 'normal'" class="logo" :class="{'fade-elem':!school.isActive}"></avatar>
                </div>
            </transition-group>
        </div>
    </div>
</template>
<script>
import avatar from '../../../components/avatar.vue';
import {mapGetters} from 'vuex';
export default{
    name : 'SchoolsSlide',
    created(){
        this._schools = _.cloneDeep(this.schools);
        this.setActive();
    },
    props : {
        schools :{
            type : Array,
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

            if(_.includes(this.midScreens, this.device.screen))
                return _.take(this._schools, 5);
            else
                return _.take(this._schools, 3);
        },
        anim(){
            return this.direction == 'right' ? 'fade-list-right' : 'fade-list-left';
        }
    },
    methods:{
        changeIndex(newVal, oldVal){
            let  school ;
            let len = this.schools.length - 1;
            if(  (oldVal == len && newVal == 0) || (newVal > oldVal && (newVal != len || oldVal != 0))){
                this.direction = 'right';
            }
            else 
            {
                this.direction = 'left';
            }

            if(this.direction == 'right'){
                school = this._schools.shift();
                this._schools.push(school);
            }
            else 
            {
                school = this._schools.pop();
                this._schools.unshift(school);
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
        },
        setActive(){
            if(_.includes(this.midScreens, this.device.screen)) 
                this._schools[2].isActive = true;
            else
                this._schools[1].isActive = true;
        }
    },
    data(){
        return{
            playList : [{}],
            timeId : 0,
            midScreens : ['md','lg','xl'],
            _index : 0,
            _schools:[],
            direction: '',
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
#schoolsSlide
    .logo
        transition all 0.4s ease-in-out

    .fade-elem
        opacity 0.2

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

