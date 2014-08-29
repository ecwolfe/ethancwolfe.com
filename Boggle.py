#! /usr/bin/env python
# Ethan Wolfe

import sys
import random

class Boggle:
	dictionary = []
	solvedWords = []
	boggleBoard = []


	def __init__(self):

		# Notice the second dice has Q instead of Qu
		dice =  ['FORIXB', 'MOQABJ', 'GURILW', 'SETUPL', 'CMPDAE', 'ACITAO', 'SLCRAE', 'ROMASH', 'NODESW', 'HEFIYE', 'ONUDTK', 'TEVIGN', 'ANEDVZ', 'PINESH', 'ABILYT', 'GKYLEU']
		
		results = [d[random.randrange(0,6)] for d in dice]
		random.shuffle(results)

		self.boggleBoard = [['' for y in xrange(4)] for x in xrange(4)]

		count = 0

		for l in xrange(0,4):
			for k in xrange(0,4):
				self.boggleBoard[l][k] = results[count]
				count += 1
		
		
	def getBoard(self):
		return self.boggleBoard

	def clearWordList(self):
		self.solvedWords = []
		words = []

	def getNeighbors(self,row, col):
		neigh = []
		for i in xrange(0,3):
			for j in xrange(0,3):
				newRow = (row - 1) + i
				newCol = (col - 1) + j
				if (newRow>0 and newRow<4 and newCol>0 and newCol<4):
					neigh.append([newRow,newCol])
		return neigh

	def isWord(self,inWord):
		left = 0
		right = len(self.dictionary)

		while (left <= right):
			middle = (left + right)/2
			#print left
			#print right
			if( inWord > self.dictionary[middle] ):
				left = middle + 1
			elif( inWord < self.dictionary[middle] ):
				right = middle - 1
			else:
				return True

		return False

	def wordSearch(self,x,y,testWord):

		if(len(testWord)>2):
			if(self.isWord(testWord)):
				if testWord not in self.solvedWords:
					self.solvedWords.append(testWord)
		if(len(testWord)>7):  # MAX_WORD_LENGTH
			return
		testWord += self.boggleBoard[x][y]
		temp = self.boggleBoard[x][y]
		self.boggleBoard[x][y] = ''
		neighbors = self.getNeighbors(x,y)
		#print neighbors
		for p in xrange(0,len(neighbors)):
			a = neighbors[p][0]
			s = neighbors[p][1]
			if (len(self.boggleBoard[a][s])>0):
				#print testWord
				self.wordSearch(a,s,testWord)
		self.boggleBoard[x][y] = temp


	def playGame(self):

		f = open ('sowpods.txt','r')

		for line in f:
			self.dictionary.append(line.rstrip('\r\n'))

		f.close()

		for l in xrange(0,4):
			for k in xrange(0,4):
				self.wordSearch(l,k,'')

		words = self.solvedWords
		
		return sorted(words)
