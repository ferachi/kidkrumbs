import * as actions from './actions.coffee';
import mutations from './mutations.coffee';
import getters from './getters.coffee';

const state = {
    results:[], 
    resultSet:[] // current list of results being viewed
}


export default {
    namespaced : true,
	state,
	mutations,
	getters,
	actions,
}
