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

