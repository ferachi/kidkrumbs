import theme from './modules/theme';
import color from './modules/color';
import auth from './modules/auth.coffee';
import assessment from './modules/assessment';
import profile from './modules/profile.coffee';
import person from './modules/person.coffee';
import result from './modules/result';
import grade from './modules/grades.coffee';
import page from './modules/page.coffee';
import session from './modules/session.coffee';
import term from './modules/term.coffee';
import help from './modules/help.coffee';
import announcement from './modules/announcement';
import student from './modules/student';
import subject from './modules/subject';
import school from './modules/school';
import homework from './modules/homework';
import home from './modules/kidkrumb-home.coffee';
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
	device:{}
}


export default {
	state,
	mutations,
	getters,
	actions,
	modules:{
        activity,
        announcement,
        assessment,
        auth,
		child,
		classroom,
		color,
		grade,
		group,
		help,
        homework,
        home,
		menu,
        person,
        page,
        profile,
        result,
        routine,
        school,
        session,
        term,
        subject,
        student,
		theme,
	}
}
