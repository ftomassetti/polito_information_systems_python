from flask import Flask,request
from flask import render_template
from flask import abort, flash, redirect, url_for
from flask.ext.login import LoginManager, UserMixin
from flask.ext.login import current_user, login_required, login_user, logout_user
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, ValidationError

app = Flask("MyApp")
app.secret_key = 'MySecretKey'
app.debug = True

# Initialize the login system
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):

	def __init__(self,username,password,role):
		self.username   = username
		self.password = password
		self.role     = role

	def get_id(self):
		return self.username

	@classmethod
	def get_all(self):
		"Retrieve all the User, it should read them from the DB, actually"
		return [User('admin','qwerty123','ADMIN'),User('fausto','papetti','USER')]

class LoginForm(Form):
	username = TextField(    'username', validators = [Required()])
	password = PasswordField('password', validators = [Required()])

	def validate_username(self, field):
	    user = load_user(self.username.data)

	    if user is None:
	        raise ValidationError('Invalid user')

	    if user.password != self.password.data:
	        raise ValidationError('Invalid password')

@login_manager.user_loader
def load_user(username):
	"""It should return the user object with the given *userid* or return None.
	   It should not raise an Exception."""
	return [u for u in User.get_all() if u.username==username][0]

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = load_user(form.username.data)
        login_user(user)     
        flash("Logged in successfully.")
        return redirect(url_for("homepage"))
    return render_template("login.html", form=form, user=current_user)

@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
	logout_user()
	flash("You are now logged out")
	return redirect(url_for("homepage"))

@app.route('/')
@app.route('/index')
def homepage():
	"Everyone can access this page"
	print('USER= %s' % current_user)
	return render_template('homepage.html',user=current_user)	

@app.route('/about')
def about():
	"Everyone can access this page"
	return render_template('about.html',user=current_user)

@app.route('/reserved')
@login_required
def reserved_page():
	"Only for user logged in"
	return render_template('reserved.html',user=current_user)

@app.route('/admin')
@login_required
def admin_page():
	"Only for user logged in"
	if not current_user.role=='ADMIN':
		abort(403)
	return render_template('admin.html',user=current_user)		
		
app.run()