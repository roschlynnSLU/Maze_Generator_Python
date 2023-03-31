import random

class Graph:

    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    
    def remove_edge(self, u, v):
        if u in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)

    def has_edge(self, u, v):
        result = False
        if u in self.graph:
            if v in self.graph[u]:
                result = True
        return result

class Maze:

    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.graph = Graph(size*size)
    
