from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from random import choice

#create connection to Mongo Database
client = MongoClient('mongodb://localhost:8080/')
db= client.eaters
col = db['eaters'] 
#creates eater column or collection called


app = Flask(__name__)
app.debug = True

"""
r = get('http: chartbeat.com/somerandomurl')
json = r.json()
terms = [' '.join(term['grams'])
	   for term in json['data'][]top_terms'][technology']]
"""

@app.route('/', methods=['GET', 'POST'])
def hello():
	if request.method == 'GET':
		return render_template('index.html')

	if request.method =='POST':
		for name, school, dhall, checkedin in request.form.iteritems():
		#for each pair in dictionary

			hasCheckedin = col.find({'name': name})
			if not hasCheckedin:
			#initialize new eater
				eater = {
					'name' : name,
					'school' : school,
					'dhall' : NULL,
				}
			if checkedin == True:
				eater['dhall'] = dhall
			else: 
				eater['dhall'] = NULL
		#col.insert(eater)
			col.update({'name': name}, eater, upsert = True)

		 # redirect to the results page
         	return redirect(url_for('results'), dhall = dhall)


@app.route('/results')
def results():
	eaters = col.find({})
	return render_template('results.html', html, dhall = dhall, eaters = eaters)
	
if __name__ == '__main__':
	app.run()
