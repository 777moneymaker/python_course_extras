#!/usr/bin/python3
import string
import random
from time import sleep

__author__ = 'Milosz Chodkowski PUT'

LETTERS = string.ascii_uppercase + ' '
TARGET_SENTENCE = 'METHINKS IT IS LIKE A WEASEL'

def hammingDistance(sentence):
    count = 0
    for char1, char2 in zip(sentence, TARGET_SENTENCE):
        if char1 != char2:
            count += 1
    return tuple([count, sentence])


def generateRandomSentence():
    new_sentence = ''.join(random.choice(LETTERS) for i in range(len(TARGET_SENTENCE)))
    return new_sentence


def solve():
    first_genre = True
    best_dist, best_solution = len(LETTERS) + 1, LETTERS # len == 27 + 1
    best_solutions = list()

    while best_dist > 0:
        random_sentence = generateRandomSentence() if first_genre else best_solution
        new_l, sentences = list(), [random_sentence for i in range(100)]
        for mark in sentences:
            mark = list(mark)
            mark[random.randint(0, len(mark) - 1)] = random.choice(LETTERS)
            new_l.append(''.join(mark))
        solutions = map(hammingDistance, new_l)
        for sol in solutions:
            if sol[0] < best_dist:
                best_dist = sol[0]
                best_solution = sol[1]
                first_genre = False
                best_solutions.append(best_solution)
    return best_solutions


def main():
    results = solve()
    for i, result in enumerate(results, start=1):
        sleep(0.1)
        print(i, result)


if __name__ == '__main__':
    main()
