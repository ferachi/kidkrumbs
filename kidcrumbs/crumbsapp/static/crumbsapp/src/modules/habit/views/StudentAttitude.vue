<template>
    <div class="studentAttitude">
        <div v-if="isLoading" key="loading" id="myE"></div>
        <div v-else class="my-2" key="loaded">
            <div class="card">
                <div class="card-body">
                    <div class="d-flex justify-content-between">
                        <h3 class="text-uppercase text-right font-weight-bold col">Habits</h3>
                        <div class="col-auto">{{routine.date}}</div>
                    </div>
                    <hr>
                    <div class="px-3 py-1">
                        <div v-if="editable">
                            <h6 class="m-0 text-uppercase font-weight-bold">Notes</h6>
                            <md-field>
                                <label>message/notes/reminders</label>
                                <md-textarea v-model="routine.message" md-autogrow ></md-textarea>
                            </md-field>
                        </div>
                        <div v-else>
                            <h5 class="text-uppercase font-weight-bold">Note:</h5>
                            <div v-if="routine.message" >
                                <blockquote class="blockquote">
                                    <p class="mb-0">{{routine.message}}</p>
                                </blockquote>
                            </div>
                            <div v-else>
                                <md-field >
                                    <label>message/notes/reminders</label>
                                    <md-textarea v-model="routine.message" md-autogrow readonly></md-textarea>
                                </md-field>
                            </div>
                        </div>
                    </div>
                    <hr>
                    <div class="habit p-3" v-for="(habit,index) in habits">
                        <h6 class="font-weight-bold">{{habit.title}}</h6>
                        <div class="d-flex flex-wrap">
                            <div v-for="(attitude,index) in habit.attitudes" class="col-6 col-md-4 col-lg-4 px-1">
                                <div v-if="attitude.type == 'CH'" >
                                    <md-checkbox true-value="YES" class="md-primary" false-value="NO"
                                                                                     v-model="attitudes[habit.key].options" :value="attitude.id"
                                                                                     :disabled="!editable">{{attitude.title}} </md-checkbox>
                                </div>
                                <div v-else-if="attitude.type == 'RD'">
                                    <md-radio class="md-primary" v-model="attitudes[habit.key].radio"
                                                                 :value="attitude.id" :disabled="!editable">{{attitude.title}} </md-radio>
                                </div>
                            </div>
                        </div>
                        <div class="d-flex flex-wrap"
                             v-if="attitudes[habit.key].texts && attitudes[habit.key].texts.length > 0 ">
                            <div class="col-6" >
                                <h6 class="m-0">Additional Info</h6>
                                <div v-for="text in attitudes[habit.key].texts" >
                                    <div class="d-flex" >
                                        <div class="col px-1" v-show="!(!editable && !text._t)">
                                            <md-field>
                                                <label>title</label>
                                                <md-input v-model="text._t" :readonly="!editable"></md-input>
                                            </md-field>
                                        </div>
                                        <div class="col px-1" v-show="!(!editable && !text._v)">
                                            <md-field>
                                                <label>value</label>
                                                <md-input v-model="text._v" :readonly="!editable"></md-input>
                                            </md-field>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr>

                    </div>
                    <div v-if="editable">
                        <button class="btn btn-primary" @click = "updateRoutine">update</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {mapGetters, mapActions, mapMutations} from 'vuex';
export default{
    name : "StudentAttitude",
    created(){
        this.fetchStudentRoutine(this.$route.params.id).then( routine =>{
            this.routine = routine;
            let attitudes = routine.attitudes

            // remap the habits to contain the attitudes w.r.t the habits' options
            this.habits = _.sortBy(_.map(this.getGroupHabits, _habit =>{

                // assign each habit its responses
                _habit.attitudes =  _.filter(attitudes, attitude => {
                    return _.some(_habit.options, opt =>{
                        return opt.id == attitude.habit_option;
                    });
                });

                // assign the element types to the attitude
                _.forEach(_habit.attitudes, attitude => {
                    let option = _.find(_habit.options, {id : attitude.habit_option});
                    attitude.type = option.habit_type
                    attitude.index = option.index;
                });
                _habit.attitudes = _.sortBy(_habit.attitudes, ['index'])
                // for sorting purposes
                _habit.key = _.camelCase(_habit.title);
                return _habit;
            }), ['key']);
            this.initAttitudeModel();
            this.isLoading = false;
        });
    },
    components:{
    },
    props:{
        editable:{
            type : Boolean,
            default:true
        }
    },
    data(){
        return {
            habits: [],
            attitudes:{},
            habitKeys:[],
            routine : null,
            isLoading:true
        }
    },
    computed:{
        ...mapGetters('group', [
            'getGroupHabits'
        ])
    },
    methods : {
        ...mapActions('routine', [
            'fetchStudentRoutine',
            'fetchStudentAttitudes',
            'updateStudentsRoutine'
        ]),
            initAttitudeModel(){
                // for each habit
                _.forEach(this.habits, _habit => {
                    // create object key and assign object
                    let key = _.camelCase(_habit.title);

                    this.attitudes[key] = {}
                    this.habitKeys.push(key); // add key to keys list; will play vital role in binding v-model

                    // iterate through attitudes
                    _.forEach(_habit.attitudes, attitude => {
                        switch(attitude.type){
                            case "RD":
                                // check if key 'radio' exist else create it
                                if(!_.has(this.attitudes[key],'radio')) this.attitudes[key]['radio']="";
                                if(!_.isEmpty(attitude.value)) this.attitudes[key]['radio'] = attitude.id;
                                break;
                            case "TX":
                                // this is dicy but ok
                                // // if key 'text' exist else create it
                                if(!_.has(this.attitudes[key],'texts')) this.attitudes[key]['texts']=[];

                                this.attitudes[key]['texts'].push({
                                    [`_t`] : attitude.title,
                                    [`_v`] : attitude.value,
                                    [`_k`] : attitude.id
                                });

                                // this.attitudes[key][attitude.id] = {
                                //     [`_t`] : attitude.title,
                                //     [`_v`] : attitude.value,
                                //     [`_k`] : attitude.id
                                // }
                                break;
                            default : 
                                // let checkbox be the default
                                // check if key 'option' exist else create it
                                if(!_.has(this.attitudes[key],'options')) this.attitudes[key]['options']=[];
                                if(attitude.value != "NO") this.attitudes[key]['options'].push(attitude.id);
                                break;
                        }
                    });
                });
                // because of the nested object creations dynamically
                // this has to be done to make the object reactive
                this.attitudes = Object.assign({}, this.attitudes);
            },
    convertModel(){

        // CHECKBOXES

        // get all attitudes for the Checkboxes
        let choiceAttitudes = _.flatMap(this.habits, _h => {
            return _.filter(_h.attitudes, {type : "CH"});
        });

        // clear all the choices
        _.forEach(choiceAttitudes, ch => {
            ch.value = "NO"
        })

        // merge all the options selected
        let optionsSelected = _.flatMap(this.attitudes, attitude => {
            if(_.has(attitude, 'options'))
                return attitude.options;
            return [];
        });

        // find the attitude from the choiceAttitudes 
        // using the optionsSelected.
        _.forEach(optionsSelected, opt => {
            let attitude = _.find(choiceAttitudes, {id:opt});
            attitude.value = "YES";
        });

        // RADIO
        // get all attitudes for the radios
        let radioAttitudes = _.flatMap(this.habits, _h => {
            return _.filter(_h.attitudes, {type : "RD"});
        });

        // clear all the radios
        _.forEach(radioAttitudes, rd => {
            rd.value = ""
        })

        // merge all the options selected
        let radiosSelected = _.flatMap(this.attitudes, attitude => {
            if(_.has(attitude, 'radio'))
                return attitude.radio;
            return [];
        });

        // find the attitude from the radioAttitudes 
        // using the radiosSelected.
        _.forEach(radiosSelected, opt => {
            let attitude = _.find(radioAttitudes, {id:opt});
            attitude.value = attitude.title;
        });

        // TEXTS
        // get all attitudes for the textes
        let textAttitudes = _.flatMap(this.habits, _h => {
            return _.filter(_h.attitudes, {type : "TX"});
        });

        // merge all the options selected
        let textsSelected = _.flatMap(this.attitudes, attitude => {
            if(_.has(attitude, 'texts'))
                return attitude.texts;
            return [];
        });

        // find the attitude from the textAttitudes 
        // using the textsSelected
        _.forEach(textsSelected, opt => {
            let attitude = _.find(textAttitudes, {id:opt._k});
            attitude.value = opt._v;
            attitude.title = opt._t;
        });

        let attitudes = _.map(this.habits, _h => _h.attitudes);
        if(_.isObject(this.routine.student)) 
            this.routine.student = this.routine.student.user;
        this.routine.editted_habit = true;
    },
    updateRoutine(){
        // save the attitudes
        this.convertModel();
        this.updateStudentsRoutine(this.routine).then( attitudes =>{
            this.$router.go(-1);
        });
    }
    }
}
</script>
<style lang="stylus">
</style>

