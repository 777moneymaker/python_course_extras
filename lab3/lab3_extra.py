#!/usr/bin/python3
'''Module written as an extra exercise for AMU's Python course.

Script opens 10 files in 'data' folder.
Then count's G/C percentage for every file.
'''
import os
from pathlib import Path

from Bio import SeqIO

__author__ = 'Milosz Chodkowski PUT'

def main():
    for file in Path('./data').iterdir():
        seq = next(SeqIO.parse(file, 'genbank')).seq
        count = seq.count('G') + seq.count('C')
        print(f'{file.stem} GC%: {count/len(seq) * 100 :.3f}')
if __name__ == '__main__':
    main()
