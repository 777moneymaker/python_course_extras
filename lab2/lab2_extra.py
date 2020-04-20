#!/usr/bin/python3
'''
Module written as an extra exercise for AMU's Python course.
'''
__author__ = 'Milosz Chodkowski PUT'


def validate(seq = 'ATGC'):
    pars_map = {'(': ')'}
    stack, pars = [], []

    for char in seq:
        # If there is any other char than parentheses or dot
        if char not in ['.', '(', ')']:
            print(f'{char} is not allowed in dot bracket format!')
            return False
        elif char == '(' or char == ')':
            pars.append(char)

    for par in pars:
        if par in pars_map:
            stack.append(pars_map[par])
        # If stack empty or last bracket not valid
        elif not stack or par != stack.pop():
            return False
    return not stack

if __name__ == '__main__':
    print(validate('...(..)(..)...'))
