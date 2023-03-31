import random
import graph_class
        
class Maze:

    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.graph = graph_class.Graph(size*size)

    def get_total_nodes(self):
        return max(self.graph) + 1

    def print_Maze_using_DFS(maze, start_node):

maze = Maze(5)
print("Welcome to 2D maze")