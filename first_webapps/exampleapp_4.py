from flask import Flask,request

app = Flask('MyMagicalApp')
app.debug = True

def get_list_of_all_news():
	# I should take them from the DB!
	news = [
		{'title':'Torino FC stops Roma!',
		 'topic':'Sport',
		 'text' :'What a great match'},
		{'title':'Linux Kernel 3.12.0 is out',
		 'topic':'Technology',
		 'text' : 'New support for...'},
		{'title':'Trying the Ferrari Enzo',
		 'topic':'Motors',
		 'text' : 'It is fast'}
	]
	return news

def get_interests_of_user():
	# I should take them from the DB!	
	interests = ['Sport','Motors']
	return interests

@app.route('/shownews')
def send_list_of_news():
	news = get_list_of_all_news()
	interests = get_interests_of_user()
	selected_news = []
	for n in news:
		if n['topic'] in interests:
			selected_news.append(n)

	response = "<html><h1>Selected news</h1>"
	for sn in selected_news: 
		response += "<h2>%s</h2>" % sn['title']
		response += "<p>%s</p>" % sn['text']
	response += "</html>"
	return response

app.run()