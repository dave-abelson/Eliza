from flask import Flask, render_template, request, jsonify
import os
import sys
import time
import random

responses = [
	'I am fucking ELIZA',
	'Hello, buddy'

]

app = Flask(__name__)
@app.route("/")
def hello():
	return "FINALLY"

@app.route('/eliza/', methods=['GET', 'POST'])
def eliza():
	if request.method == "POST":
		name = request.form['name']
		date = time.strftime("%c")
		return render_template('DOCTOR.html', name=name, date=date)
	else:
		return render_template('eliza.html')

@app.route('/eliza/DOCTOR/', methods=['GET', 'POST'], strict_slashes=False)
def doctor():
#	content = request.get_json(silent=True)
#	print content
#	return render_template('DOCTOR.html')
	return jsonify(
		eliza = random.choice(responses)
	)
if __name__=="__main__":
	#app.run(host='0.0.0.0', port=80)
	app.run(debug = True)
