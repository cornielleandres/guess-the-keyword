import os
import random

def get_random_word():
	dir = os.path.dirname(__file__) # get current directory
	file_path = os.path.join(dir, 'words.txt')

	fp = open(file_path, 'r')

	num_of_words = int(fp.readline()) # first line tells you the number of words

	random_line = random.randint(1, num_of_words + 1)

	random_word = fp.readline(1) # default random word will be the first one

	for i, line in enumerate(fp):
		if i == random_line:
			random_word = line
			break

	fp.close()

	return line[:-1] # remove the newline at the end
