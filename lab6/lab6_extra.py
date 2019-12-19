#!/usr/bin/python3

from typing import List, Tuple

__author__ = 'Milosz Chodkowski PUT'

def remove_all_occurences(array: list, val: object) -> list:
	"""Remove all occureences of value in given list.

	Args:
		param1 (list): List in which value should be removed.
		param2 (object): Value which has to be removed.

	Returns:
		list: list without given value.
	"""
	return [x for x in array if x != val]

def get_all_substrings(sequence: str) -> list:
	"""Get every substring from sequence.

	Args:
		param (str): Sequence from which every substring should be sliced.

	Returns:
		list: Every substring that can be created from given sequence.
	"""
	return [sequence[i: j] for i in range(len(sequence)) for j in range(i + 1, len(sequence) + 1)]

def complement(sequence: str) -> str:
	"""Get complementary DNA sequence.

	Args:
		param (str): DNA sequence:

	Returns:
		str: Complementary sequence.
	"""
	complement_bases = {'A': 'T','T': 'A', 'C': 'G', 'G': 'C'}
	return ''.join(complement_bases[base] for base in sequence.upper())

def reverse_complement(sequence: str) -> str:
	"""Get reversed complementary DNA sequence.

	Args: 
		param (str) DNA sequence.

	Returns:
		str: Reversed complementary sequence.
	"""
	return complement(sequence)[::-1]

PalindromeList = List[Tuple[int, int, str]]
def restriction_sites(sequence: str) -> PalindromeList:
	"""Get every palindrome sub-sequence with given property: 4 <= len(param) <= 12.

	Args:
		param (str): DNA sequence.

	Returns:
		PalindromeList: starting index, ending index, palindrome sub-sequence.
	
	Example:
		[(4, 7, 'TGCA')]
	"""
	results, substrings = list(), get_all_substrings(sequence)

	# Delete invalid susbstrings.
	for chop in substrings:
		if len(chop) > 12 or len(chop) < 4:
			substrings = remove_all_occurences(substrings, chop)

	for chop in substrings:
		for i in range(len(sequence)):
			# Found in slice, equal to reverse_complement.
			if chop in sequence[i:len(chop)+i] and chop == reverse_complement(chop):
				start, end = i+1, len(chop)+i
				final = (start, end, chop)
				# Only unique.
				if final not in results:
					results.append(final)
	# Sort by start value.
	return sorted(results, key=lambda x: x[0])


if __name__ == '__main__':
	dna = 'TCAATGCATGCGGGTCTATATGCAT'
	slices = restriction_sites(dna)
	for chop in slices:
		print(chop)