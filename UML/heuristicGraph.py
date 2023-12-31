from weightedGraph import WeightedGraph

class HeuristicGraph(WeightedGraph):

    def __init__(self):
        self.adj = {}
        self.weights = {}
        heuristic = {}

    def get_adj_nodes(self,node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def number_of_nodes(self):
        return len(self.adj)
    
    def getHeuristic(s, coordinates):
        heuristic = {}
        x1,y1 = coordinates[s]
        for node, coordinates in coordinates.items():
            x2,y2 = coordinates
            distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            heuristic[int(node)] = distance
        return heuristic