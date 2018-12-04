import http from "../../http";
import {PROFILE, RELATIONSHIPS, RELATIVES, ROLES, PROFILE_ANNOUNCEMENTS, PROFILE_SCHOOLS} from "../../urls";


state =
    profile : {} 


mutations = 
    setProfile : (state, person) ->
        state.profile = person;

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
    fetchProfile : ({commit, dispatch, state}, {id}) ->
        person = http.get(PROFILE(id))
        relatives = http.get(RELATIVES(id))
        relationships = http.get(RELATIONSHIPS(id))
        roles = http.get(ROLES(id))
        announcements = http.get(PROFILE_ANNOUNCEMENTS(id))
        schools = http.get(PROFILE_SCHOOLS(id))

        Promise.all([person,relatives,relationships, roles, announcements, schools]).then (responses) ->

            person = responses[0].data
            person.relatives = responses[1].data
            person.schools = responses[5].data
            relationships = responses[2].data
            person.relatives.forEach (relative) ->
                relationship = relationships.find (relationship) -> relationship.relative == relative.user
                relative.relationship = relationship.relationship
                relative.relationship_type = relationship.relationship_type_display
            person.announcements = responses[4].data
            commit 'announcement/setAnnouncements', person.announcements, {root : true} 
            
                
            # person.relationships = relationships
            person.schoolRoles = responses[3].data

            
            person.roles = _.uniq  _.flatMap person.schoolRoles, (sRole) ->
                sRole.roles


            commit 'setProfile', person
            person

getters =
    getProfile : (state) ->
        state.profile

    getAnnouncements : (state) ->
        state.profile?.announcements

    getRolesBySchool : (state) -> (school) ->
        schoolRole  = _.find state.profile.schoolRoles, (role) ->
           role.school == school
        schoolRole.roles

    getSchools : (state) -> 
        state.profile?.schools


export default {
	namespaced : yes,
	state,
	mutations,
	actions,
	getters,
}
