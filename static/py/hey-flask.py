from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "200 ok. flask installed and running"

if __name__ == "__main__":
	app.run(host='0.0.0.0')
