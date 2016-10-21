from flask import Flask, render_template, json

app = Flask("__name__")

@app.route("/")
def loadIndex():
	return render_template('index.html')

@app.route("/browse/")
def loadBrowse():
	#feature idea: load one of the shoes from each category here, instead of hard-coding them
        
        #take one shoe from each category and send 'em to all-shoes.html
        with open('shoes.json', 'r') as jsonFile:
                shoes = json.load(jsonFile)
        target1 = "1"
        target2 = "8"
        target3 = "12"
        target4 = "19"
        target5 = "23"
        
        shoe1Img = shoes[target1]['background-img']
        shoe2Img = shoes[target2]['background-img']
        shoe3Img = shoes[target3]['background-img']
        shoe4Img = shoes[target4]['background-img']
        shoe5Img = shoes[target5]['background-img']
        
	return render_template('all-shoes.html', shoe1Img = shoe1Img, shoe2Img = shoe2Img, shoe3Img = shoe3Img, shoe4Img = shoe4Img, shoe5Img = shoe5Img, shoes=shoes)

    
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
        
    name = shoes[shoeID]['name']
    return render_template('shoe-detail.html', category = category, name=name, shoes = shoes)



@app.errorhandler(404)
def uhOh(error):
	return render_template('404.html'), 404


if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)