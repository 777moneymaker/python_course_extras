#!/usr/bin/python3
import string
import random
from time import sleep

__author__ = 'Milosz Chodkowski PUT'

LETTERS = string.ascii_uppercase + ' '
TARGET_SENTENCE = 'METHINKS IT IS LIKE A WEASEL'

def hammingDistance(sentence):
    return sum(c1 != c2 for c1, c2 in zip(sentence, TARGET_SENTENCE)), sentence


def generateRandomSentence():
    return ''.join(random.choice(LETTERS) for i in range(len(TARGET_SENTENCE)))


def solve():
    iteration = 0
    best_dist, best_solution = len(LETTERS) + 1, LETTERS # len == 27 + 1

    while best_dist > 0:
        random_sentence = generateRandomSentence() if not iteration else best_solution
        new_l, sentences = list(), [random_sentence] * 100
        for mark in sentences:
            mark = list(mark)
            mark[random.randint(0, len(mark) - 1)] = random.choice(LETTERS)
            new_l.append(''.join(mark))
        solutions = map(hammingDistance, new_l)
        for sol in solutions:
            if sol[0] < best_dist:
                best_dist, best_solution = sol[0], sol[1] 
        iteration += 1
        print(iteration, best_solution)


if __name__ == '__main__':
    solve()