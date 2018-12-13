import * as actions from './actions.coffee';
import mutations from './mutations.coffee';
import getters from './getters.coffee';

const state = {
    activityList : [], // the massive listing of all viewed activities
    activities : [],
    activity : null, // currently viewed activity
}


export default {
    namespaced : true,
	state,
	mutations,
	getters,
	actions,
}
