from flask import Flask,request,get_flashed_messages,redirect
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo

app = Flask("My app with forms")
app.debug = True

def messages_to_html():
	html = ""
	messages = get_flashed_messages()
	if messages:
		html += '<ul>'
		for m in messages:
			html += '<li>'+m+'</li>'
		html += '</ul>'
	return html

def errors_to_html(errors,field):
	html = ""
	print("ERRORS:")
	print(dir(errors))
	if errors.has_key(field):
		for error in errors[field]:
			html += '<span style="color: red;">'+error+'</span>'
	return html

# A Form is useful for:
# - refill the form if we sent it back to the user
# - do the validation
# - do format conversions

class RegistrationForm(Form):
	firstname    = TextField(    'firstname',             validators = [Required()])
	lastname     = TextField(    'lastname',              validators = [Required()])
	username     = TextField(    'username',              validators = [Required()])
	password     = PasswordField('password',              validators = [Required(),EqualTo('confpassword', message='Passwords must match')])
	confpassword = PasswordField('password confirmation', validators = [Required()])


@app.route('/registered')
def show_registered():
	# VIEW 
	response =  '<html>'
	response += '  <h1>Registered successfully!</h1>'
	response += '</html>'
	return response


@app.route('/register', methods=['GET','POST'])
def show_registration_form():
	form = RegistrationForm(csrf_enabled=False)

	if form.validate_on_submit():
		return redirect('/registered')

	# VIEW 
	response =  '<html>'
	response += '  <h1>Registration form</h1>'
	response += messages_to_html()
	# action is empty
	response += '  <form name="registration" action="" method="post">'
	response += '    First name       : '+str(form.firstname)+errors_to_html(form.errors,'firstname')+'<br/>'
	response += '    Last name        : '+str(form.lastname)+errors_to_html(form.errors,'lastname')+'<br/>'
	response += '    Username         : '+str(form.username)+errors_to_html(form.errors,'username')+'<br/>'
	response += '    Password         : '+str(form.password)+errors_to_html(form.errors,'password')+'<br/>'
	response += '    Confirm password : '+str(form.confpassword)+errors_to_html(form.errors,'confpassword')+'<br/>'
	response += '    <input type="submit" value="Submit">'
	response += '  </form>'
	response += '</html>'
	return response

app.run()