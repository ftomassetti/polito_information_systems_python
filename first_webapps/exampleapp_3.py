from flask import Flask,request

app = Flask('MyMagicalApp')
app.debug = True

@app.route('/homepage')
def send_the_homepage():
    print("SERVER: processing the request for an homepage")
    #print("\nRequest methods:")
    #print(dir(request))
    #print("-------------\n")	
    print("\taccepted languages : "+str(request.accept_languages))
    print("\tcookies            : "+str(request.cookies))
    print("\thost url           : "+request.host_url)
    print("\treferrer           : "+str(request.referrer))
    for k,v in request.headers:
    	print("\t[header] %s = %s" % (k,v))
    return "This is the homepage; enjoy!"

@app.route('/contacts')
def send_the_contacts():
    print("SERVER: processing the request for the contacts page")	
    return "My contacts are: phone +55 01234, e-mail wonderful.programmer@polito.it"


app.run()