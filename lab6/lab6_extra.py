#!/usr/bin/python3

__author__ = 'Milosz Chodkowski PUT'

def remove_all_occurences(array, val):
	"""Remove all occureences of value in given list.

	Args:
	param1 (list): List in which value should be removed.
	param2 (number/string): Value which has to be removed.

	Returns:
	list: list without given value.
	"""
	return [x for x in array if x != val]

def get_all_substrings(sequence):
	"""Get every substring from sequence.

	Args:
	param (string): Sequence from which every substring should be sliced.

	Returns:
	list: Every substring that can be created from given sequence.
	"""
	return [sequence[i: j] for i in range(len(sequence)) for j in range(i + 1, len(sequence) + 1)]

def complement(sequence):
	"""Get complementary DNA sequence.

	Args:
	param (string): DNA sequence:

	Returns:
	string: Complementary sequence.
	"""
	complement_bases = {'A': 'T','T': 'A', 'C': 'G', 'G': 'C'}
	return ''.join(complement_bases[base] for base in sequence.upper())

def reverse_complement(sequence):
	"""Get reversed complementary DNA sequence.

	Args: 
	param (string) DNA sequence.

	Returns:
	string: Reversed complementary sequence.
	"""
	return complement(sequence[::-1])

def restriction_sites(sequence):
	"""Get every palindrome sub-sequence with given property: 4 <= len(param) <= 12.

	Args:
	param (string): DNA sequence.

	Returns:
	sorted list of tuples: starting index, ending index, palindrome sub-sequence.
	
	Example:
	[(4, 7, 'TGCA')]
	"""
	results, substrings = list(), get_all_substrings(sequence)

	for chop in substrings:
		if len(chop) > 12 or len(chop) < 4:
			substrings = remove_all_occurences(substrings, chop)

	for chop in substrings:
		for i in range(len(sequence)):
			if chop in sequence[i:len(chop)+i] and chop == reverse_complement(chop):
				start, end = i+1, len(chop)+i
				final = (start, end, chop)
				if final not in results:
					results.append(final)
	return sorted(results, key=lambda x: x[0])


if __name__ == '__main__':
	results = restriction_sites('TCAATGCATGCGGGTCTATATGCAT')
	for chop in results:
		print(chop)