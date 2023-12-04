from sevens_stuff import DirectedWeightedGraph
import sevens_stuff
import csv
from itertools import islice
import timeit

# Replace 'your_file.csv' with the actual path to your CSV file
G = DirectedWeightedGraph()
stationCoordinates = {}

#stationCoordinates Format: {'202':['']}

G.add_node(0)
#Adding Nodes
with open('3xb3_final_project\london_stations.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in islice(csv_reader, 1, None):
        G.add_node(int(row[0]))
        stationCoordinates[int(row[0])] = [float(row[1]),float(row[2])]

#Adding Edges
with open('3xb3_final_project\london_connections.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in islice(csv_reader, 1, None):
        x1,y1 = stationCoordinates[int(row[0])]
        x2,y2 = stationCoordinates[int(row[1])]
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        G.add_edge(int(row[0]),int(row[1]),distance)



# Don't use this one, this one doesn't work properly
def makeHeuristic2(s):
    heuristic = {}
    x1,y1 = stationCoordinates[str(s)]
    for node in stationCoordinates.items():
        # heuristic[node] = euclidianDistance(stationCoordinates[node],stationCoordinates[s])
        # x2,y2 = stationCoordinates[node]
        print(stationCoordinates[node])
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        heuristic[node] = distance
    return heuristic


def makeHeuristic(s):
    heuristic = {}
    x1,y1 = stationCoordinates[s]
    for node, coordinates in stationCoordinates.items():
        x2,y2 = coordinates
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        heuristic[int(node)] = distance
    return heuristic
    
# print(makeHeuristic(1))
# print(stationCoordinates['6'][0]+4)

sevens_stuff.print_graph(G)
h = makeHeuristic(24)
# sevens_stuff.aStar(G,1,73,h)
start = timeit.default_timer()
pred, path = sevens_stuff.aStar(G,24,33,h)
end = timeit.default_timer()
print("astar time:",end-start)
print("Predecessor Dictionary:", pred)
print("Shortest Path:", path)
start = timeit.default_timer()
print(sevens_stuff.dijkstra(G, 24))
end = timeit.default_timer()
print("dijkstra time:",end-start)