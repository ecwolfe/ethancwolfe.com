#!flask/bin/python
#!/usr/bin/python
# Author: Ethan Wolfe
# 08/24/14

from flask import Flask, render_template, url_for, request, redirect
import Boggle
import monkey

app = Flask(__name__)


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
	output = monkey.monkeyWrite(7,100,fIn)
	return render_template('monkey.html', re = output)

@app.route('/output', methods= ['GET','POST'])
def output():
	if request.method=='POST':
		k = request.form['k']
		length = request.form['length']
		file = request.files['fileIn']
		output = monkey.monkeyWrite(int(k),int(length),file)
	return render_template('output.html', re = output)

app.run(debug=True)
