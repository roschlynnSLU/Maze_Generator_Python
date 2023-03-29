#Python Code to Randomly Generate a Maze

class Graph:
    def __init__(self, num_Nodes):
        self.num_Nodes = num_Nodes
        self.graph = {}

class Maze:
    
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.graph = Graph(size * size)
    
    def print_test():
        print("Welcome to 2D Maze Generator")

maze = Maze(5)
maze.print_test()