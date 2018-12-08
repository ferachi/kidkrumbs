state =
	page : ''

mutations  =
	setPage : (state, _page) ->
		state.page = _page

getters =
	getPage : (state) ->
		state.page
		
export default{
	namespaced : true,
	state,
	mutations,
	getters
}
