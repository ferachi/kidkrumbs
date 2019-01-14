import http from "../../http"
import {TOKEN, AUTH_USER, LOGOUT_USER, LOGIN} from "../../urls"


state =
    # Authenticated user
    # this differs from the users profile (person object) and is used for authentication
    authUser : {}
    authCredentials : {}


mutations =
    setAuthenticatedUser : (state, user) ->
        state.authUser = user
    setAuthCredentials : (state, data) ->
        state.authCredentials = data


actions =
    # Fetch the user account
    fetchUserAccount : ({commit, dispatch, state},{id}) ->
        http.get(AUTH_USER(id)).then (response) ->
            user = response.data
            commit 'setAuthenticatedUser', user

            # Fetch the profile 
            dispatch('profile/fetchProfile',user, {root:true}).then( (res)  => user)
   
    # Logs out the user account
    logout : ({commit, dispatch, state}) ->
        http.get(LOGOUT_USER).then (response) ->
            user = response.data
            commit 'setAuthenticatedUser', {}
            commit 'setAuthCredentials', {}
            commit 'profile/setProfile', {}, {root : true}
            response.data

    login : ({commit, dispatch, state}, user) ->
        dispatch('obtainToken').then (res) ->
            http.post(LOGIN, user).then (response) ->
                user = response.data
                dispatch('fetchUserAccount',{id:user.id}).then( (res)  => res)

    # Obtain the token for data editing
    obtainToken : ({dispatch, commit}) ->
        http.get(TOKEN).then (response) ->
            # obtain the response data
            data  = response.data

            # obtain the csrftoken
            # even if the user is not authenticated!
            http.defaults.headers.common['X-CSRFTOKEN'] = data.csrftoken


            console.log response.data.authenticated
            # if user is authenticated
            if response.data.authenticated
                # set up the User's credentials 
                # the user id and sessions can be found here
                commit 'setAuthCredentials', data

                # get the account and set up the user
                dispatch('fetchUserAccount',{id:data.user}).then( (res)  => res)

getters =
    getAuthUser : (state) ->
        state.authUser
    getAuthCredentials : (state) ->
        state.authCredentials
    isAuthenticated: (state) ->
        !_.isEmpty(state.authUser)


export default {
	namespaced : yes,
	state,
	mutations,
	actions,
	getters,
}
