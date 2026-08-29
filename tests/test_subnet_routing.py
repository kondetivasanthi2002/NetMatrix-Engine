"""
Test Case 2: Subnet Arithmetic & Routing Information Base Verification
"""
import unittest
from netmatrix.routing.subnet_calculator import CIDRSubnet
from netmatrix.routing.router_state import VirtualRouterInstance

class TestSubnetRouting(unittest.TestCase):
    def test_cidr_subnet_calculations(self):
        sub = CIDRSubnet("192.168.10.0/24")
        self.assertEqual(sub.get_network_address(), "192.168.10.0")
        self.assertEqual(sub.get_broadcast_address(), "192.168.10.255")
        self.assertEqual(sub.get_netmask(), "255.255.255.0")
        self.assertEqual(sub.total_hosts(), 254)
        self.assertTrue(sub.contains("192.168.10.45"))
        self.assertFalse(sub.contains("192.168.11.1"))

    def test_virtual_router_fib_lookup(self):
        router = VirtualRouterInstance(router_id="10.0.0.1")
        router.add_route("192.168.1.0/24", "10.0.0.2", metric=5)
        router.add_route("172.16.0.0/16", "10.0.0.3", metric=10)
        
        self.assertEqual(router.lookup("192.168.1.0/24"), "10.0.0.2")
        self.assertEqual(router.lookup("172.16.0.0/16"), "10.0.0.3")

if __name__ == "__main__":
    unittest.main()
