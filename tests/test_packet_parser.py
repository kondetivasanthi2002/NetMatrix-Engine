"""
Test Case 1: Packet Parser & Low-Level Frame Verification
"""
import unittest
from netmatrix.core.ethernet import EthernetFrame, MacAddress
from netmatrix.core.ipv4_ipv6 import IPv4Packet
from netmatrix.core.tcp_udp import TCPHeader, UDPHeader

class TestPacketParser(unittest.TestCase):
    def test_ethernet_frame_pack_unpack(self):
        frame = EthernetFrame(dst_mac="AA:BB:CC:DD:EE:FF", src_mac="00:11:22:33:44:55", ethertype=0x0800, vlan_id=100, payload=b"Hello Network")
        raw = frame.pack()
        self.assertTrue(len(raw) > 14)
        unpacked = EthernetFrame.unpack(raw)
        self.assertEqual(unpacked.dst_mac.to_str(), "aa:bb:cc:dd:ee:ff")
        self.assertEqual(unpacked.src_mac.to_str(), "00:11:22:33:44:55")
        self.assertEqual(unpacked.vlan_id, 100)
        self.assertEqual(unpacked.payload, b"Hello Network")

    def test_ipv4_packet_routing_header(self):
        pkt = IPv4Packet(src_ip="192.168.1.10", dst_ip="10.0.0.1", proto=6, ttl=64, payload=b"TCP Segment")
        raw = pkt.pack()
        self.assertEqual(len(raw), 20 + len(b"TCP Segment"))
        unpacked = IPv4Packet.unpack(raw)
        self.assertEqual(unpacked.src_ip, "192.168.1.10")
        self.assertEqual(unpacked.dst_ip, "10.0.0.1")
        self.assertEqual(unpacked.protocol, 6)
        self.assertEqual(unpacked.ttl, 64)

    def test_tcp_udp_header_serialization(self):
        tcp = TCPHeader(src_port=12345, dst_port=80, seq_num=1000, ack_num=500, flags=0x12)
        raw_tcp = tcp.pack()
        unpacked_tcp = TCPHeader.unpack(raw_tcp)
        self.assertEqual(unpacked_tcp.src_port, 12345)
        self.assertEqual(unpacked_tcp.dst_port, 80)
        self.assertEqual(unpacked_tcp.seq_num, 1000)

        udp = UDPHeader(src_port=5353, dst_port=53, payload=b"DNS Query")
        raw_udp = udp.pack()
        unpacked_udp = UDPHeader.unpack(raw_udp)
        self.assertEqual(unpacked_udp.src_port, 5353)
        self.assertEqual(unpacked_udp.dst_port, 53)
        self.assertEqual(unpacked_udp.payload, b"DNS Query")

if __name__ == "__main__":
    unittest.main()
