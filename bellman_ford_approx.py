from min_heap2 import MinHeap as min_heap
from final_project_part1 import DirectedWeightedGraph

def bellman_ford(G, source, k):
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
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour) and relax_count[node] < k:
                    pred[neighbour] = node
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    relax_count[neighbour] += 1
    return dist

test_graph = DirectedWeightedGraph()
for i in range(4):
    test_graph.add_node(i)

test_graph.add_edge(0,1,1)
test_graph.add_edge(0,2,2)
test_graph.add_edge(1,2,3)
test_graph.add_edge(2,3,4)
test_graph.add_edge(3,0,5)

print(bellman_ford(test_graph, 0, 1))

'''
graph = {
    0: {1: 1, 2: 4},
    1: {0: 1, 2: 2, 3: 5},
    2: {0: 4, 1: 2, 3: 1},
    3: {1: 5, 2: 1}
}
'''