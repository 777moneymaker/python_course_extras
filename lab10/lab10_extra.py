#!/usr/bin/python3
import os
import re

__author__ = 'Milosz Chodkowski'

if __name__ == '__main__':
	pattern = re.compile('[RKS][YFW][CTGH][VIL][FV]G[ADN].[VIL]....[KR]')
	for file in os.listdir('./GC'):
		with open(os.path.join('./GC', file), 'r') as fh:
			for match in re.finditer(pattern, fh.read()):
				print(f'{file} {match.group()} {match.span()}')
