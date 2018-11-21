import * as actions from './actions.coffee';
import mutations from './mutations.coffee';
import getters from './getters.coffee';

const state = {
    homeworks:[],
    homework:null
}


export default {
    namespaced : true,
	state,
	mutations,
	getters,
	actions,
}
