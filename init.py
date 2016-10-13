from flask import Flask, render_template, json

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

@app.route("/shoe/id=<shoeID>")
def loadSpecificShoe(shoeID):
	#load the specifc show, but for now just print out the shoe ID
	return render_template('shoe-detail-1.html')



if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)

	
