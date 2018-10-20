import * as types from "../mutation_types";
const state = {
    theme : 'light'
}

const mutations = {
    [types.SET_THEME](state, _theme){
        state.theme = _theme;
    }
}
const getters = {
    getTheme(state){
        return state.theme;
    }
}

export default {
	state,
	mutations,
	getters,
}
