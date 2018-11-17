import theme from './modules/theme';
import auth from './modules/auth.coffee';
import profile from './modules/profile.coffee';
import person from './modules/person.coffee';
import help from './modules/help.coffee';
import student from './modules/student';
import child from './modules/child';
import group from './modules/group';
import routine from './modules/routine';
import activity from './modules/activity';
import menu from './modules/menu.coffee';
import * as actions from './actions';
import mutations from './mutations';
import getters from './getters';
const state = {
	device:'',
}


export default {
	state,
	mutations,
	getters,
	actions,
	modules:{
        activity,
        auth,
		child,
		group,
		help,
		menu,
        profile,
        person,
        routine,
        student,
		theme,
	}
}
