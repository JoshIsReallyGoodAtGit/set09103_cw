from flask import Flask, render_template, json

app = Flask("__name__")

@app.route("/")
def loadIndex():
	return render_template('index.html')

@app.route("/browse")
def loadBrowse():
	#feature idea: load one of the shoes from each category here, instead of hard-coding them
	return render_template('all-shoes.html')


    
@app.route("/browse/<category>")
def loadSpecificCategory(category = None):
	with open ('shoes.json', 'r') as jsonDataFile:
		shoes = json.load(jsonDataFile)
                
        #THIS IS no longer A FUCKING NIGHTMARE. 
        return render_template('category.html', category = category, shoes = shoes)
        
@app.route("/shoe/<category>/<shoeID>")
def loadShoeFromJson(category = None, shoeID = None):
    #translate shoeID into a string so we can parse json using it. Honestly so suprised that worked.
    shoeID = "" + shoeID + ""

    #load the json file for manipulation
    with open('shoes.json', 'r') as jsonData:
        shoeData = json.load(jsonData)
        
        name = shoeData[shoeID]['name']
    return render_template('shoe-detail.html', category = category, shoeID = shoeID, name=name)



@app.errorhandler(404)
def uhOh(error):
	return render_template('404.html'), 404


if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)