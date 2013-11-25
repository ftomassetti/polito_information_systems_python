from flask import Flask,request,get_flashed_messages,redirect
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo
from flask import render_template

app = Flask("MyApp")
app.debug = True

def get_posts():
	post1 = {'title':'What is MVC?','abstract':'''The Model View Controller (MVC) is
		the most used design pattern for web applications. It divided responsabilities
		among three components: the model, which is entitled to manage the data,
		the view which should represent the data in a form comprehensible to the users
		and the controller which wires everything together'''}
	post2 = {'title':'Forms','abstract':'''Forms permit to send data to the server.
		They are normally sent using the post method. Data have to be validated. In the typical
		scenario the server keep showing the form to the user until it feels it correctly.'''}
	post3 = {'title':'Templates','abstract':'''Templates are really useful, without them
		we are stuck at composing HTML in string inside a python script. That feels awkward.'''}				
	return [post1,post2,post3]

@app.route('/posts')
def show_posts():
	return render_template('posts_static.html')

@app.route('/postsdyn')
def show_posts_dynamic():
	return render_template('posts_dynamic.html',posts=get_posts())	


app.run()