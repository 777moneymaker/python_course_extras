#!/usr/bin/python3
'''Module written as an extra exercise for AMU's Python course.
__author__ = Milosz Chodkowski PUT
___field__ = Bioinformatics 
___version___ = 1.0'''

class Sequence:
	def __init__(self, seq='..(..)..()..'):
		self.seq = seq

	def validate(self, seq=None):
		'''Return the boolean value of dot bracket validation.
		>>> S.validate('..()..')
		True
		>>> S.validate('..()).')
		False'''

		# sequence eq itself if exists, else eq self sequence
		seq = self.seq if seq is None else seq

		OPEN_PAR, CLOSED_PAR = '(', ')'
		brackets_map, valid_chars = {'(': ')'}, {'(', ')', '.'}
		stack, pars = [], []

		for char in seq:
			# If there is any other char than parentheses or dot
			if char not in valid_chars:
				print('\'{}\' is not valid char in dot bracket format!'.format(char))
				return False
			if char == OPEN_PAR or char == CLOSED_PAR:
				pars.append(char)
				
		for bracket in pars:
			if bracket in brackets_map:
				# Add coresponding bracket
				stack.append(brackets_map[bracket])
			# If stack empty or last bracket not valid
			elif not stack or bracket != stack.pop():
				return False
		# True if empty else False
		return True if not stack else False 
		
if __name__ == '__main__':
	S = Sequence()
	print(S.validate())
	print(S.validate('()))((()'))
