export default class MenuItem{
    /**
     * Creates a menu item
     * @param {number} id - the id used for indexing and sorting
     * @param {string} title - the display title
     * @param {string} name - the programmatic reference
     * @param {string} link - the name of the page link
     * @param {string} [icon=""] - the icon to display on menu icon 
     * @param {string[]} [roles] - list of roles allowed to display the menu item on page
     */
    constructor(id, title, name, link, icon="", roles=[]){
        this._id = id;
        this._title = title;
        this._name = name;
        this._link = link;
        this._icon = icon;

        this._isActive = false;
        this._roles = roles;
        this._userRoles = [];
    }

    /**
     * Sets the users roles 
     * The users roles will be compared with the roles permitted to view the menu item.
     * If the user roles is not set, it defaults to an empty list of user roles
     * @param {string[]} roles - a list of user roles 
     */
    setUserRoles(roles){
        this._userRoles = roles;
    }
    

    /**
     * Determines if this menu item should be displayed
     * @return {boolean} true or false 
     *
     */
    get display(){
        return this.roles.some( role => this._userRoles.find( userRole => userRole == role));
    }


    ////////////////////////
    // GETTERS AND SETTERS
    ///////////////////////

    set roles(roles){
        this._roles = roles;
    }

    get roles(){
        return this._roles;
    }



    get id(){
        return this._id;
    }

    set id(id){
        this._id = id;
    }

    get title(){
        return this._title;
    }

    set title(title){
        this._title = title;
    }

    get name(){
        return this._name;
    }

    set name(name){
        this._name = name;
    }

    get link(){
        return this._link;
    }

    set link(link){
        this._link = link;
    }

    get icon(){
        return this._icon;
    }

    set icon(icon){
        this._icon = icon;
    }

    get isActive(){
        return this._isActive;
    }

    set isActive(isActive){
        this._isActive = isActive;
    }



}


