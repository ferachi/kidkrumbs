import http from "../../http";
import {PERSON, RELATIONSHIPS, RELATIVES, ROLES} from "../../urls";


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
        person = http.get(PERSON(id))
        relatives = http.get(RELATIVES(id))
        relationships = http.get(RELATIONSHIPS(id))
        roles = http.get(ROLES(id))

        Promise.all([person,relatives,relationships, roles]).then (responses) ->

            person = responses[0].data
            person.relatives = responses[1].data
            relationships = responses[2].data
            person.relatives.forEach (relative) ->
                relationship = relationships.find (relationship) -> relationship.relative == relative.user
                relative.relationship = relationship.relationship
                relative.relationship_type = relationship.relationship_type_display
            
                
            # person.relationships = relationships
            person.roles = responses[3].data


            commit 'setProfile', person
            # person

getters =
    getProfile : (state) ->
        state.profile

export default {
	namespaced : yes,
	state,
	mutations,
	actions,
	getters,
}
