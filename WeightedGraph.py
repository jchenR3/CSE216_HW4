from WeightedEdge import WeightedEdged
import sys

class WeightedGraph:

    def getNodesSize(self):
        return len(self.nodes)
    
    def getEdgesSize(self):
        return len(self.edges)

    def __init__(self):
        self.nodes = {}
        self.edges = {}
    
    def getKeys(self, keys):
        for tempKeys in self.nodes.keys():
            keys.append(tempKeys)

    def nodeExists(self, testNode):
        return testNode in self.nodes.keys()        
    
    def getEdgeId(self, node1, node2):
        return node1 + "-" + node2
    
    def addNode(self, nodeId, data):
        self.nodes[nodeId] = data

    def getNodeData(self, nodeId):
        return self.nodes[nodeId]
    
    def addEdge(self, node1, node2, weight):
        edgeId = self.getEdgeId(node1,node2)
        newEdge = WeightedEdged(node1, node2, weight)
        self.edges[edgeId] = newEdge
    
    def findPath(self, path, node1, node2):
        
        neighbors = []
        visitedNodes = []

        currentNode = node1

        path.append(currentNode)
        while(len(path) > 0):
            if(currentNode not in visitedNodes):
                visitedNodes.append(currentNode)

            # Fills the neighbor list with all neighbors of the current node that are not in the visited list
            for edgeId in self.edges.keys():
                tempEdge = self.edges[edgeId]
                if(tempEdge.getNode1() == currentNode and (tempEdge.getNode2() not in neighbors) and (tempEdge.getNode2() not in visitedNodes)):
                    neighbors.append(tempEdge.getNode2())
                elif(tempEdge.getNode2() == currentNode and (tempEdge.getNode1() not in neighbors) and (tempEdge.getNode1() not in visitedNodes)):
                    neighbors.append(tempEdge.getNode1())
            
            if(len(neighbors) == 0):
                path.pop()
                if(len(path) == 0):
                    break
                else:
                    currentNode = path[len(path)-1]
                    continue
            else:
                if(node2 in neighbors):
                    path.append(node2)
                    break

                min = sys.maxsize
                tempNode = ""

                for neighboringNode in neighbors:
                    edgeId = self.getEdgeId(currentNode, neighboringNode)
                    if(self.edges[edgeId].getNode1() == currentNode and self.edges[edgeId].getNode2() not in visitedNodes):
                        tempMin = self.edges[edgeId].getWeight()
                        if(tempMin < min):
                            min = tempMin
                            tempNode = neighboringNode
                    
                    elif(self.edges[edgeId].getNode2() == currentNode and self.edges[edgeId].getNode1() not in visitedNodes):
                        tempMin = self.edges[edgeId].getWeight()
                        if(tempMin < min):
                            min = tempMin
                            tempNode = neighboringNode

                currentNode = tempNode
                path.append(currentNode)
                neighbors.clear()