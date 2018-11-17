import http from "../../http";
import {PERSON, PERSON_RELATIONSHIPS, PERSON_RELATIVES, PERSON_ROLES} from "../../urls";


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
    fetchProfile : ({commit, dispatch, state}, id) ->
        person = http.get(PERSON(id))
        relatives = http.get(PERSON_RELATIVES(id))
        relationships = http.get(PERSON_RELATIONSHIPS(id))
        roles = http.get(PERSON_ROLES(id))

        Promise.all([person,relatives,relationships, roles]).then (responses) ->

            person = responses[0].data
            person.relatives = responses[1].data
            relationships = responses[2].data
            person.relatives.forEach (relative) ->
                relationship = relationships.find (relationship) -> relationship.relative == relative.user
                relative.relationship = relationship.relationship
                relative.relationship_type = relationship.relationship_type_display
            
                
            # person.relationships = relationships
            person.schoolRoles = responses[3].data
            
            person.roles = _.uniq  _.flatMap person.schoolRoles, (sRole) ->
                sRole.roles


            commit 'setProfile', person
            person

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
