from min_heap import MinHeap, Element
import random
import timeit
import matplotlib.pyplot as plt


class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
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

    def number_of_nodes(self):
        return len(self.adj)


def dijkstra(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


def bellman_ford(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    #Meat of the algorithm
    for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
       
    return dist


def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total

def create_random_complete_graph(n,upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G


#Assumes G represents its nodes as integers 0,1,...,(n-1)
def mystery(G):
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]: 
                    d[i][j] = d[i][k] + d[k][j]
    return d

def init_d(G):
    n = G.number_of_nodes()
    d = [[float("inf") for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i, j):
                d[i][j] = G.w(i, j)
        d[i][i] = 0
    return d

def new_create_random_complete_graph(node_num, edge_num, upper):
    G = DirectedWeightedGraph()
    for i in range(node_num):
        G.add_node(i)
    for i in range(node_num):
        for j in range(edge_num):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G

# ========= Part 2: AStar Implementation =====================

def aStar(G, s, d, h):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(s, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        if current_node == d:
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = pred.get(current_node)
            return pred, path
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) + h[neighbour] < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour) + h[neighbour])
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour) + h[neighbour]
                pred[neighbour] = current_node
    return pred, []

# ==================== Experiments ===============

# ==================== Part 1 =========================
def experiment1():
    dijkstraTimes = []
    bellmanTimes = []
    #Running the experiment on Dikstra's and bellman for number of nodes
    print("doning")
    for i in range(10,30):
      G = create_random_complete_graph(i,25) 
      start = timeit.default_timer()
      dijkstraDist = dijkstra(G, 0) 
      dijkstraTimes.append(timeit.default_timer() - start)
      start = timeit.default_timer()
      bellmanDist = bellman_ford(G, 0)
      bellmanTimes.append(timeit.default_timer() - start)
    plt.plot(dijkstraTimes, label="Dijkstra Times")
    plt.plot(bellmanTimes, label="Bellman Times")
    plt.xlabel('Number of nodes````')
    plt.ylabel('Runtime')
    plt.title('Number of Nodes vs Runtime')
    plt.legend(loc=1)
    plt.show()
    
def experiment2(node_num, max_ratio):
    dijkstraTimes = []
    bellmanTimes = []
    for i in range(max_ratio):
        edge_num = i
        upper = 25
        G = new_create_random_complete_graph(node_num, edge_num, upper)

        start = timeit.default_timer()
        dijkstraDist = dijkstra(G, 0)
        dijkstraTimes.append(timeit.default_timer() - start)

        start = timeit.default_timer()
        bellmanDist = bellman_ford(G, 0)
        bellmanTimes.append(timeit.default_timer() - start)

    plt.plot(dijkstraTimes, label="Dijkstra Times")
    plt.plot(bellmanTimes, label="Bellman Times")
    plt.xlabel('Edge to Node Ratio')
    plt.ylabel('Runtime')
    plt.title('Number of Nodes vs Runtime')
    plt.legend(loc=1)
    plt.show()


# experiment2(30,30)


# ========== Part 2: testing astar ============

def astarTest():
    G = DirectedWeightedGraph()
    for i in range(5):
        G.add_node(i)
    G.add_edge(0,1,2)
    G.add_edge(0,2,2)
    G.add_edge(0,3,3)
    G.add_edge(1,4,2)
    G.add_edge(2,4,1)
    G.add_edge(3,4,5)
    heuristic = {0:8,1:2,2:5,3:4,4:0}
    pred, path = aStar(G, 0, 4, heuristic)
    print("Predecessor Dictionary:", pred)
    print("Shortest Path:", path)
    print("Dijkstra Distances:",dijkstra(G, 0))

# astarTest()

