import unittest
from graph import DirectedGraph

class GraphTest (unittest.TestCase):

    def setUp(self):
        self.sample_graph = DirectedGraph()

    def test_graph_init(self):
        self.assertEqual(self.sample_graph.graph, {})

    def test_add_edge(self):
        self.sample_graph.add_edge("A", "B")
        self.assertIn("A", self.sample_graph.graph)
        self.assertIn("B", self.sample_graph.graph["A"])

        self.sample_graph.add_edge("A", "D")
        self.assertIn("A", self.sample_graph.graph)
        self.assertIn("D", self.sample_graph.graph["A"])

        self.sample_graph.add_edge("B", "C")
        self.assertIn("A", self.sample_graph.graph)
        self.assertIn("B", self.sample_graph.graph["A"])
        self.assertIn("B", self.sample_graph.graph)
        self.assertIn("C", self.sample_graph.graph["B"])

    def test_get_neighbours_for(self):
        self.sample_graph.add_edge("A", "B")
        self.sample_graph.add_edge("A", "D")
        self.assertEqual(["B", "D"], self.sample_graph.get_neighbours_for("A"))

    def test_path_between(self):
        self.sample_graph.add_edge("A", "B")
        self.sample_graph.add_edge("B", "C")
        self.assertTrue(self.sample_graph.path_between("A", "C"))
        self.assertFalse(self.sample_graph.path_between("A", "D"))
        self.assertFalse(self.sample_graph.path_between("A", "E"))

    def test_to_str(self):
        self.sample_graph.add_edge("A", "B")
        self.assertEqual(self.sample_graph.to_str(), "A ---> ['B']")


if __name__ == '__main__':
    unittest.main()