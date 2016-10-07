from flask import Flask, render_template
app = Flask(__name__)

@app.route("/test/render/")
def renderCheck():
	return render_template('nav.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0')

