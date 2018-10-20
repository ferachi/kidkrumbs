import * as types from './mutation_types';
export default {
    [types.SET_DEVICE](state, device){
        state.device = device;
    },
    [types.SET_THEME](state, theme){
        state.theme = theme;
    }
}
