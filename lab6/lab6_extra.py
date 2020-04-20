#!/usr/bin/python3
'''Module written as an extra exercise for AMU's Python course.'''

from pathlib import Path
from Bio import SeqIO

__author__ = 'Milosz Chodkowski PUT'

def get_all_substrings(sequence):
	"""Get every substring from sequence.

	Args:
		sequence (str): Sequence containing substrings.

	Returns:
		list: Every substring that can be created.
	"""
	subs = [sequence[i:j] for i, char1 in enumerate(sequence) for j, char2 in enumerate(sequence, i+1)]
	subs = filter(lambda x: 4 <= len(x) <= 12, subs)
	return set(subs)

def complement(sequence):
	"""Get complementary DNA sequence.

	Args:
		sequence (str): DNA sequence:

	Returns:
		str: Complementary sequence.
	"""
	complement_bases = {'A': 'T','T': 'A', 'C': 'G', 'G': 'C'}
	return ''.join(complement_bases[base] for base in sequence.upper())

def reverse_complement(sequence):
	"""Get reversed complementary DNA sequence.

	Args: 
		sequence (str) DNA sequence.

	Returns:
		str: Reversed complementary sequence.
	"""
	return complement(sequence)[::-1]

def restriction_sites(sequence):
	"""Get every palindrome sub-sequence with given property: 4 <= len(param) <= 12.

	Args:
		sequence (str): DNA sequence.

	Returns:
		PalindromeList: starting index, ending index, palindrome sub-sequence.
	"""
	results = set()
	substrings = get_all_substrings(sequence)
	
	for chop in substrings:	
		length = len(chop)
		for i, char in enumerate(sequence):
			if chop == sequence[i : i+length] and chop == reverse_complement(chop):
				final = (i+1, i+length, str(chop))
				results.add(final)
	return results


if __name__ == '__main__':
	file = Path(__file__).parent.joinpath('fasta.txt')
	seq = next(SeqIO.parse(file, 'fasta')).seq
	slices = restriction_sites(seq)
	print(*sorted(slices), sep='\n')