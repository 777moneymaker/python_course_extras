#!/usr/bin/python3
import string
import random

__author__ = 'Milosz Chodkowski PUT'

LETTERS = string.ascii_uppercase + string.punctuation + ' '
with open('sentence.txt', 'r') as fh:
    TARGET_SENTENCE = fh.read()

def hammingDistance(sentence):
    count = sum(c1 != c2 for c1, c2 in zip(sentence, TARGET_SENTENCE))
    return (count, sentence)


def generateRandomSentence():
    return ''.join(random.choice(LETTERS) for i in range(len(TARGET_SENTENCE)))


def solve():
    iteration = 0
    best_dist, best_solution = len(TARGET_SENTENCE) + 1, generateRandomSentence() # len == 27 + 1

    while best_dist > 0:
        sentences = [best_solution] * 100
        for mark in sentences:
            mark = list(mark)
            mark[random.randint(0, len(mark) - 1)] = random.choice(LETTERS)
            sentences.append(''.join(mark)) 
            del sentences[0]
        
        solutions = map(hammingDistance, sentences)
        for sol in solutions:
            if sol[0] < best_dist:
                best_dist, best_solution = sol[0], sol[1] 
        iteration += 1
        print(iteration, best_solution)


if __name__ == '__main__':
    solve()