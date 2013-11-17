from flask import Flask,request

app = Flask("My app with forms")
app.debug = True

@app.route('/register')
def show_registration_form():
	# VIEW 
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

@app.route('/submit_registration_form',methods=['POST'])
def process_registration_form():
	print('Form')
	print(request.form)
	
	# CONTROLLER
	password_match = request.form['password']==request.form['confpassword']
	print("Password match? "+str(password_match))

	# if password do not match we would like to send back the
	# user and refill the form with the information that were
	# correct...
	
	# VIEW 
	response =  '<html>'
	if password_match:
		response += '  <h1>Thank you for registering!</h1>'
	else:
		response += '  <h1>Problem with the registration</h1>'
	response += '</html>'
	return response

app.run()