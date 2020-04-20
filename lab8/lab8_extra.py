#!/usr/bin/python3
'''Module written as an extra exercise for AMU's Python course.'''

from pathlib import Path

__author__ = 'Milosz Chodkowski PUT'

def main():
	file = Path(__file__).parent.joinpath('lotto_history.txt')
	
	with open(file, 'r') as fh:
		lines = [line.split(' ')[2].rstrip() for line in fh]
		numbers = [int(num) for line in lines for num in line.split(',')]
	
	f_count = lambda x: (x, numbers.count(x))
	results = map(f_count, set(numbers))
	print(*sorted(results, key=lambda x: -x[1])[:10], sep='\n')


if __name__ == '__main__':
	main()