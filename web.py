#!flask/bin/python
#!/usr/bin/python
# Author: Ethan Wolfe
# 08/24/14

from flask import Flask, render_template, url_for, request, redirect
from werkzeug import secure_filename
import Boggle
import monkey

app = Flask(__name__)

@app.errorhandler(404)
def page_notfound(error):
	return render_template('error.html'), 404

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/projects')
def project():
	return render_template('projects.html')

@app.route('/boggle', methods = ['GET', 'POST'])
def boggle():
	b = Boggle.Boggle()
	b.clearWordList()
	if request.method=='POST':
		bBoard = b.getBoard()
		solutions = b.playGame()
		return render_template('boggle.html', bb = bBoard, sol = solutions)
	bBoard = b.getBoard()
	solutions = b.playGame()
	return render_template('boggle.html', bb = bBoard, sol = solutions)

@app.route('/monkey', methods= ['GET','POST'])
def markov():
	fIn = open("Meta-excerpt.txt", 'r')
	kval = 7
	ulength = 100
	if request.method=='POST':
		kval = request.form['kval'] 
		ulength = request.form['ulength']		
		try:
			kval = int(kval)
			ulength = int(ulength)
			if kval < 1 or ulength < 1:
				output = "Opps! Let me explain better: \nInput values must be greater than 0."
				return render_template('monkey.html', re = output,  k = kval, l = ulength, noError=False)
		except ValueError:
			output = "Opps! Let me explain better: \n Input values must be numbers."
			return render_template('monkey.html', re = output, k = kval, l = ulength, noError=False)
	output = monkey.monkeyWrite(kval,ulength,fIn)
	return render_template('monkey.html', re = output, k = kval, l = ulength, noError=True)

@app.route('/output', methods= ['GET','POST'])
def output():
	if request.method=='POST':
		k = request.form['k']
		length = request.form['length']
		fil = request.files['fileIn']
		try:
			k = int(k)
			length = int(length)
			if k < 1 or length < 1:
				output = "Opps! Let me explain better: \n Input values must be greater than 0."
				return render_template('output.html', re = output, noError = False)
		except ValueError:
			output = "Opps! Let me explain better: \n Input values must be numbers."
			return render_template('output.html', re = output, noError = False)
		output = "Oh Dear! Something has gone completely wrong."
		exten = fil.filename
		if exten[-4:] == ".txt":
			#fil = secure_filename(fil.filename)
			output = monkey.monkeyWrite(int(k),int(length),fil)
		else:
			output = "Opps! Let me explain better: \n Your file must end in .txt."
			return render_template('output.html', re = output, noError = False)
		
	return render_template('output.html', re = output, noError = True)

app.run(debug=True)
