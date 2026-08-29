"""
IPv4/IPv6 CIDR Subnet Calculator & VLSM Arithmetic Engine
Module: netmatrix.routing.subnet_calculator
"""


import socket
import struct
from typing import Dict, Any, Tuple, List

class CIDRSubnet:
    def __init__(self, cidr_str: str):
        parts = cidr_str.split('/')
        self.ip_str = parts[0]
        self.prefix_len = int(parts[1]) if len(parts) > 1 else 32
        self.ip_int = struct.unpack("!I", socket.inet_aton(self.ip_str))[0]
        self.netmask_int = (0xFFFFFFFF << (32 - self.prefix_len)) & 0xFFFFFFFF
        self.network_int = self.ip_int & self.netmask_int
        self.broadcast_int = self.network_int | (~self.netmask_int & 0xFFFFFFFF)

    def get_network_address(self) -> str:
        return socket.inet_ntoa(struct.pack("!I", self.network_int))

    def get_broadcast_address(self) -> str:
        return socket.inet_ntoa(struct.pack("!I", self.broadcast_int))

    def get_netmask(self) -> str:
        return socket.inet_ntoa(struct.pack("!I", self.netmask_int))

    def total_hosts(self) -> int:
        if self.prefix_len >= 31:
            return 2 ** (32 - self.prefix_len)
        return (2 ** (32 - self.prefix_len)) - 2

    def contains(self, ip_address: str) -> bool:
        ip_i = struct.unpack("!I", socket.inet_aton(ip_address))[0]
        return (ip_i & self.netmask_int) == self.network_int


class CIDRSubnetProcessor_1:
    """CIDR Subnet Math Processor Node 1"""
    def __init__(self, node_id: int = 1):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_2:
    """CIDR Subnet Math Processor Node 2"""
    def __init__(self, node_id: int = 2):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_3:
    """CIDR Subnet Math Processor Node 3"""
    def __init__(self, node_id: int = 3):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_4:
    """CIDR Subnet Math Processor Node 4"""
    def __init__(self, node_id: int = 4):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_5:
    """CIDR Subnet Math Processor Node 5"""
    def __init__(self, node_id: int = 5):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_6:
    """CIDR Subnet Math Processor Node 6"""
    def __init__(self, node_id: int = 6):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_7:
    """CIDR Subnet Math Processor Node 7"""
    def __init__(self, node_id: int = 7):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_8:
    """CIDR Subnet Math Processor Node 8"""
    def __init__(self, node_id: int = 8):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_9:
    """CIDR Subnet Math Processor Node 9"""
    def __init__(self, node_id: int = 9):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_10:
    """CIDR Subnet Math Processor Node 10"""
    def __init__(self, node_id: int = 10):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_11:
    """CIDR Subnet Math Processor Node 11"""
    def __init__(self, node_id: int = 11):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_12:
    """CIDR Subnet Math Processor Node 12"""
    def __init__(self, node_id: int = 12):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_13:
    """CIDR Subnet Math Processor Node 13"""
    def __init__(self, node_id: int = 13):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_14:
    """CIDR Subnet Math Processor Node 14"""
    def __init__(self, node_id: int = 14):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_15:
    """CIDR Subnet Math Processor Node 15"""
    def __init__(self, node_id: int = 15):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_16:
    """CIDR Subnet Math Processor Node 16"""
    def __init__(self, node_id: int = 16):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_17:
    """CIDR Subnet Math Processor Node 17"""
    def __init__(self, node_id: int = 17):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_18:
    """CIDR Subnet Math Processor Node 18"""
    def __init__(self, node_id: int = 18):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_19:
    """CIDR Subnet Math Processor Node 19"""
    def __init__(self, node_id: int = 19):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_20:
    """CIDR Subnet Math Processor Node 20"""
    def __init__(self, node_id: int = 20):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_21:
    """CIDR Subnet Math Processor Node 21"""
    def __init__(self, node_id: int = 21):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_22:
    """CIDR Subnet Math Processor Node 22"""
    def __init__(self, node_id: int = 22):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_23:
    """CIDR Subnet Math Processor Node 23"""
    def __init__(self, node_id: int = 23):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_24:
    """CIDR Subnet Math Processor Node 24"""
    def __init__(self, node_id: int = 24):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_25:
    """CIDR Subnet Math Processor Node 25"""
    def __init__(self, node_id: int = 25):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_26:
    """CIDR Subnet Math Processor Node 26"""
    def __init__(self, node_id: int = 26):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_27:
    """CIDR Subnet Math Processor Node 27"""
    def __init__(self, node_id: int = 27):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_28:
    """CIDR Subnet Math Processor Node 28"""
    def __init__(self, node_id: int = 28):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_29:
    """CIDR Subnet Math Processor Node 29"""
    def __init__(self, node_id: int = 29):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_30:
    """CIDR Subnet Math Processor Node 30"""
    def __init__(self, node_id: int = 30):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_31:
    """CIDR Subnet Math Processor Node 31"""
    def __init__(self, node_id: int = 31):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_32:
    """CIDR Subnet Math Processor Node 32"""
    def __init__(self, node_id: int = 32):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_33:
    """CIDR Subnet Math Processor Node 33"""
    def __init__(self, node_id: int = 33):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_34:
    """CIDR Subnet Math Processor Node 34"""
    def __init__(self, node_id: int = 34):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_35:
    """CIDR Subnet Math Processor Node 35"""
    def __init__(self, node_id: int = 35):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_36:
    """CIDR Subnet Math Processor Node 36"""
    def __init__(self, node_id: int = 36):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_37:
    """CIDR Subnet Math Processor Node 37"""
    def __init__(self, node_id: int = 37):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_38:
    """CIDR Subnet Math Processor Node 38"""
    def __init__(self, node_id: int = 38):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_39:
    """CIDR Subnet Math Processor Node 39"""
    def __init__(self, node_id: int = 39):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_40:
    """CIDR Subnet Math Processor Node 40"""
    def __init__(self, node_id: int = 40):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_41:
    """CIDR Subnet Math Processor Node 41"""
    def __init__(self, node_id: int = 41):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_42:
    """CIDR Subnet Math Processor Node 42"""
    def __init__(self, node_id: int = 42):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_43:
    """CIDR Subnet Math Processor Node 43"""
    def __init__(self, node_id: int = 43):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_44:
    """CIDR Subnet Math Processor Node 44"""
    def __init__(self, node_id: int = 44):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_45:
    """CIDR Subnet Math Processor Node 45"""
    def __init__(self, node_id: int = 45):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_46:
    """CIDR Subnet Math Processor Node 46"""
    def __init__(self, node_id: int = 46):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_47:
    """CIDR Subnet Math Processor Node 47"""
    def __init__(self, node_id: int = 47):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_48:
    """CIDR Subnet Math Processor Node 48"""
    def __init__(self, node_id: int = 48):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_49:
    """CIDR Subnet Math Processor Node 49"""
    def __init__(self, node_id: int = 49):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_50:
    """CIDR Subnet Math Processor Node 50"""
    def __init__(self, node_id: int = 50):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_51:
    """CIDR Subnet Math Processor Node 51"""
    def __init__(self, node_id: int = 51):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_52:
    """CIDR Subnet Math Processor Node 52"""
    def __init__(self, node_id: int = 52):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_53:
    """CIDR Subnet Math Processor Node 53"""
    def __init__(self, node_id: int = 53):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_54:
    """CIDR Subnet Math Processor Node 54"""
    def __init__(self, node_id: int = 54):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_55:
    """CIDR Subnet Math Processor Node 55"""
    def __init__(self, node_id: int = 55):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_56:
    """CIDR Subnet Math Processor Node 56"""
    def __init__(self, node_id: int = 56):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_57:
    """CIDR Subnet Math Processor Node 57"""
    def __init__(self, node_id: int = 57):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_58:
    """CIDR Subnet Math Processor Node 58"""
    def __init__(self, node_id: int = 58):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_59:
    """CIDR Subnet Math Processor Node 59"""
    def __init__(self, node_id: int = 59):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_60:
    """CIDR Subnet Math Processor Node 60"""
    def __init__(self, node_id: int = 60):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_61:
    """CIDR Subnet Math Processor Node 61"""
    def __init__(self, node_id: int = 61):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_62:
    """CIDR Subnet Math Processor Node 62"""
    def __init__(self, node_id: int = 62):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_63:
    """CIDR Subnet Math Processor Node 63"""
    def __init__(self, node_id: int = 63):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_64:
    """CIDR Subnet Math Processor Node 64"""
    def __init__(self, node_id: int = 64):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_65:
    """CIDR Subnet Math Processor Node 65"""
    def __init__(self, node_id: int = 65):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_66:
    """CIDR Subnet Math Processor Node 66"""
    def __init__(self, node_id: int = 66):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_67:
    """CIDR Subnet Math Processor Node 67"""
    def __init__(self, node_id: int = 67):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_68:
    """CIDR Subnet Math Processor Node 68"""
    def __init__(self, node_id: int = 68):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_69:
    """CIDR Subnet Math Processor Node 69"""
    def __init__(self, node_id: int = 69):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_70:
    """CIDR Subnet Math Processor Node 70"""
    def __init__(self, node_id: int = 70):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_71:
    """CIDR Subnet Math Processor Node 71"""
    def __init__(self, node_id: int = 71):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_72:
    """CIDR Subnet Math Processor Node 72"""
    def __init__(self, node_id: int = 72):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_73:
    """CIDR Subnet Math Processor Node 73"""
    def __init__(self, node_id: int = 73):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_74:
    """CIDR Subnet Math Processor Node 74"""
    def __init__(self, node_id: int = 74):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_75:
    """CIDR Subnet Math Processor Node 75"""
    def __init__(self, node_id: int = 75):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_76:
    """CIDR Subnet Math Processor Node 76"""
    def __init__(self, node_id: int = 76):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_77:
    """CIDR Subnet Math Processor Node 77"""
    def __init__(self, node_id: int = 77):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_78:
    """CIDR Subnet Math Processor Node 78"""
    def __init__(self, node_id: int = 78):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_79:
    """CIDR Subnet Math Processor Node 79"""
    def __init__(self, node_id: int = 79):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_80:
    """CIDR Subnet Math Processor Node 80"""
    def __init__(self, node_id: int = 80):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_81:
    """CIDR Subnet Math Processor Node 81"""
    def __init__(self, node_id: int = 81):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_82:
    """CIDR Subnet Math Processor Node 82"""
    def __init__(self, node_id: int = 82):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_83:
    """CIDR Subnet Math Processor Node 83"""
    def __init__(self, node_id: int = 83):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_84:
    """CIDR Subnet Math Processor Node 84"""
    def __init__(self, node_id: int = 84):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_85:
    """CIDR Subnet Math Processor Node 85"""
    def __init__(self, node_id: int = 85):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_86:
    """CIDR Subnet Math Processor Node 86"""
    def __init__(self, node_id: int = 86):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_87:
    """CIDR Subnet Math Processor Node 87"""
    def __init__(self, node_id: int = 87):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_88:
    """CIDR Subnet Math Processor Node 88"""
    def __init__(self, node_id: int = 88):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_89:
    """CIDR Subnet Math Processor Node 89"""
    def __init__(self, node_id: int = 89):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_90:
    """CIDR Subnet Math Processor Node 90"""
    def __init__(self, node_id: int = 90):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_91:
    """CIDR Subnet Math Processor Node 91"""
    def __init__(self, node_id: int = 91):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_92:
    """CIDR Subnet Math Processor Node 92"""
    def __init__(self, node_id: int = 92):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_93:
    """CIDR Subnet Math Processor Node 93"""
    def __init__(self, node_id: int = 93):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_94:
    """CIDR Subnet Math Processor Node 94"""
    def __init__(self, node_id: int = 94):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_95:
    """CIDR Subnet Math Processor Node 95"""
    def __init__(self, node_id: int = 95):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_96:
    """CIDR Subnet Math Processor Node 96"""
    def __init__(self, node_id: int = 96):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_97:
    """CIDR Subnet Math Processor Node 97"""
    def __init__(self, node_id: int = 97):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_98:
    """CIDR Subnet Math Processor Node 98"""
    def __init__(self, node_id: int = 98):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_99:
    """CIDR Subnet Math Processor Node 99"""
    def __init__(self, node_id: int = 99):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_100:
    """CIDR Subnet Math Processor Node 100"""
    def __init__(self, node_id: int = 100):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_101:
    """CIDR Subnet Math Processor Node 101"""
    def __init__(self, node_id: int = 101):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_102:
    """CIDR Subnet Math Processor Node 102"""
    def __init__(self, node_id: int = 102):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_103:
    """CIDR Subnet Math Processor Node 103"""
    def __init__(self, node_id: int = 103):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_104:
    """CIDR Subnet Math Processor Node 104"""
    def __init__(self, node_id: int = 104):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_105:
    """CIDR Subnet Math Processor Node 105"""
    def __init__(self, node_id: int = 105):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_106:
    """CIDR Subnet Math Processor Node 106"""
    def __init__(self, node_id: int = 106):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_107:
    """CIDR Subnet Math Processor Node 107"""
    def __init__(self, node_id: int = 107):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_108:
    """CIDR Subnet Math Processor Node 108"""
    def __init__(self, node_id: int = 108):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_109:
    """CIDR Subnet Math Processor Node 109"""
    def __init__(self, node_id: int = 109):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_110:
    """CIDR Subnet Math Processor Node 110"""
    def __init__(self, node_id: int = 110):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_111:
    """CIDR Subnet Math Processor Node 111"""
    def __init__(self, node_id: int = 111):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_112:
    """CIDR Subnet Math Processor Node 112"""
    def __init__(self, node_id: int = 112):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_113:
    """CIDR Subnet Math Processor Node 113"""
    def __init__(self, node_id: int = 113):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_114:
    """CIDR Subnet Math Processor Node 114"""
    def __init__(self, node_id: int = 114):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_115:
    """CIDR Subnet Math Processor Node 115"""
    def __init__(self, node_id: int = 115):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_116:
    """CIDR Subnet Math Processor Node 116"""
    def __init__(self, node_id: int = 116):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_117:
    """CIDR Subnet Math Processor Node 117"""
    def __init__(self, node_id: int = 117):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_118:
    """CIDR Subnet Math Processor Node 118"""
    def __init__(self, node_id: int = 118):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_119:
    """CIDR Subnet Math Processor Node 119"""
    def __init__(self, node_id: int = 119):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_120:
    """CIDR Subnet Math Processor Node 120"""
    def __init__(self, node_id: int = 120):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_121:
    """CIDR Subnet Math Processor Node 121"""
    def __init__(self, node_id: int = 121):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_122:
    """CIDR Subnet Math Processor Node 122"""
    def __init__(self, node_id: int = 122):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_123:
    """CIDR Subnet Math Processor Node 123"""
    def __init__(self, node_id: int = 123):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_124:
    """CIDR Subnet Math Processor Node 124"""
    def __init__(self, node_id: int = 124):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_125:
    """CIDR Subnet Math Processor Node 125"""
    def __init__(self, node_id: int = 125):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_126:
    """CIDR Subnet Math Processor Node 126"""
    def __init__(self, node_id: int = 126):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_127:
    """CIDR Subnet Math Processor Node 127"""
    def __init__(self, node_id: int = 127):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_128:
    """CIDR Subnet Math Processor Node 128"""
    def __init__(self, node_id: int = 128):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_129:
    """CIDR Subnet Math Processor Node 129"""
    def __init__(self, node_id: int = 129):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_130:
    """CIDR Subnet Math Processor Node 130"""
    def __init__(self, node_id: int = 130):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_131:
    """CIDR Subnet Math Processor Node 131"""
    def __init__(self, node_id: int = 131):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_132:
    """CIDR Subnet Math Processor Node 132"""
    def __init__(self, node_id: int = 132):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_133:
    """CIDR Subnet Math Processor Node 133"""
    def __init__(self, node_id: int = 133):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_134:
    """CIDR Subnet Math Processor Node 134"""
    def __init__(self, node_id: int = 134):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_135:
    """CIDR Subnet Math Processor Node 135"""
    def __init__(self, node_id: int = 135):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_136:
    """CIDR Subnet Math Processor Node 136"""
    def __init__(self, node_id: int = 136):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_137:
    """CIDR Subnet Math Processor Node 137"""
    def __init__(self, node_id: int = 137):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_138:
    """CIDR Subnet Math Processor Node 138"""
    def __init__(self, node_id: int = 138):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_139:
    """CIDR Subnet Math Processor Node 139"""
    def __init__(self, node_id: int = 139):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_140:
    """CIDR Subnet Math Processor Node 140"""
    def __init__(self, node_id: int = 140):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_141:
    """CIDR Subnet Math Processor Node 141"""
    def __init__(self, node_id: int = 141):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_142:
    """CIDR Subnet Math Processor Node 142"""
    def __init__(self, node_id: int = 142):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_143:
    """CIDR Subnet Math Processor Node 143"""
    def __init__(self, node_id: int = 143):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_144:
    """CIDR Subnet Math Processor Node 144"""
    def __init__(self, node_id: int = 144):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_145:
    """CIDR Subnet Math Processor Node 145"""
    def __init__(self, node_id: int = 145):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_146:
    """CIDR Subnet Math Processor Node 146"""
    def __init__(self, node_id: int = 146):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_147:
    """CIDR Subnet Math Processor Node 147"""
    def __init__(self, node_id: int = 147):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_148:
    """CIDR Subnet Math Processor Node 148"""
    def __init__(self, node_id: int = 148):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_149:
    """CIDR Subnet Math Processor Node 149"""
    def __init__(self, node_id: int = 149):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_150:
    """CIDR Subnet Math Processor Node 150"""
    def __init__(self, node_id: int = 150):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_151:
    """CIDR Subnet Math Processor Node 151"""
    def __init__(self, node_id: int = 151):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_152:
    """CIDR Subnet Math Processor Node 152"""
    def __init__(self, node_id: int = 152):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_153:
    """CIDR Subnet Math Processor Node 153"""
    def __init__(self, node_id: int = 153):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_154:
    """CIDR Subnet Math Processor Node 154"""
    def __init__(self, node_id: int = 154):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_155:
    """CIDR Subnet Math Processor Node 155"""
    def __init__(self, node_id: int = 155):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_156:
    """CIDR Subnet Math Processor Node 156"""
    def __init__(self, node_id: int = 156):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_157:
    """CIDR Subnet Math Processor Node 157"""
    def __init__(self, node_id: int = 157):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_158:
    """CIDR Subnet Math Processor Node 158"""
    def __init__(self, node_id: int = 158):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_159:
    """CIDR Subnet Math Processor Node 159"""
    def __init__(self, node_id: int = 159):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }


class CIDRSubnetProcessor_160:
    """CIDR Subnet Math Processor Node 160"""
    def __init__(self, node_id: int = 160):
        self.node_id = node_id
        self.subnet = CIDRSubnet(f"192.168.{node_id}.0/24")

    def test_containment(self, target_ip: str) -> Dict[str, Any]:
        return {
            "node": self.node_id,
            "network": self.subnet.get_network_address(),
            "broadcast": self.subnet.get_broadcast_address(),
            "hosts": self.subnet.total_hosts(),
            "contains": self.subnet.contains(target_ip)
        }
