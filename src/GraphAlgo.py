import math
import random
from typing import List
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
import json
import matplotlib.pyplot as plt
from queue import *
import sys


def intersection(lst1, lst2, lst3):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        """
        Init the graph on which this set of algorithms operates on.
        :param g: a directed graph
        """
        self.graph = g

    def get_graph(self) -> GraphInterface:
        """
        :return: the underlying graph of which this class works.
        """
        return self.graph

    def save_to_json(self, file_name: str) -> bool:
        string_json = {"Edges": [], "Nodes": []}

        try:
            with open(file_name, "w") as file:
                for k in self.graph.get_all_v().keys():
                    v = self.graph.get_node(k)
                    if v.getPos() is None:
                        pos = '0.0,0.0,0.0'

                    else:
                        pos = str(v.getPos()[0]) + "," + str(v.getPos()[1]) + "," + str(v.getPos()[2])
                    key = v.getKey()
                    dict_vertex = {"pos": pos, "id": key}
                    string_json["Nodes"].append(dict_vertex)
                    if v.getNi_dict() is not None:
                        for d in v.getNi_dict().keys():
                            edge_dict = {"src": k, "dest": d, "w": v.get_edge_Weight(d)}
                            string_json["Edges"].append(edge_dict)

                graph_json_str = json.dumps(string_json)
                file.write(graph_json_str)
                return True

        except IOError as e:
            print(e)
            return False

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        graph_from_json = DiGraph()

        try:
            with open(file_name, 'r') as file:
                json_str = file.read()  # returns the whole text
                graph_dict_from_json = json.loads(json_str)  ## parse json_str ,the result is a Python dictionary:

            for v in graph_dict_from_json['Nodes']:
                pos = v.get('pos')
                if pos is not None:
                    pos = tuple(map(float, v['pos'].split(',')))  # for ex: (35.1931,32.102,0.0)
                key = v['id']
                graph_from_json.add_node(key, pos)

            for ed in graph_dict_from_json['Edges']:  # itearate the array val of the key Edges
                source = int(ed['src'])
                destination = int(ed['dest'])
                weight = float(ed['w'])
                graph_from_json.add_edge(source, destination, weight)

            self.graph = graph_from_json
        except IOError:
            return False

        if self.graph is not None:
            return True

        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
         Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
         @param id1: The start node id
         @param id2: The end node id
         @return: The distance of the path, a list of the nodes ids that the path goes through
         """
        # tag=0 not visited || tag=1 visited
        # vertex.w >> follows the destination node
        # priority queue (( update_distance , node)) || (priority , element)
        # pq.get() – Removes and returns an item from the queue > low priority get first

        if id1 in self.graph.vertices and id2 in self.graph.vertices and id1 != id2:
            p_queue = PriorityQueue()
            self.reset_graph()
            parent = {}
            path = []
            curr = self.graph.get_node(id1)
            curr.setWeight(0)
            p_queue.put((0, curr))

            while not p_queue.empty():
                curr = p_queue.get()[1]
                if curr.getTag() == 0:
                    curr.setTag(1)
                    if curr.getKey() == id2:
                        break
                    for k, w in self.graph.all_out_edges_of_node(curr.getKey()).items():
                        tmp_w = curr.getWeight() + w
                        if tmp_w < self.graph.get_node(k).getWeight():
                            self.graph.get_node(k).setWeight(tmp_w)
                            parent[k] = curr
                            p_queue.put((tmp_w, self.graph.get_node(k)))

            v = self.graph.get_node(id2)
            if v.getTag() == 0:
                self.reset_graph()
                return float('inf'), []
            dist = self.graph.get_node(id2).getWeight()
            path.insert(0, v.getKey())
            while v.getKey() != id1:
                path.insert(0, parent.get(v.getKey()).getKey())
                v = parent.get(v.getKey())

            return dist, path

        return None

    def reset_graph(self) -> None:
        """
        resets the state of the graph for algorithmic use
        """
        for node in self.graph.get_all_v().values():
            if node.getWeight() != sys.maxsize or node.getTag() != 0:
                node.setWeight(sys.maxsize)
                node.setTag(0)

    def connected_component(self, id1: int) -> list:
        if self.graph is None or id1 not in self.graph.vertices.keys():
            return []
        bfs1 = []
        bfs2 = []
        output = []
        self.bfs(id1, self.graph, bfs1)
        # transpose graph
        gr = self.graph.reverse_graph()
        self.bfs(id1, gr, bfs2)
        out = intersection(bfs1, bfs2, output)
        return out

    def bfs(self, v, graph, res):
        """

        """
        self.reset_graph()
        q = [v]
        res.append(v)
        graph.get_node(v).setTag(1)

        while q:
            ver = q.pop()
            for key, val in graph.all_out_edges_of_node(ver).items():
                if graph.get_node(key).getTag() == 0:
                    graph.get_node(key).setTag(1)
                    q.append(key)
                    res.append(key)

        return res

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        Notes:
        If the graph is None the function should return an empty list []
        """
        ans = []
        if self is None:
            return ans
        t = list(self.graph.vertices.keys())
        while t:
            scc = self.connected_component(t[0])
            for i in scc:
                t.remove(i)
            ans.append(scc)  # List[list]
        return ans

    def plot_graph(self) -> None:
        x = []
        y = []
        nodes = self.graph.get_all_v()
        for node in nodes.values():
            if node.getPos() is None:
                x_r = random.uniform(0, 1)
                y_r = random.uniform(0, 1)
                z_r = 0
                node.setPosition(x_r, y_r, z_r)
            x.append(node.getPos()[0])
            y.append(node.getPos()[1])

        fig, ax = plt.subplots()

        ax.scatter(x, y, color='blue', linewidths=1, s=100)  # plot the nodes in the graph in blue
        for node in self.graph.get_all_v().values():
            x1, y1 = (node.getPos()[0]), (node.getPos()[1])
            ax.annotate(node.getKey(), (x1, y1 + 0.012), size=15)

            for e in self.graph.all_out_edges_of_node(node.getKey()).items():
                item_x = self.graph.get_node(e[0]).getPos()[0]
                item_y = self.graph.get_node(e[0]).getPos()[1]
                plt.arrow(x1, y1, 0.98 * (item_x - x1), 0.98 * (item_y - y1), length_includes_head=True,
                          head_width=0.0004, head_length=0.0004, width=0.00001, fc='red', ec='black', zorder=1.2)
        plt.axis('off')
        plt.grid(color='grey', linestyle=':', linewidth=0.5)
        plt.title('Directed Weighted Graph:|V|=' + str(self.graph.v_size()) + ',' + '|E|= ' + str(self.graph.e_size()))
        plt.show()
