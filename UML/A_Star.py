from SPAlgorithm import SPAlgorithm
from min_heap import MinHeap, Element

class A_Star(SPAlgorithm):

    def calc_sp(self, graph, source, dest):
        pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {} #Distance dictionary
        Q = MinHeap([])
        nodes = list(graph.adj.keys())
        h = graph.get_heuristic()

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
            if current_node == dest:
                path = []
                while current_node is not None:
                    path.insert(0, current_node)
                    current_node = pred.get(current_node)
                return pred, path
            for neighbour in graph.adj[current_node]:
                if dist[current_node] + graph.w(current_node, neighbour) + h[neighbour] < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour) + h[neighbour])
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour) + h[neighbour]
                    pred[neighbour] = current_node
        return pred, []