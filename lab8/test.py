#!/usr/bin/python3

import numpy as np 

def matrix_to_list(graph):
	return {node: [i for i in range(len(graph)) if graph[node, i] != 0] for node in range(len(graph))}

if __name__ == '__main__':
	graph = np.random.randint(0, 2, (5, 5))
	print(graph)
	print(matrix_to_list(graph))