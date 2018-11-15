import * as actions from './actions.coffee';
import mutations from './mutations.coffee';
import getters from './getters.coffee';

const state = {
    routines : [],
    routine : null,
    studentRoutine : null,
    studentsRoutines : []
}


export default {
    namespaced : true,
	state,
	mutations,
	getters,
	actions,
}