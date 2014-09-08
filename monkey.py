#! /usr/bin/env python
# Ethan Wolfe

import sys
import random

def monkeyWrite(k, length, f):					# k: level of simlarity, length: how long new text should be, f: file to read

	source = ''

	for line in f:
		source += line.rstrip('\n')			# Loads text from file into source

	f.close()

	if ( len(source) < 1):					# Error Handling
		result = "Opps Let me explain better your document must have some length to it."
		return result

	randOne = random.randint(0,len(source))			# Random Seed One
	randTwo = random.randint(0,len(source))			# Random Seed Two

	l = 0							# counter for number of chars in text
	seed = ''						# The seed of text to look for
	compare = ''						# The current section of text being looked at
	storage = ''						# Possible next letters
	result = ''						# Final Text

	for i in xrange(0,k):
		seed += source[randOne + i]			# Fills seed from random point in source text 

	while  len(result) < length:				# Checks if result is long enough
		while l < len(source):				# Checks that source still has text left
			while l < k:			 	# Fills compare from start of text
				compare += source[l]
				l = l + 1
			if seed.lower() == compare.lower():	# If seed is equal then add next letter in text to storage
				storage += source[l]
			compare = compare[1:]			# Deque first letter of compare
			compare += source[l]			# Enque next letter of the text
			l = l + 1				
		if len(storage) == 0:				# If no matches were found to seed Second Random Seed
			seed = ''
			randTwo = random.randint(0,len(source))
			for i in xrange(0,k):
				seed += source[randTwo + i]
		else:							# If a match is found:
			randOne = random.randint(0,len(storage)-1)		# Choose a random letter from storage
			result += storage[randOne]				# Add letter to the final result
			seed = seed[1:]						# Deque first letter of seed
			seed += storage[randOne]				# Enque selected letter to seed
			storage = ''						# Clear storage					
		l = 0						# After each completion of text
		compare = ''					# Reset all values to look through list

	return result
