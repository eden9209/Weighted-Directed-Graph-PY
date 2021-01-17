from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

"""
https://www.youtube.com/watch?v=vEL0tLa7F2A  -  self.algo
https://www.programiz.com/dsa/strongly-connected-components - self.algo2
"""


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        self.graph = DiGraph()
        for vertex in range(5):
            self.graph.add_node(vertex)
        self.graph.add_edge(0, 1, 2)
        self.graph.add_edge(1, 2, 1)
        self.graph.add_edge(1, 4, 6)
        self.graph.add_edge(2, 3, 2)
        self.graph.add_edge(3, 4, 1)
        self.algo = GraphAlgo(self.graph)  # init
        ###########
        self.g = DiGraph()
        for vertex in range(8):
            self.g.add_node(vertex)
        self.g.add_edge(0, 1, 0)
        self.g.add_edge(1, 2, 0)
        self.g.add_edge(2, 3, 0)
        self.g.add_edge(3, 0, 0)
        self.g.add_edge(2, 4, 0)
        self.g.add_edge(4, 5, 0)
        self.g.add_edge(5, 6, 0)
        self.g.add_edge(6, 4, 0)
        self.g.add_edge(6, 7, 0)
        self.algo2 = GraphAlgo(self.g)  # init

    def test_get_graph(self):
        self.assertTrue(self.graph, self.algo.get_graph())
        self.assertTrue(self.g, self.algo2.get_graph())

    def test_shortest_path(self):
        """
        https://www.youtube.com/watch?v=vEL0tLa7F2A
        build this graph in the setup
        self.algo
        """
        self.assertEqual(self.algo.shortest_path(0, 4), (6, [0, 1, 2, 3, 4]))
        self.assertEqual(self.algo.shortest_path(0, 3), (5, [0, 1, 2, 3]))
        # node not exist in a graph
        self.assertEqual(self.algo.shortest_path(0, 10), None)
        # no path between two nodes:
        self.assertEqual(self.algo.shortest_path(4, 3), (float('inf'), []))

    def test_load_from_json(self):
        self.assertTrue(self.algo.load_from_json("../data/A0"))  # True if the loading was successful
        graph_A0 = DiGraph()
        graph_A0.add_node(0, (35.18753053591606, 32.10378225882353, 0.0))
        graph_A0.add_node(1, (35.18958953510896, 32.10785303529412, 0.0))
        graph_A0.add_node(2, (35.19341035835351, 32.10610841680672, 0.0))
        graph_A0.add_node(3, (35.197528356739305, 32.1053088, 0.0))
        graph_A0.add_node(4, (35.2016888087167, 32.10601755126051, 0.0))
        graph_A0.add_node(5, (35.20582803389831, 32.10625380168067, 0.0))
        graph_A0.add_node(6, (35.20792948668281, 32.10470908739496, 0.0))
        graph_A0.add_node(7, (35.20746249717514, 32.10254648739496, 0.0))
        graph_A0.add_node(8, (35.20319591121872, 32.1031462, 0.0))
        graph_A0.add_node(9, (35.19597880064568, 32.10154696638656, 0.0))
        graph_A0.add_node(10, (35.18910131880549, 32.103618700840336, 0.0))

        graph_A0.add_edge(0, 1, 1.4004465106761335)
        graph_A0.add_edge(0, 10, 1.4620268165085584)
        graph_A0.add_edge(1, 0, 1.8884659521433524)
        graph_A0.add_edge(1, 2, 1.7646903245689283)
        graph_A0.add_edge(2, 1, 1.7155926739282625)
        graph_A0.add_edge(2, 3, 1.1435447583365383)
        graph_A0.add_edge(3, 2, 1.0980094622804095)
        graph_A0.add_edge(3, 4, 1.4301580756736283)
        graph_A0.add_edge(4, 3, 1.4899867265011255)
        graph_A0.add_edge(4, 5, 1.9442789961315767)
        graph_A0.add_edge(5, 4, 1.4622464066335845)
        graph_A0.add_edge(5, 6, 1.160662656360925)
        graph_A0.add_edge(6, 5, 1.6677173820549975)
        graph_A0.add_edge(6, 7, 1.3968360163668776)
        graph_A0.add_edge(7, 6, 1.0176531013725074)
        graph_A0.add_edge(7, 8, 1.354895648936991)
        graph_A0.add_edge(8, 7, 1.6449953452844968)
        graph_A0.add_edge(8, 9, 1.8526880332753517)
        graph_A0.add_edge(9, 8, 1.4575484853801393)
        graph_A0.add_edge(9, 10, 1.022651770039933)
        graph_A0.add_edge(10, 0, 1.1761238717867548)
        graph_A0.add_edge(10, 9, 1.0887225789883779)

        self.assertEqual(self.algo.get_graph().__repr__(), graph_A0.__repr__())
        self.assertEqual(self.algo.get_graph().v_size(), graph_A0.v_size())
        self.assertEqual(self.algo.get_graph().e_size(), graph_A0.e_size())
        self.assertEqual(self.algo.get_graph().get_mc(), graph_A0.get_mc())
        self.assertEqual(self.algo.get_graph().get_all_v().keys(), graph_A0.get_all_v().keys())

    def test_connected_component(self):
        l = self.algo2.connected_component(0)
        self.assertEqual(str(l), str([0, 1, 2, 3]))
        l1 = self.algo2.connected_component(4)
        self.assertEqual(str(l1), str([4, 5, 6]))
        l2 = self.algo2.connected_component(7)
        self.assertEqual(str(l2), str([7]))

    def test_connected_components(self):
        list_of_list = self.algo2.connected_components()
        expected = [[0, 1, 2, 3], [4, 5, 6], [7]]
        print(list_of_list)
        print(expected)
        listOut = []
        for item in list_of_list:
            temp = []
            for inner in item:
                for b in expected:
                    if inner == b:
                        temp.append(b)
            listOut.append(temp)

        self.assertEqual(listOut, [[], [], []])
