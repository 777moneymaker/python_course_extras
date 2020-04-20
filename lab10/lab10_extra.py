#!/usr/bin/python3
import re

from pathlib import Path

__author__ = 'Milosz Chodkowski'

if __name__ == '__main__':
	pattern = re.compile('[RKS][YFW][CTGH][VIL][FV]G[ADN].[VIL]....[KR]')
	for file in Path('./GC').iterdir():
		for match in re.finditer(pattern, file.read_text()):
			print(f'{file.stem} {match.group()} {match.span()}')