from flask import Flask

app = Flask("My app with forms")
app.debug = True

@app.route('/register')
def show_registration_form():
	## VIEW 
	response =  '<html>'
	response += '  <h1>Registration form</h1>'
	response += '  <form name="registration" action="submit_registration_form" method="post">'
	response += '    First name       : <input type="text" name="firstname"><br/>'
	response += '    Last name        : <input type="text" name="lastname"><br/>'
	response += '    Username         : <input type="text" name="username"><br/>'
	response += '    Password         : <input type="password" name="password"><br/>'
	response += '    Confirm password : <input type="password" name="confpassword"><br/>'
	response += '    <input type="submit" value="Submit">'
	response += '  </form>'
	response += '</html>'
	return response

app.run()