import ROLES from '../../data_models/permissions'
import MenuItem from '../../component_models/menu'

menus = [
    new MenuItem 0, "Me", "me", "app", "far fa-grin-stars fa-sm fa-fw", [ROLES.STUDENT]
    new MenuItem 1, "Children", "children", "children", "far fa-grin-squint fa-sm fa-fw", [ROLES.EXTERNAL]
    new MenuItem 2, "Class", "classroom", "classrooms", "fas fa-sm fa-chalkboard fa-fw", [ROLES.ADMINISTRATIVE]
    new MenuItem 3, "News", "news", "news", "far fa-bell fa-sm fa-fw", [ROLES.STUDENT,ROLES.ADMINISTRATIVE, ROLES.EXTERNAL]
    new MenuItem 4, "Profile", "profile", "app", "far fa-user fa-sm fa-fw", [ROLES.STUDENT,ROLES.ADMINISTRATIVE, ROLES.EXTERNAL]
    new MenuItem 5, "More", "more", "app", "fas fa-bars fa-sm fa-fw", [ROLES.STUDENT,ROLES.ADMINISTRATIVE, ROLES.EXTERNAL]
]
    
state =
    menus : menus


getters =
    # return the menus
    getMenus : (state, getters, rootState, rootGetters) ->
        # TEST: 
        # To get the logged in user role
        profile = rootGetters['profile/getProfile']

        userRoles = if profile?.roles then profile.roles else []
        
        #set the user roles for each menu item
        state.menus.forEach (menu) ->
            menu.setUserRoles userRoles

        # get only menus that can be displayed
        menus = state.menus.filter (menu) ->
            menu.display
        # menus[0].isActive = true

        # return menus
        menus

actions =
    activateMenu : ({state},menu) ->
        state.menus.forEach (menu) ->
            menu.isActive = false
        activeMenu = state.menus.find (_menu) ->
            menu.name == _menu.name
        activeMenu.isActive = true


export default{
    namespaced: true,
    state,
    actions,
    getters
}
