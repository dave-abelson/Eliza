from flask import Flask, render_template
import os
import sys

app = Flask(__name__)
#root = os.path.dirname(__file__)
#template_path = os.path.join(root, 'eliza/templates')
#app = Flask(__name__, template_folder= template_path)
@app.route("/")
def hello():
	return "FINALLY"

@app.route('/eliza/')
def eliza():
	return render_template('eliza.html')

if __name__=="__main__":
	#app.run(host='0.0.0.0', port=80)
	app.run(debug = True)
