#!/usr/bin/python3
import string
import random
from time import sleep

__author__ = 'Milosz Chodkowski PUT'

LETTERS = string.ascii_uppercase + ' ' + '.'
DEFAULT_SENTENCE = 'METHINKS IT IS LIKE A WEASEL.'


def hammingDist(sentence):
    count = 0
    for char1, char2 in zip(sentence, DEFAULT_SENTENCE):
        if char1 != char2:
            count += 1
    return (count, sentence)


def generateSentence():
    new_sentence = ''.join(random.choice(LETTERS) for i in range(28))
    return new_sentence


def solve():
    generation = 0
    best_dist, best_solution = len(LETTERS), LETTERS

    while best_dist > 0:
        sentence = generateSentence() if not generation else best_solution
        sentences, new_l = [sentence for i in range(100)], list()
        for word in sentences:
            word = list(word)
            word[random.randint(0, len(word) - 1)] = random.choice(LETTERS)
            new_l.append(''.join(word))
            solutions = map(hammingDist, new_l)
            for sol in solutions:
                if sol[0] < best_dist:
                    best_dist = sol[0]
                    best_solution = sol[1]
        sleep(0.1)
        print(generation + 1, best_solution)
        generation += 1


if __name__ == '__main__':
    solve()
