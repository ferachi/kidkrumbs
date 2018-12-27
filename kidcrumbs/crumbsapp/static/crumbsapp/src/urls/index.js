// AUTHENTICATION
export const TOKEN = '/token/'; // direct access to token; is this secure?
export const AUTH_USER = (id) => `/api/accounts/${id}/`; // access to the logged in user.
export const LOGOUT_USER = `/api/accounts/logout/`; // Logs out user


// USER PROFILES
export const PROFILES = '/api/profiles/'; // All Users; Will not be available 
export const PROFILE = (id) => `${PROFILES}${id}/`; // route to a single person
export const RELATIVES = (id) => `${PROFILE(id)}get_relatives/`; // gets the users relatives
export const RELATIONSHIPS = (id) => `${PROFILE(id)}get_relationships/`; // gets the users relatives
export const ROLES = (id) => `${PROFILE(id)}get_roles/`; // gets the users schools roles
export const PROFILE_ANNOUNCEMENTS = (id) => `${PROFILE(id)}get_announcements/`; // gets the users announcements
export const PROFILE_SCHOOLS = (id) => `${PROFILE(id)}get_schools/`; // gets the users schools


// PEOPLE PROFILES
export const PEOPLE = '/api/people/'; // All Users; Will not be available 
export const PERSON = (id) => `${PEOPLE}${id}/`; // route to a single person
export const PERSON_RELATIVES = (id) => `${PERSON(id)}get_relatives/`; // gets the users relatives
export const PERSON_RELATIONSHIPS = (id) => `${PERSON(id)}get_relationships/`; // gets the users relatives
export const PERSON_ROLES = (id) => `${PERSON(id)}get_roles/`; // gets the users schools roles
export const UPDATE_AVATAR = (id) => `${PERSON(id)}update_avatar/`; // updates profiles avatar
export const UPDATE_PROFILE = (id) => `${PERSON(id)}update_profile/`; // updates the users profile
export const CHANGE_PASSWORD = `${PEOPLE}change_password/`; // change the profiles password

// STUDENTS
export const STUDENTS = '/api/students/'; // All Students, this list differs depending on the user requesting it 
export const STUDENT = (id) => `${STUDENTS}${id}/`; // route to a single student
export const STUDENT_GROUPS = (id) => `${STUDENT(id)}get_groups/`; // gets an individual students' groups
export const STUDENT_RESULTS = (id) => `${STUDENT(id)}get_results/`; // gets an individual students' groups
export const STUDENT_TERM_POSITIONS = (id) => `${STUDENT(id)}get_term_result_positions/`; // gets an individual students' groups
export const STUDENT_CLASSROOMS = (id) => `${STUDENT(id)}get_classrooms/`; // gets an individual students' groups
export const STUDENT_SUBJECTS = (id) => `${STUDENT(id)}get_subjects/`; // gets an individual students' subjects
export const STUDENT_ENROLLMENTS = (id) => `${STUDENT(id)}get_enrollments/`; // gets an individual students' enrollments
export const STUDENT_MEMBERSHIPS = (id) => `${STUDENT(id)}get_memberships/`; // gets an individual students' memberships
export const STUDENT_CURRENT_GROUPS = (id) => `${STUDENT(id)}get_current_groups/`;//gets all the current groups for a student 
export const STUDENT_HABITS = (id) => `${STUDENT(id)}get_routines/`;//gets all the routines for the student
export const STUDENT_HABITS_BY_GROUP = (id,group) => `${STUDENT(id)}get_routines_by_group/?group=${group}`; // same as above but by group


// ACTIVITIES
export const ACTIVITIES = '/api/activities/'; // All Activities, this list differs with respect to school
export const ACTIVITY = (id) => `${ACTIVITIES}${id}/`; // route to a single activity
export const ACTIVITYITEMS = '/api/activity-items/'; // All sub activities, this list differs with respect to school
export const ACTIVITYITEM = (id) => `${ACTIVITYITEMS}${id}/`; // route to a single activity item
export const ACTIVITYCOMMENTS = '/api/activity-comments/'; // this route should only be used to create comments
export const ACTIVITYCOMMENTREPLIES = '/api/activity-comment-replies/'; // this route should only be used to create replies


// GROUPS
export const GROUPS = '/api/groups/'; // All Groups, this list differs depending on the user requesting it
export const GROUP = (id) => `${GROUPS}${id}/`; // route to a single group
export const GROUP_ACTIVITIES = (id) => `${GROUP(id)}get_activities/`; // route to a groups activity list
export const GROUP_ROUTINES = (id) => `${GROUP(id)}get_routines/`; // route to a groups activity list
export const GROUP_MEMBERS = (id) => `${GROUP(id)}get_current_members/`; // route to a groups member list
export const GROUP_STUDENTS = (id) => `${GROUP(id)}get_students/`; // route to a groups student list
export const GROUP_CURRENT_STUDENTS = (id) => `${GROUP(id)}get_current_students/`; // route to a groups current students' list
export const GROUP_TEACHERS = (id) => `${GROUP(id)}get_current_teachers/`; // route to a groups teacher list
export const GROUP_HABITS = (id) => `${GROUP(id)}get_habits/`; // route to a groups habit list


// CLASSROOMS
export const CLASSROOMS = '/api/classrooms/'; // All classrooms, this list differs depending on the user requesting it 
export const CLASSROOM = (id) => `${CLASSROOMS}${id}/`; // route to a single classroom
export const CLASSROOM_SUBJECTS = (id) => `${CLASSROOM(id)}get_subjects/`; // route to a single classrooms' subjects
export const CLASSROOM_HOMEWORKS = (id) => `${CLASSROOM(id)}get_homeworks/`; // route to a single classrooms' homeworks
export const CLASSROOM_MEMBERS = (id) => `${CLASSROOM(id)}get_members/`; // route to a single classrooms' members


// SCHOOLS
export const SCHOOLS = '/api/schools/'; // All Schools, this list differs depending on the user requesting it
export const SCHOOL = (id) => `${SCHOOLS}${id}/`; // route to a single school
export const SCHOOL_CLASSROOMS = (id) => `${SCHOOL(id)}get_classrooms/`; // route to a schools classrooms
export const SCHOOL_SUBJECTS = (id) => `${SCHOOL(id)}get_subjects/`; // route to a schools subjects
export const SCHOOL_SESSIONS = (id) => `${SCHOOL(id)}get_sessions/`; // route to a schools subjects
export const SCHOOL_STUDENTS = (id) => `${SCHOOL(id)}get_current_students/`; // route to a schools students
export const SCHOOL_GROUPS = (id) => `${SCHOOL(id)}get_groups/`; // route to a schools groups
export const SCHOOL_GRADE_SYSTEM = (id) => `${SCHOOL(id)}get_grade_system/`; // route to a schools groups


// ROUTINES
export const ROUTINES = '/api/routines/';
export const ROUTINE = (id) => `${ROUTINES}${id}/`;
export const ROUTINE_STUDENT_ROUTINES = (id) => `${ROUTINE(id)}get_students_routines/`;
export const STUDENT_ROUTINES = '/api/student-routines/';
export const STUDENT_ROUTINE =  (id) => `${STUDENT_ROUTINES}${id}/`;
export const STUDENT_ROUTINE_ATTITUDES =  (id) => `${STUDENT_ROUTINE(id)}get_students_attitudes/`;
export const ATTITUDES = '/api/attitudes/';

// ROUTINES
export const SUBJECTS = '/api/subjects/';
export const SUBJECT = (id) => `${SUBJECTS}${id}/`;

// ROUTINES
export const HOMEWORKS = '/api/home-works/';
export const HOMEWORK = (id) => `${HOMEWORKS}${id}/`;

// ANNOUNCEMENTS
export const ANNOUNCEMENTS = '/api/announcements/';
export const ANNOUNCEMENT = (id) => `${ANNOUNCEMENTS}${id}/`;

// SESSIONS
export const SESSIONS = '/api/sessions/';
export const SESSION = (id) => `${SESSIONS}${id}/`;


