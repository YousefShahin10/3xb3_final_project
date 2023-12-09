from min_heap import MinHeap, Element
from final_project_part1 import DirectedWeightedGraph, dijkstra, bellman_ford
import random
import timeit
import matplotlib.pyplot as plt


# Implementation =====================

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


# ===================================================


# Test
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
    heuristic = {'0':8,1:2,2:5,3:4,4:0}
    pred, path = aStar(G, 0, 4, heuristic)
    print("Predecessor Dictionary:", pred)
    print("Shortest Path:", path)
    print("Dijkstra Distances:",dijkstra(G, 0))

#Uncomment the method below to run the test
# astarTest()

#=================================