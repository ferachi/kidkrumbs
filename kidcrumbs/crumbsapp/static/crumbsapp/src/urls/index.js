// AUTHENTICATION
export const TOKEN = '/token/'; // direct access to token; is this secure?
export const AUTH_USER = (id) => `/api/accounts/${id}/`; // access to the logged in user;


// USER PROFILES
export const PEOPLE = '/api/people/'; // All Users; Will not be available 
export const PERSON = (id) => `${PEOPLE}${id}/`; // route to a single person
export const RELATIVES = (id) => `${PERSON(id)}get_relatives/`; // gets the users relatives
export const RELATIONSHIPS = (id) => `${PERSON(id)}get_relationships/`; // gets the users relatives
export const ROLES = (id) => `${PERSON(id)}get_roles/`; // gets the users schools roles


// STUDENTS
export const STUDENTS = '/api/students/'; // All Students, this list differs depending on the user requesting it 
export const STUDENT = (id) => `${STUDENTS}${id}/`; // route to a single student


// ACTIVITIES
export const ACTIVITIES = '/api/activities/'; // All Activities, this list differs with respect to school
export const ACTIVITY = (id) => `${ACTIVITIES}${id}/`; // route to a single activity
export const ACTIVITYITEMS = '/api/activity-items/'; // All sub activities, this list differs with respect to school
export const ACTIVITYITEM = (id) => `${ACTIVITYITEMS}${id}/`; // route to a single activity item


// GROUPS
export const GROUPS = '/api/groups/'; // All Groups, this list differs depending on the user requesting it
export const GROUP = (id) => `${GROUPS}${id}/`; // route to a single group
export const GROUP_ACTIVITIES = (id) => `${GROUP(id)}${get_activities}/`; // route to a groups activity list

export const CLASSROOMS = '/api/classrooms/'; // All classrooms, this list differs depending on the user requesting it 
export const CLASSROOM = (id) => `${CLASSROOMS}${id}/`; // route to a single classroom
