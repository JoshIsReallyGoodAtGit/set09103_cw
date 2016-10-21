from flask import Flask, render_template, json

app = Flask("__name__")

@app.route("/")
def loadIndex():
        #the 'root' route!
	return render_template('index.html')

    
@app.route("/browse/")
def loadBrowse():
        #take one shoe from each category and send 'em to all-shoes.html
        with open('shoes.json', 'r') as jsonFile:
                shoes = json.load(jsonFile)
                
        #hardcode the shoe IDs. This saves me from creating a very complex algorithm to find the first shoe in each category. 
        target1 = "1"
        target2 = "8"
        target3 = "12"
        target4 = "19"
        target5 = "23"
        target6 = "26"
        
        #now take the thumbnail of each shoe and send it to shoe-detail.html
        shoe1Img = shoes[target1]['background-img']
        shoe2Img = shoes[target2]['background-img']
        shoe3Img = shoes[target3]['background-img']
        shoe4Img = shoes[target4]['background-img']
        shoe5Img = shoes[target5]['background-img']
        shoe6Img = shoes[target6]['background-img']
        
        #return the template
	return render_template('all-shoes.html', shoe1Img = shoe1Img, shoe2Img = shoe2Img, shoe3Img = shoe3Img, shoe4Img = shoe4Img, shoe5Img = shoe5Img, shoe6Img = shoe6Img, shoes=shoes)

    
    
@app.route("/browse/<category>")
def loadSpecificCategory(category = None):
	with open ('shoes.json', 'r') as jsonFile:
		shoes = json.load(jsonFile)
                
        #same as before, only less complex
        return render_template('category.html', category = category, shoes = shoes)
        
        
        
@app.route("/shoe/<category>/<shoeID>")
def loadShoeFromJson(category = None, shoeID = None):
    #load the json file for manipulation
    with open('shoes.json', 'r') as jsonFile:
        shoes = json.load(jsonFile)
    
    #load a specific shoe so the user can view all of it's information. Jinja will find the rest, so only the name and category are passed (as well as the shoes data)
    name = shoes[shoeID]['name']
    return render_template('shoe-detail.html', category = category, name=name, shoes = shoes)




@app.errorhandler(404)
def uhOh(error):
        #if the user lands on a page that doesn't exist, give them this error so they can be on their way.
	return render_template('404.html'), 404

#used to run the app


if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)