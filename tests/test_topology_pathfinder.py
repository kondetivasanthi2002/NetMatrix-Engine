"""
Test Case 4: Network Topology Pathfinder & Dijkstra Verification
"""
import unittest
from netmatrix.routing.topology_graph import TopologyGraph

class TestTopologyPathfinder(unittest.TestCase):
    def test_dijkstra_shortest_path(self):
        topo = TopologyGraph()
        topo.add_link("Router_A", "Router_B", 10.0)
        topo.add_link("Router_B", "Router_C", 5.0)
        topo.add_link("Router_A", "Router_C", 20.0)
        
        cost, path = topo.shortest_path("Router_A", "Router_C")
        self.assertEqual(cost, 15.0)
        self.assertEqual(path, ["Router_A", "Router_B", "Router_C"])

if __name__ == "__main__":
    unittest.main()
