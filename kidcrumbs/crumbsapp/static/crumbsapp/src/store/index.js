import theme from './modules/theme';
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
		theme,
		menu,
		help
	}
}
