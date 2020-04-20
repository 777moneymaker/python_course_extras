#!/usr/bin/python3
'''Module written as an extra exercise for AMU's Python course.'''

import string
import random

__author__ = 'Milosz Chodkowski PUT'

LETTERS = string.ascii_uppercase + ' '
TARGET_SENTENCE = 'METHINKS IT IS A WEASEL'

def hamming_distance(sentence):
    count = sum(c1 != c2 for c1, c2 in zip(sentence, TARGET_SENTENCE))
    return count, sentence

def generate_random_sentence():
    return ''.join(random.choice(LETTERS) for _ in range(len(TARGET_SENTENCE)))

def main():
    iteration = 0
    best_dist = len(TARGET_SENTENCE)
    best_solution = generate_random_sentence()
    length = len(TARGET_SENTENCE)
    while best_dist > 0:
        sentences = [best_solution] * 100
        for sentence in sentences:
            sentence = list(sentence)
            sentence[random.choice(range(length))] = random.choice(LETTERS)
            sentences.append(''.join(sentence)) 
            del sentences[0]
        
        solutions = map(hamming_distance, sentences)
        for sol in solutions:
            if sol[0] < best_dist:
                best_dist, best_solution = sol[0], sol[1] 
        iteration += 1
        print(iteration, best_solution)


if __name__ == '__main__':
    main()