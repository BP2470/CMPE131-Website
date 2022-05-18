# API Reference

All the following API used in the project

## Classes
`class User(UserMixin, db.Model)`
----------
Parameters

* `db.Model` - The database's model object
    * Constructor Parameters
        * id - ID of User
        * username - Username of User
        * password - Password of User
        * email - E-mail of User
        * post - Post of User
* `UserMixin` - User model implementation from Flask-Login
    * has an is_authenticated() method that returns True if the user has provided valid credentials
    * has an is_active() method that returns True if the user’s account is active
    * has an is_anonymous() method that returns True if the current user is an anonymous user
    * has a get_id() method which, given a User instance, returns the unique ID for that object
----------
Functions
* `def set_password(self, password)`
    Generates a hash password from `werkzeug.security` library
    * Parameters
        * self - User
        * password - User.password

* `def check_password(self, password)`
    Checks self's hash password with input password
    * Parameters
        * self - User
        * password - User.password

* `def delete(self)`
    Deletes self from database
    * Parameters
        * self - User

*   `def __repr__(self)`
    Returns the username and email of User object
    * Parameters
        * self - User
    * Return
        * self.username - Username of User
        * self.email - E-mail of User
----------
----------
`class Post(db.Model)`
----------
Parameters

* `db.Model` - The database's model object
    * Constructor Parameters
        * id - ID of User
        * body - Item/Text Content of User
        * timestamp - Date in UTC of item post of User
        * user_id - User ID of user
----------
Functions
* `def __repr__(self)`
    Returns the username and email of User object
    * Parameters
        * self - User
    * Return
        * self.user_id - User ID of User
        * self.timestamp - Timestamp of post of User
        * self.body - Item/Text content of User
----------
----------
`class LoginForm(FlaskForm)`
----------
Parameters
* `FlaskForm` - Flask-specific subclass of WTForms 
    * Constructor Parameters
        * username - class for StringField
        * password - class for PasswordField
        * remember_me - class for BooleanField
        * submit - class for SubmitField
----------
----------
`class SignUpForm(FlaskForm)`
----------
Parameters
* `FlaskForm` - Flask-specific subclass of WTForms 
    * Constructor Parameters
        * username - class for StringField
        * password - class for PasswordField
        * remember_me - class for BooleanField
        * submit - class for SubmitField
----------
----------
`class DeleteAccount(FlaskForm)`
----------
Parameters
* `FlaskForm` - Flask-specific subclass of WTForms 
    * Constructor Parameters
        * delete - class for SubmitField
----------
----------
`class addPost(FlaskForm)`
----------
Parameters
* `FlaskForm` - Flask-specific subclass of WTForms 
    * Constructor Parameters
        * addPost - class for StringField
----------
----------
`class buyForm(FlaskForm)`
----------
Parameters
* `FlaskForm` - Flask-specific subclass of WTForms 
    * Constructor Parameters
        * cardNumber - class for StringField
        * submit - class for SubmitField
----------
----------
`class buyForm(FlaskForm)`
----------
Parameters
* `FlaskForm` - Flask-specific subclass of WTForms 
    * Constructor Parameters
        * choices - List field for select class
        * select - class for SelectField for choices class for options in html
        * query - class for StringField
        * submit - class for SubmitField
----------
----------
----------
## Functions
`def load_user(id)`
Loads the user using a login manager library
* Parameter
    * id - ID of User
* Return
    * The User from query.filter of the ID
----------
`def signup()`
Creates a new User based on given inputs on the form
* Return
    * A render template of signup.html
----------
`def login()`
Logs in the User based on given inputs on form
* Return
    * A render template of login.html
----------
`def splash()`
A template screen before the home screen
* Return
    * A render template of splash.html
----------
`def home()`
Shows the home screen of the website or redirects to own user profile if
* Return
    * A render template of home.html
----------
`def profile()`
Shows the profile of the user currently logged in session
* Return
    * A render template of profile.html
----------
`def logout()`
Logs the user out of the session
* Return
    * A render template of logout.html
----------
`def deleteAccount()`
Deletes the user account from the database
* Return
    * A render template of delete.html
----------
`def all()`
Retrieves and shows all item posts from all Users
* Return
    * A render template of all.html
----------
`def search()`
Searches for exact User/Item Post based on input from user
* Return
    * Item not Found or exact User/Item string
----------
`def item_page(item_id)`
Shows a bidding page for the selected item along with the option to bid
* Parameter
    * item_id - ID of Item Post
* Return
    * A render template of item.html
----------
`def get_random_string`
Returns a random string of a given length of upper and lower case letters
* Parameter
    * length - given length of string that is constant for addPost function
* Return
    * A random string of the given length of upper and lower case letters
