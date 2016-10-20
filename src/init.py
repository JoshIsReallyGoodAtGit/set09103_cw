from flask import Flask, render_template, json

app = Flask("__name__")

@app.route("/")
def loadIndex():
	return render_template('index.html')

@app.route("/browse/")
def loadBrowse():
	#feature idea: load one of the shoes from each category here, instead of hard-coding them
	return render_template('all-shoes.html')

    
@app.route("/browse/<category>")
def loadSpecificCategory(category = None):
	with open ('shoes.json', 'r') as jsonDataFile:
		shoes = json.load(jsonDataFile)
        return render_template('category.html', category = category, shoes = shoes)
        
@app.route("/shoe/<category>/<shoeID>")
def loadShoeFromJson(category = None, shoeID = None):

    #load the json file for manipulation
    with open('shoes.json', 'r') as jsonData:
        shoes = json.load(jsonData)
    
    for shoe in shoes:
        if shoes[shoeID]['name'] == "":
            def force404():
                abort(404)
                
    name = shoes[shoeID]['name']
    return render_template('shoe-detail.html', category = category, name=name, shoes = shoes)



@app.errorhandler(404)
def uhOh(error):
	return render_template('404.html'), 404


if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)