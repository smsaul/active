import random

masterwordlist = []

def loadwordlist():
	global masterwordlist
	masterwordlist = [line.strip() for line in open("wordlist.txt", 'r')]

def pwgen():
	word_string = []
	for i in range(4):
		ran_word = random.choice(masterwordlist)
		word_string.append(ran_word)
	return word_string
