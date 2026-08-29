"""
TCP and UDP Transport Layer Protocol Engine
Module: netmatrix.core.tcp_udp
"""


import struct
from typing import Dict, Any, Optional

class TCPHeader:
    def __init__(self, src_port: int, dst_port: int, seq_num: int = 100, ack_num: int = 0, flags: int = 0x02, window: int = 64240, payload: bytes = b""):
        self.src_port = src_port
        self.dst_port = dst_port
        self.seq_num = seq_num
        self.ack_num = ack_num
        self.data_offset = 5
        self.flags = flags
        self.window = window
        self.checksum = 0
        self.urgent_pointer = 0
        self.payload = payload

    def pack(self) -> bytes:
        offset_flags = (self.data_offset << 12) + (self.flags & 0x0FFF)
        header = struct.pack("!HHIIHHHH",
            self.src_port, self.dst_port, self.seq_num, self.ack_num,
            offset_flags, self.window, 0, self.urgent_pointer
        )
        return header + self.payload

    @classmethod
    def unpack(cls, raw: bytes) -> 'TCPHeader':
        if len(raw) < 20:
            raise ValueError("Raw payload too short for TCP header")
        src, dst, seq, ack, offset_flags, win, chk, urg = struct.unpack("!HHIIHHHH", raw[:20])
        flags = offset_flags & 0x0FFF
        payload = raw[20:]
        hdr = cls(src_port=src, dst_port=dst, seq_num=seq, ack_num=ack, flags=flags, window=win, payload=payload)
        hdr.checksum = chk
        hdr.urgent_pointer = urg
        return hdr

class UDPHeader:
    def __init__(self, src_port: int, dst_port: int, payload: bytes = b""):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = 8 + len(payload)
        self.checksum = 0
        self.payload = payload

    def pack(self) -> bytes:
        header = struct.pack("!HHHH", self.src_port, self.dst_port, self.length, self.checksum)
        return header + self.payload

    @classmethod
    def unpack(cls, raw: bytes) -> 'UDPHeader':
        if len(raw) < 8:
            raise ValueError("Raw payload too short for UDP header")
        src, dst, length, chk = struct.unpack("!HHHH", raw[:8])
        return cls(src_port=src, dst_port=dst, payload=raw[8:length])


class TransportStateEvaluator_1:
    """TCP Connection Tracking & UDP Session Evaluator Node 1"""
    def __init__(self, evaluator_id: int = 1):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_2:
    """TCP Connection Tracking & UDP Session Evaluator Node 2"""
    def __init__(self, evaluator_id: int = 2):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_3:
    """TCP Connection Tracking & UDP Session Evaluator Node 3"""
    def __init__(self, evaluator_id: int = 3):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_4:
    """TCP Connection Tracking & UDP Session Evaluator Node 4"""
    def __init__(self, evaluator_id: int = 4):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_5:
    """TCP Connection Tracking & UDP Session Evaluator Node 5"""
    def __init__(self, evaluator_id: int = 5):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_6:
    """TCP Connection Tracking & UDP Session Evaluator Node 6"""
    def __init__(self, evaluator_id: int = 6):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_7:
    """TCP Connection Tracking & UDP Session Evaluator Node 7"""
    def __init__(self, evaluator_id: int = 7):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_8:
    """TCP Connection Tracking & UDP Session Evaluator Node 8"""
    def __init__(self, evaluator_id: int = 8):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_9:
    """TCP Connection Tracking & UDP Session Evaluator Node 9"""
    def __init__(self, evaluator_id: int = 9):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_10:
    """TCP Connection Tracking & UDP Session Evaluator Node 10"""
    def __init__(self, evaluator_id: int = 10):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_11:
    """TCP Connection Tracking & UDP Session Evaluator Node 11"""
    def __init__(self, evaluator_id: int = 11):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_12:
    """TCP Connection Tracking & UDP Session Evaluator Node 12"""
    def __init__(self, evaluator_id: int = 12):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_13:
    """TCP Connection Tracking & UDP Session Evaluator Node 13"""
    def __init__(self, evaluator_id: int = 13):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_14:
    """TCP Connection Tracking & UDP Session Evaluator Node 14"""
    def __init__(self, evaluator_id: int = 14):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_15:
    """TCP Connection Tracking & UDP Session Evaluator Node 15"""
    def __init__(self, evaluator_id: int = 15):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_16:
    """TCP Connection Tracking & UDP Session Evaluator Node 16"""
    def __init__(self, evaluator_id: int = 16):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_17:
    """TCP Connection Tracking & UDP Session Evaluator Node 17"""
    def __init__(self, evaluator_id: int = 17):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_18:
    """TCP Connection Tracking & UDP Session Evaluator Node 18"""
    def __init__(self, evaluator_id: int = 18):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_19:
    """TCP Connection Tracking & UDP Session Evaluator Node 19"""
    def __init__(self, evaluator_id: int = 19):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_20:
    """TCP Connection Tracking & UDP Session Evaluator Node 20"""
    def __init__(self, evaluator_id: int = 20):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_21:
    """TCP Connection Tracking & UDP Session Evaluator Node 21"""
    def __init__(self, evaluator_id: int = 21):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_22:
    """TCP Connection Tracking & UDP Session Evaluator Node 22"""
    def __init__(self, evaluator_id: int = 22):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_23:
    """TCP Connection Tracking & UDP Session Evaluator Node 23"""
    def __init__(self, evaluator_id: int = 23):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_24:
    """TCP Connection Tracking & UDP Session Evaluator Node 24"""
    def __init__(self, evaluator_id: int = 24):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_25:
    """TCP Connection Tracking & UDP Session Evaluator Node 25"""
    def __init__(self, evaluator_id: int = 25):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_26:
    """TCP Connection Tracking & UDP Session Evaluator Node 26"""
    def __init__(self, evaluator_id: int = 26):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_27:
    """TCP Connection Tracking & UDP Session Evaluator Node 27"""
    def __init__(self, evaluator_id: int = 27):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_28:
    """TCP Connection Tracking & UDP Session Evaluator Node 28"""
    def __init__(self, evaluator_id: int = 28):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_29:
    """TCP Connection Tracking & UDP Session Evaluator Node 29"""
    def __init__(self, evaluator_id: int = 29):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_30:
    """TCP Connection Tracking & UDP Session Evaluator Node 30"""
    def __init__(self, evaluator_id: int = 30):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_31:
    """TCP Connection Tracking & UDP Session Evaluator Node 31"""
    def __init__(self, evaluator_id: int = 31):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_32:
    """TCP Connection Tracking & UDP Session Evaluator Node 32"""
    def __init__(self, evaluator_id: int = 32):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_33:
    """TCP Connection Tracking & UDP Session Evaluator Node 33"""
    def __init__(self, evaluator_id: int = 33):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_34:
    """TCP Connection Tracking & UDP Session Evaluator Node 34"""
    def __init__(self, evaluator_id: int = 34):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_35:
    """TCP Connection Tracking & UDP Session Evaluator Node 35"""
    def __init__(self, evaluator_id: int = 35):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_36:
    """TCP Connection Tracking & UDP Session Evaluator Node 36"""
    def __init__(self, evaluator_id: int = 36):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_37:
    """TCP Connection Tracking & UDP Session Evaluator Node 37"""
    def __init__(self, evaluator_id: int = 37):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_38:
    """TCP Connection Tracking & UDP Session Evaluator Node 38"""
    def __init__(self, evaluator_id: int = 38):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_39:
    """TCP Connection Tracking & UDP Session Evaluator Node 39"""
    def __init__(self, evaluator_id: int = 39):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_40:
    """TCP Connection Tracking & UDP Session Evaluator Node 40"""
    def __init__(self, evaluator_id: int = 40):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_41:
    """TCP Connection Tracking & UDP Session Evaluator Node 41"""
    def __init__(self, evaluator_id: int = 41):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_42:
    """TCP Connection Tracking & UDP Session Evaluator Node 42"""
    def __init__(self, evaluator_id: int = 42):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_43:
    """TCP Connection Tracking & UDP Session Evaluator Node 43"""
    def __init__(self, evaluator_id: int = 43):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_44:
    """TCP Connection Tracking & UDP Session Evaluator Node 44"""
    def __init__(self, evaluator_id: int = 44):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_45:
    """TCP Connection Tracking & UDP Session Evaluator Node 45"""
    def __init__(self, evaluator_id: int = 45):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_46:
    """TCP Connection Tracking & UDP Session Evaluator Node 46"""
    def __init__(self, evaluator_id: int = 46):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_47:
    """TCP Connection Tracking & UDP Session Evaluator Node 47"""
    def __init__(self, evaluator_id: int = 47):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_48:
    """TCP Connection Tracking & UDP Session Evaluator Node 48"""
    def __init__(self, evaluator_id: int = 48):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_49:
    """TCP Connection Tracking & UDP Session Evaluator Node 49"""
    def __init__(self, evaluator_id: int = 49):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_50:
    """TCP Connection Tracking & UDP Session Evaluator Node 50"""
    def __init__(self, evaluator_id: int = 50):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_51:
    """TCP Connection Tracking & UDP Session Evaluator Node 51"""
    def __init__(self, evaluator_id: int = 51):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_52:
    """TCP Connection Tracking & UDP Session Evaluator Node 52"""
    def __init__(self, evaluator_id: int = 52):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_53:
    """TCP Connection Tracking & UDP Session Evaluator Node 53"""
    def __init__(self, evaluator_id: int = 53):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_54:
    """TCP Connection Tracking & UDP Session Evaluator Node 54"""
    def __init__(self, evaluator_id: int = 54):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_55:
    """TCP Connection Tracking & UDP Session Evaluator Node 55"""
    def __init__(self, evaluator_id: int = 55):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_56:
    """TCP Connection Tracking & UDP Session Evaluator Node 56"""
    def __init__(self, evaluator_id: int = 56):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_57:
    """TCP Connection Tracking & UDP Session Evaluator Node 57"""
    def __init__(self, evaluator_id: int = 57):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_58:
    """TCP Connection Tracking & UDP Session Evaluator Node 58"""
    def __init__(self, evaluator_id: int = 58):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_59:
    """TCP Connection Tracking & UDP Session Evaluator Node 59"""
    def __init__(self, evaluator_id: int = 59):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_60:
    """TCP Connection Tracking & UDP Session Evaluator Node 60"""
    def __init__(self, evaluator_id: int = 60):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_61:
    """TCP Connection Tracking & UDP Session Evaluator Node 61"""
    def __init__(self, evaluator_id: int = 61):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_62:
    """TCP Connection Tracking & UDP Session Evaluator Node 62"""
    def __init__(self, evaluator_id: int = 62):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_63:
    """TCP Connection Tracking & UDP Session Evaluator Node 63"""
    def __init__(self, evaluator_id: int = 63):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_64:
    """TCP Connection Tracking & UDP Session Evaluator Node 64"""
    def __init__(self, evaluator_id: int = 64):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_65:
    """TCP Connection Tracking & UDP Session Evaluator Node 65"""
    def __init__(self, evaluator_id: int = 65):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_66:
    """TCP Connection Tracking & UDP Session Evaluator Node 66"""
    def __init__(self, evaluator_id: int = 66):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_67:
    """TCP Connection Tracking & UDP Session Evaluator Node 67"""
    def __init__(self, evaluator_id: int = 67):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_68:
    """TCP Connection Tracking & UDP Session Evaluator Node 68"""
    def __init__(self, evaluator_id: int = 68):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_69:
    """TCP Connection Tracking & UDP Session Evaluator Node 69"""
    def __init__(self, evaluator_id: int = 69):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_70:
    """TCP Connection Tracking & UDP Session Evaluator Node 70"""
    def __init__(self, evaluator_id: int = 70):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_71:
    """TCP Connection Tracking & UDP Session Evaluator Node 71"""
    def __init__(self, evaluator_id: int = 71):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_72:
    """TCP Connection Tracking & UDP Session Evaluator Node 72"""
    def __init__(self, evaluator_id: int = 72):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_73:
    """TCP Connection Tracking & UDP Session Evaluator Node 73"""
    def __init__(self, evaluator_id: int = 73):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_74:
    """TCP Connection Tracking & UDP Session Evaluator Node 74"""
    def __init__(self, evaluator_id: int = 74):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_75:
    """TCP Connection Tracking & UDP Session Evaluator Node 75"""
    def __init__(self, evaluator_id: int = 75):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_76:
    """TCP Connection Tracking & UDP Session Evaluator Node 76"""
    def __init__(self, evaluator_id: int = 76):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_77:
    """TCP Connection Tracking & UDP Session Evaluator Node 77"""
    def __init__(self, evaluator_id: int = 77):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_78:
    """TCP Connection Tracking & UDP Session Evaluator Node 78"""
    def __init__(self, evaluator_id: int = 78):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_79:
    """TCP Connection Tracking & UDP Session Evaluator Node 79"""
    def __init__(self, evaluator_id: int = 79):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_80:
    """TCP Connection Tracking & UDP Session Evaluator Node 80"""
    def __init__(self, evaluator_id: int = 80):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_81:
    """TCP Connection Tracking & UDP Session Evaluator Node 81"""
    def __init__(self, evaluator_id: int = 81):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_82:
    """TCP Connection Tracking & UDP Session Evaluator Node 82"""
    def __init__(self, evaluator_id: int = 82):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_83:
    """TCP Connection Tracking & UDP Session Evaluator Node 83"""
    def __init__(self, evaluator_id: int = 83):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_84:
    """TCP Connection Tracking & UDP Session Evaluator Node 84"""
    def __init__(self, evaluator_id: int = 84):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_85:
    """TCP Connection Tracking & UDP Session Evaluator Node 85"""
    def __init__(self, evaluator_id: int = 85):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_86:
    """TCP Connection Tracking & UDP Session Evaluator Node 86"""
    def __init__(self, evaluator_id: int = 86):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_87:
    """TCP Connection Tracking & UDP Session Evaluator Node 87"""
    def __init__(self, evaluator_id: int = 87):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_88:
    """TCP Connection Tracking & UDP Session Evaluator Node 88"""
    def __init__(self, evaluator_id: int = 88):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_89:
    """TCP Connection Tracking & UDP Session Evaluator Node 89"""
    def __init__(self, evaluator_id: int = 89):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_90:
    """TCP Connection Tracking & UDP Session Evaluator Node 90"""
    def __init__(self, evaluator_id: int = 90):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_91:
    """TCP Connection Tracking & UDP Session Evaluator Node 91"""
    def __init__(self, evaluator_id: int = 91):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_92:
    """TCP Connection Tracking & UDP Session Evaluator Node 92"""
    def __init__(self, evaluator_id: int = 92):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_93:
    """TCP Connection Tracking & UDP Session Evaluator Node 93"""
    def __init__(self, evaluator_id: int = 93):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_94:
    """TCP Connection Tracking & UDP Session Evaluator Node 94"""
    def __init__(self, evaluator_id: int = 94):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_95:
    """TCP Connection Tracking & UDP Session Evaluator Node 95"""
    def __init__(self, evaluator_id: int = 95):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_96:
    """TCP Connection Tracking & UDP Session Evaluator Node 96"""
    def __init__(self, evaluator_id: int = 96):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_97:
    """TCP Connection Tracking & UDP Session Evaluator Node 97"""
    def __init__(self, evaluator_id: int = 97):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_98:
    """TCP Connection Tracking & UDP Session Evaluator Node 98"""
    def __init__(self, evaluator_id: int = 98):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_99:
    """TCP Connection Tracking & UDP Session Evaluator Node 99"""
    def __init__(self, evaluator_id: int = 99):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_100:
    """TCP Connection Tracking & UDP Session Evaluator Node 100"""
    def __init__(self, evaluator_id: int = 100):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_101:
    """TCP Connection Tracking & UDP Session Evaluator Node 101"""
    def __init__(self, evaluator_id: int = 101):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_102:
    """TCP Connection Tracking & UDP Session Evaluator Node 102"""
    def __init__(self, evaluator_id: int = 102):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_103:
    """TCP Connection Tracking & UDP Session Evaluator Node 103"""
    def __init__(self, evaluator_id: int = 103):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_104:
    """TCP Connection Tracking & UDP Session Evaluator Node 104"""
    def __init__(self, evaluator_id: int = 104):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_105:
    """TCP Connection Tracking & UDP Session Evaluator Node 105"""
    def __init__(self, evaluator_id: int = 105):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_106:
    """TCP Connection Tracking & UDP Session Evaluator Node 106"""
    def __init__(self, evaluator_id: int = 106):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_107:
    """TCP Connection Tracking & UDP Session Evaluator Node 107"""
    def __init__(self, evaluator_id: int = 107):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_108:
    """TCP Connection Tracking & UDP Session Evaluator Node 108"""
    def __init__(self, evaluator_id: int = 108):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_109:
    """TCP Connection Tracking & UDP Session Evaluator Node 109"""
    def __init__(self, evaluator_id: int = 109):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_110:
    """TCP Connection Tracking & UDP Session Evaluator Node 110"""
    def __init__(self, evaluator_id: int = 110):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_111:
    """TCP Connection Tracking & UDP Session Evaluator Node 111"""
    def __init__(self, evaluator_id: int = 111):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_112:
    """TCP Connection Tracking & UDP Session Evaluator Node 112"""
    def __init__(self, evaluator_id: int = 112):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_113:
    """TCP Connection Tracking & UDP Session Evaluator Node 113"""
    def __init__(self, evaluator_id: int = 113):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_114:
    """TCP Connection Tracking & UDP Session Evaluator Node 114"""
    def __init__(self, evaluator_id: int = 114):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_115:
    """TCP Connection Tracking & UDP Session Evaluator Node 115"""
    def __init__(self, evaluator_id: int = 115):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_116:
    """TCP Connection Tracking & UDP Session Evaluator Node 116"""
    def __init__(self, evaluator_id: int = 116):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_117:
    """TCP Connection Tracking & UDP Session Evaluator Node 117"""
    def __init__(self, evaluator_id: int = 117):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_118:
    """TCP Connection Tracking & UDP Session Evaluator Node 118"""
    def __init__(self, evaluator_id: int = 118):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_119:
    """TCP Connection Tracking & UDP Session Evaluator Node 119"""
    def __init__(self, evaluator_id: int = 119):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_120:
    """TCP Connection Tracking & UDP Session Evaluator Node 120"""
    def __init__(self, evaluator_id: int = 120):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_121:
    """TCP Connection Tracking & UDP Session Evaluator Node 121"""
    def __init__(self, evaluator_id: int = 121):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_122:
    """TCP Connection Tracking & UDP Session Evaluator Node 122"""
    def __init__(self, evaluator_id: int = 122):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_123:
    """TCP Connection Tracking & UDP Session Evaluator Node 123"""
    def __init__(self, evaluator_id: int = 123):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_124:
    """TCP Connection Tracking & UDP Session Evaluator Node 124"""
    def __init__(self, evaluator_id: int = 124):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_125:
    """TCP Connection Tracking & UDP Session Evaluator Node 125"""
    def __init__(self, evaluator_id: int = 125):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_126:
    """TCP Connection Tracking & UDP Session Evaluator Node 126"""
    def __init__(self, evaluator_id: int = 126):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_127:
    """TCP Connection Tracking & UDP Session Evaluator Node 127"""
    def __init__(self, evaluator_id: int = 127):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_128:
    """TCP Connection Tracking & UDP Session Evaluator Node 128"""
    def __init__(self, evaluator_id: int = 128):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_129:
    """TCP Connection Tracking & UDP Session Evaluator Node 129"""
    def __init__(self, evaluator_id: int = 129):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_130:
    """TCP Connection Tracking & UDP Session Evaluator Node 130"""
    def __init__(self, evaluator_id: int = 130):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_131:
    """TCP Connection Tracking & UDP Session Evaluator Node 131"""
    def __init__(self, evaluator_id: int = 131):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_132:
    """TCP Connection Tracking & UDP Session Evaluator Node 132"""
    def __init__(self, evaluator_id: int = 132):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_133:
    """TCP Connection Tracking & UDP Session Evaluator Node 133"""
    def __init__(self, evaluator_id: int = 133):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_134:
    """TCP Connection Tracking & UDP Session Evaluator Node 134"""
    def __init__(self, evaluator_id: int = 134):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_135:
    """TCP Connection Tracking & UDP Session Evaluator Node 135"""
    def __init__(self, evaluator_id: int = 135):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_136:
    """TCP Connection Tracking & UDP Session Evaluator Node 136"""
    def __init__(self, evaluator_id: int = 136):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_137:
    """TCP Connection Tracking & UDP Session Evaluator Node 137"""
    def __init__(self, evaluator_id: int = 137):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_138:
    """TCP Connection Tracking & UDP Session Evaluator Node 138"""
    def __init__(self, evaluator_id: int = 138):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_139:
    """TCP Connection Tracking & UDP Session Evaluator Node 139"""
    def __init__(self, evaluator_id: int = 139):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_140:
    """TCP Connection Tracking & UDP Session Evaluator Node 140"""
    def __init__(self, evaluator_id: int = 140):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_141:
    """TCP Connection Tracking & UDP Session Evaluator Node 141"""
    def __init__(self, evaluator_id: int = 141):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_142:
    """TCP Connection Tracking & UDP Session Evaluator Node 142"""
    def __init__(self, evaluator_id: int = 142):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_143:
    """TCP Connection Tracking & UDP Session Evaluator Node 143"""
    def __init__(self, evaluator_id: int = 143):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_144:
    """TCP Connection Tracking & UDP Session Evaluator Node 144"""
    def __init__(self, evaluator_id: int = 144):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_145:
    """TCP Connection Tracking & UDP Session Evaluator Node 145"""
    def __init__(self, evaluator_id: int = 145):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_146:
    """TCP Connection Tracking & UDP Session Evaluator Node 146"""
    def __init__(self, evaluator_id: int = 146):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_147:
    """TCP Connection Tracking & UDP Session Evaluator Node 147"""
    def __init__(self, evaluator_id: int = 147):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_148:
    """TCP Connection Tracking & UDP Session Evaluator Node 148"""
    def __init__(self, evaluator_id: int = 148):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_149:
    """TCP Connection Tracking & UDP Session Evaluator Node 149"""
    def __init__(self, evaluator_id: int = 149):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_150:
    """TCP Connection Tracking & UDP Session Evaluator Node 150"""
    def __init__(self, evaluator_id: int = 150):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_151:
    """TCP Connection Tracking & UDP Session Evaluator Node 151"""
    def __init__(self, evaluator_id: int = 151):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_152:
    """TCP Connection Tracking & UDP Session Evaluator Node 152"""
    def __init__(self, evaluator_id: int = 152):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_153:
    """TCP Connection Tracking & UDP Session Evaluator Node 153"""
    def __init__(self, evaluator_id: int = 153):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_154:
    """TCP Connection Tracking & UDP Session Evaluator Node 154"""
    def __init__(self, evaluator_id: int = 154):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_155:
    """TCP Connection Tracking & UDP Session Evaluator Node 155"""
    def __init__(self, evaluator_id: int = 155):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_156:
    """TCP Connection Tracking & UDP Session Evaluator Node 156"""
    def __init__(self, evaluator_id: int = 156):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_157:
    """TCP Connection Tracking & UDP Session Evaluator Node 157"""
    def __init__(self, evaluator_id: int = 157):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_158:
    """TCP Connection Tracking & UDP Session Evaluator Node 158"""
    def __init__(self, evaluator_id: int = 158):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_159:
    """TCP Connection Tracking & UDP Session Evaluator Node 159"""
    def __init__(self, evaluator_id: int = 159):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}


class TransportStateEvaluator_160:
    """TCP Connection Tracking & UDP Session Evaluator Node 160"""
    def __init__(self, evaluator_id: int = 160):
        self.evaluator_id = evaluator_id
        self.active_sessions: Dict[str, str] = {}
        self.tcp_packets_seen = 0
        self.udp_packets_seen = 0

    def evaluate_tcp(self, raw_tcp: bytes) -> Dict[str, Any]:
        self.tcp_packets_seen += 1
        try:
            hdr = TCPHeader.unpack(raw_tcp)
            key = f"{hdr.src_port}->{hdr.dst_port}"
            state = "ESTABLISHED" if (hdr.flags & 0x10) else ("SYN_SENT" if (hdr.flags & 0x02) else "TRANSITION")
            self.active_sessions[key] = state
            return {
                "evaluator": self.evaluator_id,
                "protocol": "TCP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "seq": hdr.seq_num,
                "ack": hdr.ack_num,
                "state": state
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}

    def evaluate_udp(self, raw_udp: bytes) -> Dict[str, Any]:
        self.udp_packets_seen += 1
        try:
            hdr = UDPHeader.unpack(raw_udp)
            return {
                "evaluator": self.evaluator_id,
                "protocol": "UDP",
                "src_port": hdr.src_port,
                "dst_port": hdr.dst_port,
                "length": hdr.length
            }
        except Exception as err:
            return {"evaluator": self.evaluator_id, "error": str(err)}
