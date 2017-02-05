from flask import Flask, render_template, request, jsonify
import os
import sys
import time
import random
import json

responses = [
	'How does that make you feel?',
	'Interesting, tell me more.',
	'Do you blame your mother for that?',
	'Do you blame your father for that?',
	'Perhaps you are experiencing insomnia.',
	'Dehydration may lead to that',
	'Exercise and a healthy diet will fix that.',
	'You may be projecting.',
	'My book has a chapter that covers that.',
	'Can you elaborate?',
	'Why do you say that?',
	'Please, continue.',
	'It sounds like an anger issue.',
	'How was yesterday?',
	'Do you really feel that way?',
	'Did you have a good relationship with your parents?',
	'So what brought you here today?',
	'What would make the problem better?',
	'In general, how would you say your mood has been?',
	'What are you expecting from this session?',
	'Interesting.',
	'Mmmhm, go on.',
	'I can\'t tell you that.'
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
	#if request.method =="POST":
	#	input = request.data
	#	
	#	return jsonify( eliza = len(input))
	#else:
	return jsonify(	eliza = random.choice(responses))
if __name__=="__main__":
	app.run(debug = True)
