const state = {
    colors:['dodgerblue','deeppink','purple','red','green','orange','teal'],
    color : 'dodgerblue'
}

const mutations = {
    setColor(state, _color){
        state.color = _color;
    }
}
const getters = {
    getColor(state){
        return state.color;
    },
    getColors(state){
        return state.colors;
    }
}

export default {
	state,
	mutations,
	getters,
}
