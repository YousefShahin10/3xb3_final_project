from sevens_stuff import DirectedWeightedGraph
import csv
from itertools import islice

# Replace 'your_file.csv' with the actual path to your CSV file
G = DirectedWeightedGraph()
stationCoordinates = {}

#stationCoordinates Format: {'202':['']}

#Adding Nodes
with open('3xb3_final_project\london_stations.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in islice(csv_reader, 1, None):
        G.add_node(row[0])
        stationCoordinates[row[0]] = [float(row[1]),float(row[2])]

#Adding Edges
with open('3xb3_final_project\london_connections.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in islice(csv_reader, 1, None):
        x1,y1 = stationCoordinates[row[0]]
        x2,y2 = stationCoordinates[row[1]]
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        G.add_edge(row[0],row[1],distance)

# print(stationCoordinates)


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
    x1,y1 = stationCoordinates[str(s)]
    print(x1)
    for node, coordinates in stationCoordinates.items():
        x2,y2 = coordinates
        print(x2)
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        heuristic[node] = distance
    return heuristic
    
print(makeHeuristic(1))
# print(stationCoordinates['6'][0]+4)