from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def loadIndex():
	return render_template('index.html')

@app.route("/browse")
def loadBrowse():
	return render_template('all-shoes.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)

	
