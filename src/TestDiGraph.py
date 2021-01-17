from unittest import TestCase
from src.DiGraph import DiGraph


class MyTestCase(TestCase):

    def setUp(self) -> None:
        self.graph = DiGraph()
        # i=0....6
        for i in range(7):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1, 5)
        self.graph.add_edge(1, 3, 1)
        self.graph.add_edge(2, 4, 0.7)
        self.graph.add_edge(0, 5, 2)
        self.graph.add_edge(4, 0, 1.2)
        self.graph.add_edge(4, 6, 2)
        self.graph.add_edge(1, 2, 9)
        self.graph.add_edge(1, 5, 1)
        self.graph.add_edge(5, 3, 4)
        self.graph.add_edge(0, 6, 1)

    def test_v_size(self):
        size = self.graph.v_size()
        self.assertEqual(size, 7)

    def test_e_size(self):
        edges_size = self.graph.e_size()
        self.assertEqual(edges_size, 10)

    def test_get_all_v(self):
        self.assertEqual(len(self.graph.get_all_v()), 7)

    def test_getNode(self):
        vertex = self.graph.get_node(4)
        self.assertEqual(4, vertex.getKey())

    def test_add_edge(self):
        # negative edge
        self.assertFalse(self.graph.add_edge(1, 3, -9))
        # id1==id2
        self.assertFalse(self.graph.add_edge(1, 1, 4))
        # the edge already exist
        self.assertFalse(self.graph.add_edge(1, 3, 1))

    def test_remove_edge(self):
        # Removes 3 edge from the graph
        self.graph.remove_edge(0, 1)
        self.graph.remove_edge(0, 6)
        self.graph.remove_edge(1, 3)

        edges_size = self.graph.num_of_edges

        self.assertEqual(edges_size, 7)

    def test_all_out_edges_of_node(self):
        actual = list(self.graph.all_out_edges_of_node(0))
        expected = [1, 5, 6]
        self.assertEqual(actual, expected)

    def test_all_in_edges_of_node(self):
        actual = list(self.graph.all_in_edges_of_node(5))
        expected = [0, 1]
        self.assertEqual(actual, expected)

    def test_remove_node(self):
        s = self.graph.v_size()
        self.assertEqual(s, 7)
        self.graph.remove_node(5)
        self.graph.remove_node(1)
        size = self.graph.v_size()
        self.assertEqual(size, 5)
        self.assertFalse(self.graph.remove_node(12))

    def test_graph_transpose(self):
        a = self.graph.get_node(1).get_edge_Weight(3)
        gr = self.graph.reverse_graph()
        b = gr.get_node(3).get_edge_Weight(1)
        self.assertEqual(a, b)
