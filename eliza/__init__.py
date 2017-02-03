from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	return "FUCKING FINALLY"

@app.route('/eliza/')
def eliza():
	return "ELIZA"

if __name__=="__main__":
	app.run(host='0.0.0.0', port=80)

