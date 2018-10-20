HELP_ARTICLES = [ 
	page : 'lounge'
	header : 'lounge header'
	content : 'lounge content'
,
	page : 'versus'
	header : 'versus header'
	content : 'versus content'
,
]

state = 
	displayModal : false
	helpArticles : HELP_ARTICLES

mutations  = 
	hideModal : (state, val) ->
		console.log 'hiding modal'
		state.displayModal = val
	openModal : (state, val) ->
		state.displayModal = val

actions = {}

getters = 
	showModal : (state) ->
		state.displayModal
	getHelp : (state, getters, rootState, rootGetter) ->
		# TODO:
		# get the current page from the page state 

		# TEMP:
		# temporary line; delete asap
		page = rootGetter['page/getPage']
		article = _.find state.helpArticles, (article) ->
			article.page == page
		article
		
export default{
	namespaced : true,
	state,
	mutations,
	actions,
	getters
}
