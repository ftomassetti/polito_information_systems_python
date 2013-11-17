from flask import Flask

app = Flask('MyMagicalApp')

@app.route('/homepage')
def send_the_homepage():
    print("SERVER: processing the request for an homepage")	
    return "This is the homepage; enjoy!"

@app.route('/contacts')
def send_the_contacts():
    print("SERVER: processing the request for the contacts page")	
    return "My contacts are: phone +55 01234, e-mail wonderful.programmer@polito.it"


app.run()