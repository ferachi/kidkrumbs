import theme from './modules/theme';
import auth from './modules/auth.coffee';
import profile from './modules/profile.coffee';
import help from './modules/help.coffee';
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
        auth,
		theme,
		menu,
        profile,
		help
	}
}
