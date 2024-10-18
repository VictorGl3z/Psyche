# Problem Statement
# Determine if two nodes are adjacent in an undirected graph when
# given the adjacency matrix and two nodes.
#
# Examples
# matrix:
# [0, 1, 0, 0], 
# [1, 0, 1, 1],
# [0, 1, 0, 1],
# [0, 1, 1, 0]
# is_adjacent(matrix, 0, 1) -> True
# is_adjacent(matrix, 0, 2) -> False

def is_adjacent(matrix, node1, node2):
    return matrix[node1][node2]
