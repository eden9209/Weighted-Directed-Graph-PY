from abc import ABC

from src.GraphInterface import GraphInterface
from src.Vertex import Vertex
from builtins import *


# The Graph class contains a dictionary that maps vertex keys to Class vertex >> vertices
# Count of the number of vertices in the graph >> numVertices
# Count of the number of edges in the graph >> num_of_edges

class DiGraph(GraphInterface, ABC):

    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        self.num_of_edges = 0
        self.mc = 0

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.vertices:
            node = Vertex(node_id)
            if pos is not None:
                node.setPosition(pos[0], pos[1], pos[2])
            self.numVertices = self.numVertices + 1
            self.vertices[node_id] = node
            return True
        else:
            return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if weight < 0 or id1 == id2:
            return False

        if id2 in self.get_node(id1).connectedTo:
            return False

        if id1 not in self.get_all_v().keys():
            return False

        if id2 not in self.get_all_v().keys():
            return False

        self.vertices[id1].addNeighbor(id2, weight)
        self.num_of_edges = self.num_of_edges + 1
        self.mc += 1
        return True

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self.vertices

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.num_of_edges

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.numVertices

    def get_node(self, key) -> Vertex:
        """
        :param key: a key of a node
        :return: the node that associated with the initial key
        """
        if key in self.vertices.keys():
            return self.vertices[key]

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        if id1 in self.vertices:
            in_edges = {}
            # current_node = self.get_node(id1)
            for v1 in self.vertices.values():
                if id1 in v1.connectedTo.keys():
                    # Return the weight of the edge between self and nbr (two vertices)
                    w = v1.get_edge_Weight(id1)
                    in_edges[v1.getKey()] = w

            return in_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if id1 in self.vertices:
            current_node = self.get_node(id1)
            return current_node.getNi_dict()

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if node_id in self.vertices:

            for k1 in self.all_in_edges_of_node(node_id).keys():
                self.remove_edge(k1, node_id)

            # for k2 in self.all_out_edges_of_node(node_id).keys():
            #     self.remove_edge(node_id, k2)

            del self.vertices[node_id]
            self.mc = self.mc + 1
            self.numVertices = self.numVertices - 1

            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 in self.vertices.keys() and node_id2 in self.vertices.keys():
            current_node = self.get_node(node_id1)
            if node_id2 in current_node.getNi_key():
                current_node.remove_ni(node_id2)
                self.mc = self.mc + 1
                self.num_of_edges = self.num_of_edges - 1
                return True
        return False

    def reverse_graph(self):
        g_r = DiGraph()
        for n in self.get_all_v().values():
            g_r.add_node(n.getKey(), n.getPos())
        for n in self.get_all_v().values():
            for e in self.all_out_edges_of_node(n.getKey()).items():  # (other node id, weight))
                g_r.add_edge(e[0], n.getKey(), e[1])
        return g_r

    def get_mc(self) -> int:
        return self.mc

    def __repr__(self):
        s = "Graph: |V|={} , |E|={}".format(self.numVertices, self.num_of_edges)
        return s
