import csv
from itertools import islice
import timeit
import matplotlib.pyplot as pl
from final_project_part1 import DirectedWeightedGraph, dijkstra
from part2_AStar import aStar

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
    


def astarDijkstraTimeComparer(source, destination):
    print("===============================================")
    print("Finding Path from ",stationNames[source]," to ", stationNames[destination])
    itermediateStations = []
    h = makeHeuristic(source)

    start = timeit.default_timer()
    pred, path = aStar(G,source,destination,h)
    end = timeit.default_timer()
    print("A* time:",end-start)

    for station in path:
        itermediateStations.append(stationNames[station])
    
    start = timeit.default_timer()
    dijkstra(G, 24)
    end = timeit.default_timer()

    print("Dijkstra time:",end-start)
    print(path)
    print("Path Taken:", itermediateStations)

# astarDijkstraTimeComparer(162,218)

# Experiment for shortest path pairs


def part3Experiment1():
    astarTimes, djikstraTimes = [], []
    for node1 in stationCoordinates:
        print("Current Node:",node1)
        
        currentAStarTime, currentDjikstraTime = 0,0
        for node2 in stationCoordinates:
            if node1 != node2:
                # Timing A*
                h = makeHeuristic(node1)
                start = timeit.default_timer()
                pred, path = aStar(G,node1,node2,h)
                end = timeit.default_timer()
                currentAStarTime += (end-start)

                # Timing Djikstra
                start1 = timeit.default_timer()
                dijkstra(G, node1)
                end1 = timeit.default_timer()
                currentDjikstraTime += (end1-start1)
        djikstraTimes.append(currentDjikstraTime)
        astarTimes.append(currentAStarTime)
    
    # Plotting Results
    pl.plot(djikstraTimes, label="Dijkstra's")
    pl.plot(astarTimes, label="A*")

    pl.xlabel("Station ID")
    pl.ylabel("Time")
    pl.title("Shortest Pair Path for every station")

    pl.legend(loc=1)
    pl.show()


#uncomment the method below to run the experiment
part3Experiment1()