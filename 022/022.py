# -*- coding: utf-8 -*-

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

# learned how to interact with files in python
# learned how to dump object into JSON file in python by importing json module

import json

def sort():
	names = [] # empty list, will append to later
	currentName = "" # initialize empty string
	log = False # variable that represents whether we are currently logging a name iteratively

	originalNames = open("names.txt", 'r').read() # convert file into string

	size = len(originalNames) # get size of file that was converted to string

	for x in range(0, size):
		if (originalNames[x] == '"' and log == False):
			log = True # start taking new name
		elif (originalNames[x] == '"' and log == True):
			log = False # done taking name, append to list
			names.append(currentName)
			currentName = ""
		elif (log == True):
			currentName += originalNames[x] # add to currentName

	names = sorted(names) # sort the names list

	outFile = open("sorted_names.json", 'w') # open file for writing

	outFile.write(json.dumps(names)) # use json to dump object into file

	outFile.close()

def score():
	score = 0 # initialize score variable, will add to later

	with open("sorted_names.json", 'r') as file: # open file for reading
		read = json.load(file) # load json file into list variable

		for x in range(0, len(read)): # iterate through each name in list
			nameScore = 0; # initialize nameScore variable, will add to later
			positionScore = x+1 # corresponds to spot in the list

			for y in range(0, len(read[x])): # iterate through each character in the current name
				nameScore += (ord(read[x][y].lower())-96) # add each alphabetic value in the name to the nameScore variable

			score += nameScore*positionScore # find the score for the name by multiplying the sum of the alphabetic values by the position in the list
		file.close()

	print score

sort()
score()