import * as actions from './actions.coffee';
import mutations from './mutations.coffee';
import getters from './getters.coffee';

const state = {
    enrollmentResults : [], // enrollment with results
    enrollments : [],
    assessments : [],
    session : {},
    classroom : {},
    term : {},
    baseSubject : {},
    subject : {},
}


export default {
    namespaced : true,
	state,
	mutations,
	getters,
	actions,
}
