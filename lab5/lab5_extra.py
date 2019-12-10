#!/usr/bin/python3
import string
import random
from time import sleep

__author__ = 'Milosz Chodkowski PUT'

LETTERS = string.ascii_uppercase + ' '

def hammingDist(sequence):
	def_seq = 'METHINKS IT IS LIKE A WEASEL'
	count = 0
	for val1, val2 in zip(sequence, def_seq):
		if val1 != val2:
			count += 1
	return (count, sequence)

def generateSequence():
	val = ''.join(random.choice(LETTERS) for i in range(28))
	return val

def solve():
	generations = 0
	best_dist, best_solution = len(LETTERS), None

	while best_dist > 0:
		val = generateSequence() if not generations else best_solution
		sequences, new_l = [val for i in range(100)], list()
		for i in range(len(sequences)):
			word = list(sequences[i])
			word[random.randint(0, len(word) - 1)] = random.choice(LETTERS)
			new_l.append(''.join(word))
			solutions = map(hammingDist, new_l)
			for sol in solutions:
				if sol[0] < best_dist:
					best_dist = sol[0]
					best_solution = sol[1]
		sleep(0.1)
		print(generations + 1, best_solution)
		generations += 1

if __name__ == '__main__':
	solve()
			