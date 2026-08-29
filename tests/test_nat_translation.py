"""
Test Case 5: NAT / Port Address Translation (PAT) Verification
"""
import unittest
from netmatrix.security.nat_engine import NATTable

class TestNatTranslation(unittest.TestCase):
    def test_nat_outbound_and_inbound_translation(self):
        nat = NATTable(public_ip="203.0.113.1")
        
        ext_ip, ext_port = nat.translate_outbound("192.168.1.100", 54321)
        self.assertEqual(ext_ip, "203.0.113.1")
        self.assertEqual(ext_port, 10000)
        
        # Same internal connection should map to same external port
        ext_ip2, ext_port2 = nat.translate_outbound("192.168.1.100", 54321)
        self.assertEqual(ext_port2, 10000)
        
        # Reverse lookup for inbound packet
        orig = nat.translate_inbound(10000)
        self.assertEqual(orig, ("192.168.1.100", 54321))

if __name__ == "__main__":
    unittest.main()
