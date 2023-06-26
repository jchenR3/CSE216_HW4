import sys

# print(sys.path)s

from pyTPS import pyTPS
from Airport import Airport
from WeightedGraph import WeightedGraph
from AddFlight import AddFlight
import json

# Global variablees
stops = []
airportGraph = WeightedGraph()
tps = pyTPS()

# Read the JSON file
file_path = 'D:\VSC Coding Folder\CSE-216\HW4\graphStructure\graphStructure.json'
with open(file_path, 'r') as file:
    jsonFromFile = json.load(file)

nodes = jsonFromFile['nodes']
edges = jsonFromFile['edges']

node_properties = [(node_id, *node_data[0].values()) for node_id, node_data in jsonFromFile['nodes'].items()]

edge_properties = [(edge_id, *edge_data[0].values()) for edge_id, edge_data in jsonFromFile['edges'].items()]

for node_id, code, latitude_deg, latitude_min, longitude_deg, longitude_min in node_properties:
    newNode = Airport(code, latitude_deg, latitude_min, longitude_deg, longitude_min)
    airportGraph.addNode(code, newNode)

# print(airportGraph.getNodesSize())

for edge_id, source, target in edge_properties:
    distance = Airport.calculateDistance(airportGraph.getNodeData(source), airportGraph.getNodeData(target))
    airportGraph.addEdge(source, target, distance)
    airportGraph.addEdge(target, source, distance)

# print(airportGraph.getEdgesSize())

def displayAirports():
    print("\n\nAIRPORTS YOU CAN TRAVEL TO AND FROM:")
    codes = []
    airportGraph.getKeys(codes)
    tempString = ""
    for i in range(len(codes)):
        if(i % 10 == 0):
            tempString += "\t"
        tempString += codes[i]
        if(i < (len(codes)-1)):
            tempString += ", "
        if(i % 10 == 9):
            print(tempString)
            tempString = ""
    print()

def displayCurrentTrip():

    totalMileage = 0

    print("Trip Stops: ")
    for i in range(len(stops)):
        print(f"    {i+1}. {stops[i]}")
    print()

    print("Trip Legs: ")
    if(len(stops) > 1):
        for i in range(len(stops)-1):
            path = []
            tempNode = ""
            airportGraph.findPath(path, stops[i], stops[i+1])
            if(len(path) == 0):
                print(f"    {i+1}. ")
                continue
            for j in range(len(path)):
                if(j == len(path)-1):
                    tempNode += path[j]
                else:
                    tempNode += path[j]
                    tempNode += "-"
    
            mileageForEachLeg = 0
            for k in range(len(path)-1):
                mileageForEachLeg += Airport.calculateDistance(airportGraph.getNodeData(path[k]), airportGraph.getNodeData(path[k+1]))
            
            totalMileage += mileageForEachLeg

            print(f"    {i+1}. {tempNode} ({mileageForEachLeg} Miles)")
        
    
    print(f"\nTotal Trip Distance: {totalMileage} Miles\n")

def displayMenu():
    print("ENTER A SELECTION")
    print("S) Add a Stop to your Trip")
    print("U) Undo")
    print("R) Redo")
    print("E) Empty Trip")
    print("Q) Quit")

def processUserInput():
    userInput = input("-")
    if(userInput == "S"):
        addingAirport = input("\nEnter an Airport to add to Trip: ")
        if(airportGraph.nodeExists(addingAirport)):
            if(len(stops) > 0):
                if(stops[len(stops)-1] == addingAirport):
                    print("Cannot add same airport as previous airport, try again")
                else:
                    newAirport = AddFlight(addingAirport, stops)
                    tps.addTransaction(newAirport)
            else:
                newAirport = AddFlight(addingAirport, stops)
                tps.addTransaction(newAirport)
        else:
            print("Invalid aiport, try again")
    elif(userInput == "U"):
        tps.undoTransaction()
    elif(userInput == "R"):
        tps.doTransaction()
    elif(userInput == "E"):
        tps.clearAllTransactions()
        stops.clear()
    elif(userInput == "Q"):
        return False
    return True

keepGoing = True
while (keepGoing):
    # print(tps.toString())                                                   #
    displayAirports()
    displayCurrentTrip()
    displayMenu()
    keepGoing = processUserInput()

print("GOODBYE")