from SPAlgorithm import SPAlgorithm

class Bellman_Ford(SPAlgorithm):

    def calc_sp(self, graph, source, dest):
        pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {} #Distance dictionary
        nodes = list(graph.adj.keys())
        relax_count = {}
        #Initialize distances
        for node in nodes:
            dist[node] = float("inf")
        dist[source] = 0

        #Meat of the algorithm
        for node in nodes:
            for neighbour in graph.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    pred[neighbour] = node
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    relax_count[neighbour] += 1
        return dist[dest]


    def approx_bellman_ford(G, source, k):
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
