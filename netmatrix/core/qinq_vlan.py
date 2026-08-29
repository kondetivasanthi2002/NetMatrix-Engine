"""
802.1ad QinQ Dual VLAN Encapsulation & Tagging Engine
"""
import struct
from typing import Dict, Any, Optional

class QinQHeader:
    def __init__(self, outer_vlan: int, inner_vlan: int, ethertype: int = 0x0800):
        self.outer_vlan = outer_vlan
        self.inner_vlan = inner_vlan
        self.ethertype = ethertype

    def pack(self) -> bytes:
        outer = struct.pack("!HH", 0x88A8, self.outer_vlan & 0x0FFF)
        inner = struct.pack("!HH", 0x8100, self.inner_vlan & 0x0FFF)
        return outer + inner + struct.pack("!H", self.ethertype)
