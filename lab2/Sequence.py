#!/usr/bin/python3
'''
Module written as an extra exercise for AMU's Python course.
'''
__author__ = 'Milosz Chodkowski PUT'
___field__ = 'Bioinformatics'
___version___ = 1.0


class Sequence:
    def __init__(self, seq='..(..)..()..'):
        self.seq = seq

    def validate(self, seq=None):
        '''Return the boolean value of dot bracket validation.
        >>> S.validate('..()..')
        True'''
        seq = self.seq if seq is None else seq
        OPEN_PAR, CLOSED_PAR = '(', ')'
        pars_map, valid_chars = {'(': ')'}, {'(', ')', '.'}
        stack, pars = [], []

        for char in seq:
            # If there is any other char than parentheses or dot
            if char not in valid_chars:
                print(f'\'{char}\' not valid in dot bracket format!')
                return False
            if char == OPEN_PAR or char == CLOSED_PAR:
                pars.append(char)

        for par in pars:
            if par in pars_map:
                stack.append(pars_map[par])
            # If stack empty or last bracket not valid
            elif not stack or par != stack.pop():
                return False
        return not stack


if __name__ == '__main__':
    S = Sequence()
    print(S.validate('...(..)(..)...'))
