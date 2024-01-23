from sys import maxsize
from itertools import permutations

V = 4      # Number of vertices

def travellingSalesmanProblem(graph, s):
    vertex = [i for i in range(V) if i != s]

    min_path = maxsize

    next_permutation = permutations(vertex)

    for i in next_permutation:


        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        min_path = min(min_path, current_pathweight)

    return min_path

if __name__ == "__main__":
    # Adjacency Matrix representation of the graph (weights between cities)
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    s = 0           #source vertex

    print(travellingSalesmanProblem(graph, s))




#output
#80