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
	#load the lowtops.html file, this will be changed to the respective page soon enough.
	return render_template('lowtops.html')



@app.route("/shoe/id=<shoeID>")
def loadShoeFromJson(shoeID = None):
    #translate shoeID into a string so we can parse json using it. Honestly so suprised that worked.
    shoeID = "" + shoeID + ""
    
    #load the json file for manipulation
    with open('shoes.json', 'r') as jsonData:
        shoeData = json.load(jsonData)
        
    #now we've got the json file, get the exact values for the Shoe
    #shoe name
    ShoeName = shoeData[shoeID]['name']
    shoeNameHandler = {'shoeName': ShoeName}
    
    #shoe colours
    coloursAvailable = shoeData[shoeID]['colours']
    shoeColourHandler = {'colours': coloursAvailable}
    
    #size range
    #first size
    sizeRange1 = shoeData[shoeID]['size-1']
    sizeRange1Handler = {'size1': sizeRange1}	

   #last size
    sizeRange2 = shoeData[shoeID]['size-2']
    sizeRange2Handler = {'size2': sizeRange2}
    #end size range

    return render_template('shoe-detail.html', shoe = shoeNameHandler, colour = shoeColourHandler, size1 = sizeRange1Handler, size2 = sizeRange2Handler)


@app.errorhandler(404)
def uhOh(error):
	return render_template('404.html'), 404


if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)