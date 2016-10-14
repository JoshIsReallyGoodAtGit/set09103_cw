from flask import Flask, render_template
import json

app = Flask("__name__")

@app.route("/")
def loadIndex():
	return render_template('index.html')

@app.route("/browse")
def loadBrowse():
	return render_template('all-shoes.html')


@app.route("/allshoes/<name>")
def loadSpecificCategory(name):
	#load the lowtops.html file
	return render_template('lowtops.html')

#I can't seem to get ?id=<shoeID> to work, so I'm using a slash instead for
#the time being

#@app.route("/shoe/id=<shoeID>")
#def loadSpecificShoe(shoeID):
	#load the specifc show, but for now just print out the shoe ID
	#return render_template('shoe-detail-1.html')
#def loadShoeFromJson(shoeID):
#	with open('shoes.json', 'r') as jsonData:
        #dump the jsonData into a string
        #shoeDump = json.dumps(jsonData)

        #now load the data into a string
	       # with open('shoes.json', "r") as f:
        	#	shoeName = json.load(f)
       		#	for i in shoeName:
                #		if i['id'] == '01':
                 #      			shoeName = i['name']
		#			print(shoeName, file=sys.stderr)


@app.errorhandler(404)
def uhOh(error):
	return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)

	
