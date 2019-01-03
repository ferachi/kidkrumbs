
state =
    school : {}
    menus : [
        {name : 'home', title : 'home', icon:"<span class='fas fa-home fa-fw'></span>", link : 'app', bigDisplay:true, isActive:false},
        {name : 'schools', title : 'schools', icon:"<span class='fas fa-school fa-fw'></span>", link : 'kidkrumbsSchools', bigDisplay:true, isActive:false},
        {name : 'about', title : 'about', icon:"<span class='fas fa-lightbulb fa-fw'></span>", link : 'aboutKidkrumbs', bigDisplay:false, isActive:false},
        {name : 'contact', title :'contact',icon:"<span class='fas fa-paper-plane fa-fw'></span>",link : 'contactKidkrumbs', bigDisplay:false, isActive:false},
        {name : 'login', title : 'login', icon:"<span class='fas fa-sign-in-alt fa-fw'></span>", bigDisplay:true, link : 'login',isActive:false},
        {name : 'crumbs', title : 'crumbs', icon:"<span class='fas fa-female fa-fw'></span>", bigDisplay:true, link : 'profile', isActive:false},
    ]

mutations =
    setSchool : (state, school) ->
        state.school = school

actions =
    activateMenu : ({getters}, menu) ->
        getters.getMenus.forEach (_menu) ->
            _menu.isActive = false

        menu.isActive = true


getters =
    getSchool : (state) ->
        state.school

    getMenus : (state) ->
        state.menus


export default {
    namespaced : true,
    state,
    actions,
    mutations,
    getters
}
