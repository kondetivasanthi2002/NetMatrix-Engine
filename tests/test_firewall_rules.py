"""
Test Case 3: Stateful Firewall & SPI Filter Verification
"""
import unittest
from netmatrix.security.firewall_engine import StatefulFirewallModule

class TestFirewallRules(unittest.TestCase):
    def test_firewall_stateful_filtering(self):
        fw = StatefulFirewallModule(module_id=1)
        
        # Matching HTTPS rule (Rule 1: ACCEPT)
        res1 = fw.filter_packet("192.168.1.50", 443, "TCP")
        self.assertEqual(res1, "ACCEPT")
        
        # Matching Telnet rule (Rule 2: DROP)
        res2 = fw.filter_packet("192.168.1.50", 23, "TCP")
        self.assertEqual(res2, "DROP")
        
        # Unmatched port (Default: DROP)
        res3 = fw.filter_packet("192.168.1.50", 9999, "TCP")
        self.assertEqual(res3, "DROP")

if __name__ == "__main__":
    unittest.main()
