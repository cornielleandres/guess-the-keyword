import os
import random

def get_random_word():
	dir = os.path.dirname(__file__) # get current directory
	file_path = os.path.join(dir, 'words.txt') # get path to words.txt

	fp = open(file_path, 'r')

	num_of_words = int(fp.readline()) # first line tells you the number of words

	random_line = random.randrange(0, num_of_words)

	for i, line in enumerate(fp):
		if i == random_line:
			random_word = line
			break

	fp.close()

	return random_word[:-1] # remove the newline at the end
