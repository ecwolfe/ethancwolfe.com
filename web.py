#!flask/bin/python
#!/usr/bin/python
# Author: Ethan Wolfe
# 08/24/14

from flask import Flask, render_template, url_for, request, redirect
import Boggle
import monkey
import threading

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
	Boggle.clearGame()
	boggleBoard = ''
	solutions = ''
	boggleBoard = Boggle.setupBoggle()
	solutions = Boggle.playGame(boggleBoard)
	if request.method=='POST':
		Boggle.clearGame()
		boggleBoard = Boggle.setupBoggle()
		solutions = Boggle.playGame(boggleBoard)
		return render_template('boggle.html', bb = boggleBoard, sol = solutions)
	return render_template('boggle.html', bb = boggleBoard, sol = solutions)

@app.route('/monkey')
def markov():
	output = monkey.monkeyWrite(7,100,'Meta-excerpt.txt')
	return render_template('monkey.html', re = output)

"""
@app.route('/boggle',methods = ['POST'])
def reboggle():
	boggleBoard = Boggle.setupBoggle()
	solutions = Boggle.playGame(boggleBoard)
	return render_template('boggle.html', bb = boggleBoard, sol = solutions)
"""

app.run(debug=True)
