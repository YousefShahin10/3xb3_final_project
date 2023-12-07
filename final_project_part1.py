import min_heap
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
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
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

def new_dijkstra(G, source, k):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    relax_count = {}  # Counter for the number of relaxations for each node
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    # Initialize priority queue/heap, distances, and relaxation counters
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
        relax_count[node] = 0
    Q.decrease_key(source, 0)

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if relax_count[current_node] < k and dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
                relax_count[neighbour] += 1
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
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist

def new_bellman_ford(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())
    relax_count = {}
    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
        relax_count[node] = 0
    dist[source] = 0

    #Meat of the algorithm
    for node in nodes:
        for neighbour in G.adj[node]:
            if dist[neighbour] > dist[node] + G.w(node, neighbour) and relax_count[node] < k:
                pred[neighbour] = node
                dist[neighbour] = dist[node] + G.w(node, neighbour)
                relax_count[neighbour] += 1
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
def new_create_random_complete_graph(n, upper, edges):
    if edges < n - 1:
        raise Exception("E has to be >= V - 1")

    G = DirectedWeightedGraph()

    dangling = []
    connected = []

    for i in range(n):
        G.add_node(i)
        dangling.append(i)

    connected.append(dangling.pop())

    for i in range(edges):
        if (len(dangling) != 0):
            start = connected[random.randint(0, len(connected) - 1)]
            end = dangling.pop(random.randint(0, len(dangling) - 1))
            G.add_edge(start, end, random.randint(1, upper))
            connected.append(end)

        else:

            start = random.randint(0, n - 1)
            end = random.randint(0, n - 1)
            while start == end or G.are_connected(start, end):
                end = random.randint(0, n - 1)
            G.add_edge(start, end, random.randint(1, upper))

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


def experiment1():#testing runtime while increasing the number of nodes
    dijkstraTimes = []
    bellmanTimes = []
    # Running the experiment on Dikstra's and bellman for number of nodes
    print("doning")
    for i in range(10, 30):
        G = create_random_complete_graph(i, 25)
        start = timeit.default_timer()
        dijkstraDist = dijkstra(G, 0)
        dijkstraTimes.append(timeit.default_timer() - start)

        start = timeit.default_timer()
        bellmanDist = bellman_ford(G, 0)
        bellmanTimes.append(timeit.default_timer() - start)

    plt.plot(dijkstraTimes, label="Dijkstra Times")
    plt.plot(bellmanTimes, label="Bellman Times")

    plt.xlabel('Number of nodes')
    plt.ylabel('Runtime')
    plt.title('Number of Nodes vs Runtime')
    plt.legend(loc=1)
    plt.show()



def experiment2(node_num, max_ratio):#testing runtime while the density of the graph increases
    dijkstra_times = []
    bellman_times = []

    print("doning")
    for i in range(1, max_ratio):
        edge_num = i*node_num
        upper = 25
        print(edge_num)
        print(node_num)
        # G = new_create_random_complete_graph(node_num, edge_num, upper)
        G = new_create_random_complete_graph(node_num, upper, edge_num)
        start = timeit.default_timer()
        dijkstra_dist = dijkstra(G, 0)
        dijkstra_times.append(timeit.default_timer() - start)

        start = timeit.default_timer()
        bellman_dist = bellman_ford(G, 0)
        bellman_times.append(timeit.default_timer() - start)

    plt.plot(dijkstra_times, label="Dijkstra Times")
    plt.plot(bellman_times, label="Bellman Times")
    print('reached')
    plt.xlabel('Edge to Node Ratio')
    plt.ylabel('Runtime')
    plt.title('Number of Nodes vs Runtime')
    plt.legend(loc=1)
    plt.show()

def experiment3(approx_num):#testing runtime while increasing the k-value
    dijkstraTimes = []
    bellmanTimes = []

    print("doning")
    for k in range(approx_num):
        upper = 25
        node_num = 30
        G = create_random_complete_graph(node_num, upper)

        start = timeit.default_timer()
        dijkstraDist = new_dijkstra(G, 0, k)
        dijkstraTimes.append(timeit.default_timer() - start)

        start = timeit.default_timer()

        bellmanDist = new_bellman_ford(G, 0, k)
        bellmanTimes.append(timeit.default_timer() - start)

    plt.plot(dijkstraTimes, label="Dijkstra Times")
    plt.plot(bellmanTimes, label="Bellman Times")

    plt.xlabel('k-value')
    plt.ylabel('Runtime')
    plt.title('Number of Nodes vs Runtime')
    plt.legend(loc=1)
    plt.show()

def experiment4(approx_num):#testing accuracy of shortest path while changing the k-value
    dijkstraTotalDist = []
    bellmanTotalDist = []

    for k in range(approx_num):
        upper = 25
        node_num = 30
        G = create_random_complete_graph(node_num, upper)


        dijkstraDist = new_dijkstra(G, 0, k)
        dijkstraTotalDist.append(total_dist(dijkstraDist))


        bellmanDist = new_bellman_ford(G, 0, k)
        bellmanTotalDist.append(total_dist(bellmanDist))

    plt.plot(dijkstraTotalDist, label="Dijkstra Distances")
    plt.plot(bellmanTotalDist, label="Bellman Distances")

    plt.xlabel('Edge to Node Ratio')
    plt.ylabel('Distance')
    plt.title('Number of Nodes vs Total Shortest Path Distances of Dijkstra and Bellman')
    plt.legend(loc=1)
    plt.show()

# experiment1()
# experiment2(20,7)
# experiment3(20)
experiment4(50)

