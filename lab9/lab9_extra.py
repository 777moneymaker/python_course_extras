#!/usr/bin/python3
'''Module written as an extra exercise for AMU's Python course.'''

import random
import argparse

from Bio import SeqIO

__author__ = 'Milosz Chodkowski PUT'

def wrap(seq):
	'''Wraps the sequence by inserting the '\n' char

	Args:
		seq (str): Sequence to wrap.
	Returns:
		(str) Wrapped sequence.
	'''
	wraps = [char if i % 60 else '\n' for i, char in enumerate(seq, 1)]
	return ''.join(wraps)

def reverse_complement(seq):
	'''Generates the reverse complement sequence

	Args:
		seq (str): DNA sequence.
	Returns:
		(str) Reversed complementary sequence
	'''
	complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
	return ''.join([complement[char] for char in seq])[::-1]

def read_sequences(f_gen, f_ann, f_save, user_type):
	'''Retrieves the DNA sequence and annotations

	Method reads 2 files: sequence file and annotation file. It cuts the name (ex. >contig1) and sequence of each record.
	Then it parses the annotation file, reads the data and saves it.

	Args:
		f_gen (str): Input (gene) filename.
		f_ann (str): Input (annotation) filename.
		f_save (str): Save file.
		user_type (str): Feature user wants to retrieve (ex. CDS)
	Saves:
		(str): Information retrieved from f_gen and f_ann files.
	Returns:
		None
	'''
	with open(f_gen, 'r') as fh_gen, open(f_ann, 'r') as fh_ann, open(f_save, 'w') as fh_save:
		CONTIGS = {}
		for record in SeqIO.parse(fh_gen, 'fasta'): 
			CONTIGS[record.name] = str(record.seq)

		# Annotation file.
		for line in fh_ann.readlines():
			if not line.startswith('#!'):
				name = line.split('\t')[0].strip()
				seq_type = line.split('\t')[2].strip()
				if seq_type == user_type:
					start, stop = int(line.split('\t')[3].strip()), int(line.split('\t')[4].strip())
					strand = line.split('\t')[6].strip()
					identifier = line.split('\t')[8].split(' ')[1].rstrip(';').strip('\"')
					# Save file.
					full_name = f'>{name}|{seq_type}|{identifier}|{start}:{stop}|{strand}\n{wrap(CONTIGS[name][start:stop+1])}\n'
					fh_save.write(full_name)

			
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Retrieve FASTA sequences')
	parser.add_argument(
		'-g', '-G', '--genome',
		required=True,
		dest='genome_filename',
		help='input genomic FASTA filename')
	parser.add_argument(
		'-a', '-A', '--annotation',
		required = True,
		dest='annotation_filename',
		help='input annotation GTF filename')
	parser.add_argument(
		'-f', '-F', '--feature', '--feat',
		dest='seq_type',
		choices=['gene', 'transcript', 'exon', 'CDS'],
		default='gene',
		help='gene / transcript / exon / CDS (default: gene)')
	parser.add_argument(
		'-s', '-S', '--save',
		dest='save_filename',
		default='genes.txt',
		help='save txt filename')
	args = parser.parse_args()
	read_sequences(args.genome_filename, args.annotation_filename, args.save_filename, args.seq_type)
