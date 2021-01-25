import os
import sys
import numpy as np



scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p083_matrix.txt")

file = open(src_filename, "r")

src = file.read()



Matrix = [[int(i) for i in k.split(",")] for k in  src.split("\n")[:-1]]


class Graph():
    def __init__(self, M):
        self.start = (0,0)
        self.graph = {}
        self.end = (len(M)-1, len(M[0])-1)
        self.dist = {}
        self.values = M
        self.visited = set()


    def __str__(self):
        return str(self.root)

    def __setitem__(self, key, value):
        self.graph[key] = value
    def __getitem__(self, key):
        return self.graph[key]

    def BFS(self, source):
        print(source)
        self.dist[(source, source)] = self.values[source[0]][source[1]]
        self.Q = self.graph.keys()
        for q in self.Q:
            if q!=(source):
                self.dist[(source, q)] = float('inf')
        while len(self.Q) != 0:
            v = min(self.Q, key=lambda x: self.dist[(source, x)])
            self.Q.remove(v)
            for u in self.graph[v]:
                alt = self.dist[(source, v)] + self.values[u[0]][u[1]]
                if alt < self.dist[(source, u)]:
                    self.dist[(source, u)] = alt
        return self.dist[(source, self.end)]



myGraph = Graph(Matrix)

for r, row in enumerate(Matrix):
    for c, cell in enumerate(row):
        myGraph[(r,c)] = []
        if r != len(Matrix)-1:
            myGraph[(r,c)].append((r+1, c))
        if r != 0:
            myGraph[(r,c)].append((r-1, c))
        if c != len(row)-1:
            myGraph[(r,c)].append((r, c+1))
        if c != 0:
            myGraph[(r,c)].append((r, c-1))


print(myGraph.BFS((0,0)))
