import sys


# This Class name is: Vertex,
# Class Vertex will represent each vertex in the class Graph .
# Each vertex uses dictionary > "connectedTo"
# The Aim of the dictionary is:
# holds the key-weight pairs of all connections from this vertex.
# key of the connected vertex and weight of the edge.

class Vertex:

    def __init__(self, key: int, info: str = None, pos: tuple = None, tag: int = 0):
        self.key = key
        self.info = info
        self.pos = pos
        self.tag = tag
        # each Vertex have a "connectedTo" dictionary .
        self.connectedTo = {}
        self.weight = sys.maxsize  # for Dijkstra's

    # getters Methods
    def getKey(self):
        return self.key

    def getInfo(self):
        return self.info

    def getPos(self):
        return self.pos

    def getTag(self):
        return self.tag

    def getWeight(self):
        return self.weight

    # setters Methods

    def setPosition(self, x, y, z):
        self.pos = (x, y, z)

    def setInfo(self, info):
        self.info = info

    def setWeight(self, w):
        self.weight = w

    def setTag(self, t):
        self.tag = t

    # Generic Methods:

    # Add the information about connection between vertexes into the dictionary connectedTo
    def addNeighbor(self, neighbor, weight=0):
        # neighbor is another vertex
        self.connectedTo[neighbor] = weight

    # Return the vertex's neighbors keys
    def getNi_key(self):
        return self.connectedTo.keys()

    # Return the vertex's neighbors dict
    def getNi_dict(self):
        return self.connectedTo

    # Return the weight of the edge between self and nbr (two vertices)
    def get_edge_Weight(self, nbr):
        return self.connectedTo[nbr]

    def remove_ni(self, key):
        del self.connectedTo[key]
