import http from "../../http"
import {PERSON, PERSON_RELATIONSHIPS, PERSON_RELATIVES, PERSON_ROLES, UPDATE_AVATAR, UPDATE_PROFILE, CHANGE_PASSWORD} from "../../urls"


state =
    profile : {}


mutations =
    setProfile : (state, person) ->
        state.profile = person

    setProfileImage : (state, image) ->
        state.profile =  Object.assign {}, state.profile,{image}


    setProfileAvatar : (state, avatar) ->
        state.profile =  Object.assign {}, state.profile,{avatar}

    # addRelation : (state, relation) ->
    #     # modify the relations
    #     if state.profile.relations
    #         state.profile.relations.push relation
    #     else
    #         state.profile.relations = [relation]
    #
    #     # make the profile reactive
    #     # after the update
    #     state.profile = Object.assign {},state.profile

actions =
    # Fetch users profile (person object)
    fetchProfile : ({commit, dispatch, state}, id) ->
        person = http.get(PERSON(id))
        relatives = http.get(PERSON_RELATIVES(id))
        relationships = http.get(PERSON_RELATIONSHIPS(id))
        roles = http.get(PERSON_ROLES(id))

        Promise.all([person,relatives,relationships, roles]).then (responses) ->

            person = responses[0].data
            relationships = responses[2].data
            relatives = responses[1].data
            person.relatives = _.map relatives , (relative) ->
                relative.relation = relationships.find (relationship) -> relationship.relative == relative.user
                relative.relationship_type = relative.relationship?.relationship_type_display
                relative
            # HACK 
            # used to change the username
            person._username = person.username
                
            # person.relationships = relationships
            person.schoolRoles = responses[3].data
            
            person.roles = _.uniq  _.flatMap person.schoolRoles, (sRole) ->
                sRole.roles

            commit 'setProfile', person
            person


    updateAvatar : ({commit, state, rootGetters}, image) ->
        return null unless state.profile

        authProfile = rootGetters['profile/getProfile']
        commit 'setProfileImage', image
        state.profile = _.omit(state.profile, ['relatives', 'roles', 'schoolRoles'])
        http.put(UPDATE_AVATAR(state.profile.username),state.profile).then (response) ->
            _profile = response.data.profile
            commit 'setProfileAvatar', _profile.avatar
            if(authProfile.user == _profile.user)
                commit 'profile/setProfileAvatar', _profile.avatar, {root : true}
            state.profile

    updateProfile : ({commit, state, dispatch}) ->
        return null unless state.profile

        state.profile = _.omit(state.profile, ['relatives', 'roles', 'schoolRoles'])
        http.put(UPDATE_PROFILE(state.profile.username),state.profile).then (response) ->
            _profile = response.data
            userProfile = dispatch('profile/fetchProfile',{id:_profile.user}, {root:true})
            personProfile = dispatch "fetchProfile", _profile.username

            Promise.all([userProfile, personProfile]).then (profiles) ->
                _profile


    changePassword : ({commit, state}, password) ->
        return null unless state.profile
        user = state.profile.user

        http.post(CHANGE_PASSWORD,{password,user}).then (response) ->
            state.profile


getters =
    getProfile : (state) ->
        state.profile

    getRolesBySchool : (state) -> (school) ->
        schoolRole  = _.find state.profile.schoolRoles, (role) ->
           role.school == school
        schoolRole.roles


export default {
	namespaced : yes,
	state,
	mutations,
	actions,
	getters,
}
