#!/usr/bin/python3
'''Module written as an extra exercise for AMU's Python course.'''

__author__ = 'Milosz Chodkowski PUT'
__field__ = 'Bioinformatics'
__version__ = 1.0

def main():
	with open('lotto_history.txt', 'r') as fh:
		RESULTS = [line.split(' ')[2].rstrip() for line in fh.readlines()]
		NUMBERS = [int(num) for line in RESULTS for num in line.split(',')]

	counters = list(map(lambda x: (x, NUMBERS.count(x)), set(NUMBERS)))
	print(sorted(counters, key=lambda x: x[1], reverse=True)[:10])


if __name__ == '__main__':
	main()