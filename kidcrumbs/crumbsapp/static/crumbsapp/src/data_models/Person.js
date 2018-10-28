class User{
    constructor(id, email){
        this._id = id;
        this._email = email;
    }
}


class Person{
    constructor(user){
        this._user = user;
    }

    set avatar(_avatar){
        this._avatar = _avatar;
    }

    get avatar(){
        return this._avatar;
    }

    set title(_title){
        this._title = _title;
    }

    get title(){
        return this._title;
    }

    set description(_description){
        this._description = _description;
    }

    get description(){
        return this._description;
    }

    set occupation(_occupation){
        this._occupation = _occupation;
    }

    get occupation(){
        return this._occupation;
    }

    set gender(_gender){
        this._gender = _gender;
    }

    get gender(){
        return this._gender;
    }

    set dob(_dob){
        this._dob = _dob;
    }

    get dob(){
        return this._dob;
    }

    set hobbies(_hobbies){
        this._hobbies = _hobbies;
    }

    get hobbies(){
        return this._hobbies;
    }

    set qualifications(_qualifications){
        this._qualifications = _qualifications;
    }

    get qualifications(){
        return this._qualifications;
    }

}

    // title = models.CharField(max_length=20, blank=True)
    // description = models.TextField("Brief Description", blank=True)
    // occupation = models.CharField(max_length=120, blank=True)
    // gender = models.CharField(max_length=1, choices=GENDER, default='F')
    // dob = models.DateField("date of birth", null=True, blank=True)
    // hobbies = models.CharField(max_length=300, blank=True, help_text="Specify hobbies separated by commas")
    // qualifications = models.CharField(max_length=150, help_text='qualifications separated with commas', blank=True)
    // email_confirmed = models.BooleanField(default=False)
    // relatives = models.ManyToManyField('self', through='Relation', through_fields=('person','relative'), symmetrical=False, blank=True)
    // created_date = models.DateTimeField(auto_now_add=True)
    // timestamp = models.DateTimeField(auto_now=True)
export { Person as default, User } 
