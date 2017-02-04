from flask import Flask, render_template, request
import os
import sys
import time

app = Flask(__name__)
@app.route("/")
def hello():
	return "FINALLY"

@app.route('/eliza/', methods=['GET', 'POST'])
def eliza():
	if request.method == "POST":
		name = request.form['name']
		date = time.strftime("%c")
		return render_template('elizapost.html', name=name, date=date)
	else:
		return render_template('eliza.html')

if __name__=="__main__":
	#app.run(host='0.0.0.0', port=80)
	app.run(debug = True)
