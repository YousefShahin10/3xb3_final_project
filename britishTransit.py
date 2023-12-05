from sevens_stuff import DirectedWeightedGraph
import sevens_stuff
import csv
from itertools import islice
import timeit

# Replace 'your_file.csv' with the actual path to your CSV file
G = DirectedWeightedGraph()
stationCoordinates = {} #Stores the coordinates of each station
stationNames = {} #Stores the name of each station
#stationCoordinates Format: {'202':['']}

#Adding Nodes
with open('3xb3_final_project\london_stations.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in islice(csv_reader, 1, None):
        G.add_node(int(row[0]))
        stationCoordinates[int(row[0])] = [float(row[1]),float(row[2])]
        stationNames[int(row[0])] = row[3]

#Adding Edges
with open('3xb3_final_project\london_connections.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in islice(csv_reader, 1, None):
        x1,y1 = stationCoordinates[int(row[0])]
        x2,y2 = stationCoordinates[int(row[1])]
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        G.add_edge(int(row[0]),int(row[1]),distance)
        G.add_edge(int(row[1]),int(row[0]),distance)
        

def makeHeuristic(s):
    heuristic = {}
    x1,y1 = stationCoordinates[s]
    for node, coordinates in stationCoordinates.items():
        x2,y2 = coordinates
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        heuristic[int(node)] = distance
    return heuristic
    

# h = makeHeuristic(162)
# # sevens_stuff.aStar(G,1,73,h)
# start = timeit.default_timer()
# pred, path = sevens_stuff.aStar(G,162,218,h)
# end = timeit.default_timer()
# print("astar time:",end-start)
# # print("Predecessor Dictionary:", pred)
# print("Shortest Path:", path)
# stops = []
# for station in path:
#     stops.append(stationNames[station])
# print(stops)
# start = timeit.default_timer()
# sevens_stuff.dijkstra(G, 24)
# end = timeit.default_timer()
# print("dijkstra time:",end-start)
# # print(stationNames)


def astarDijkstraTimeComparer(source, destination):
    print("===============================================")
    print("Finding Path from ",stationNames[source]," to ", stationNames[destination])
    itermediateStations = []
    h = makeHeuristic(source)

    start = timeit.default_timer()
    pred, path = sevens_stuff.aStar(G,source,destination,h)
    end = timeit.default_timer()
    print("A* time:",end-start)

    for station in path:
        itermediateStations.append(stationNames[station])
    
    start = timeit.default_timer()
    sevens_stuff.dijkstra(G, 24)
    end = timeit.default_timer()

    print("Dijkstra time:",end-start)
    print(path)
    print("Path Taken:", itermediateStations)

astarDijkstraTimeComparer(162,218)