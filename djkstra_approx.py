from min_heap import MinHeap, Element
from final_project_part1 import DirectedWeightedGraph
def dijkstra(G, source, k):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    relax_count = {}  # Counter for the number of relaxations for each node
    Q = MinHeap([])
    nodes = list(G.adj.keys())

    # Initialize priority queue/heap, distances, and relaxation counters
    for node in nodes:
        Q.insert(Element(node, float("inf")))
        dist[node] = float("inf")
        relax_count[node] = 0
    Q.decrease_key(source, 0)

    # Meat of the algorithm
    while not Q.is_empty():
        print(pred)
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

test_graph = DirectedWeightedGraph()
for i in range(4):
    test_graph.add_node(i)

test_graph.add_edge(0,1,1)
test_graph.add_edge(0,2,2)
test_graph.add_edge(1,2,3)
test_graph.add_edge(2,3,4)
test_graph.add_edge(3,0,5)

print(dijkstra(test_graph, 0, 10))