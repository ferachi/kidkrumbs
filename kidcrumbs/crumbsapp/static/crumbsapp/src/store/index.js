import theme from './modules/theme';
import auth from './modules/auth.coffee';
import profile from './modules/profile.coffee';
import person from './modules/person.coffee';
import result from './modules/result';
import grade from './modules/grades.coffee';
import page from './modules/page.coffee';
import session from './modules/session.coffee';
import help from './modules/help.coffee';
import announcement from './modules/announcement';
import student from './modules/student';
import subject from './modules/subject';
import school from './modules/school';
import homework from './modules/homework';
import child from './modules/child';
import group from './modules/group';
import classroom from './modules/classroom';
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
        announcement,
        auth,
		child,
		classroom,
		grade,
		group,
		help,
        homework,
		menu,
        person,
        page,
        profile,
        result,
        routine,
        school,
        session,
        subject,
        student,
		theme,
	}
}
