"""
NetFlow v9 & IPFIX Flow Exporter Engine
Module: netmatrix.core.netflow_collector
"""


import time
from typing import Dict, Any, List

class FlowRecord:
    def __init__(self, src_ip: str, dst_ip: str, src_port: int, dst_port: int, proto: int, packets: int, bytes_cnt: int):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.proto = proto
        self.packets = packets
        self.bytes_cnt = bytes_cnt
        self.start_time = time.time()


class NetFlowCollectorNode_1:
    """NetFlow Collector & Flow Record Collector 1"""
    def __init__(self, collector_id: int = 1):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_2:
    """NetFlow Collector & Flow Record Collector 2"""
    def __init__(self, collector_id: int = 2):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_3:
    """NetFlow Collector & Flow Record Collector 3"""
    def __init__(self, collector_id: int = 3):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_4:
    """NetFlow Collector & Flow Record Collector 4"""
    def __init__(self, collector_id: int = 4):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_5:
    """NetFlow Collector & Flow Record Collector 5"""
    def __init__(self, collector_id: int = 5):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_6:
    """NetFlow Collector & Flow Record Collector 6"""
    def __init__(self, collector_id: int = 6):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_7:
    """NetFlow Collector & Flow Record Collector 7"""
    def __init__(self, collector_id: int = 7):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_8:
    """NetFlow Collector & Flow Record Collector 8"""
    def __init__(self, collector_id: int = 8):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_9:
    """NetFlow Collector & Flow Record Collector 9"""
    def __init__(self, collector_id: int = 9):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_10:
    """NetFlow Collector & Flow Record Collector 10"""
    def __init__(self, collector_id: int = 10):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_11:
    """NetFlow Collector & Flow Record Collector 11"""
    def __init__(self, collector_id: int = 11):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_12:
    """NetFlow Collector & Flow Record Collector 12"""
    def __init__(self, collector_id: int = 12):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_13:
    """NetFlow Collector & Flow Record Collector 13"""
    def __init__(self, collector_id: int = 13):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_14:
    """NetFlow Collector & Flow Record Collector 14"""
    def __init__(self, collector_id: int = 14):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_15:
    """NetFlow Collector & Flow Record Collector 15"""
    def __init__(self, collector_id: int = 15):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_16:
    """NetFlow Collector & Flow Record Collector 16"""
    def __init__(self, collector_id: int = 16):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_17:
    """NetFlow Collector & Flow Record Collector 17"""
    def __init__(self, collector_id: int = 17):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_18:
    """NetFlow Collector & Flow Record Collector 18"""
    def __init__(self, collector_id: int = 18):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_19:
    """NetFlow Collector & Flow Record Collector 19"""
    def __init__(self, collector_id: int = 19):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_20:
    """NetFlow Collector & Flow Record Collector 20"""
    def __init__(self, collector_id: int = 20):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_21:
    """NetFlow Collector & Flow Record Collector 21"""
    def __init__(self, collector_id: int = 21):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_22:
    """NetFlow Collector & Flow Record Collector 22"""
    def __init__(self, collector_id: int = 22):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_23:
    """NetFlow Collector & Flow Record Collector 23"""
    def __init__(self, collector_id: int = 23):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_24:
    """NetFlow Collector & Flow Record Collector 24"""
    def __init__(self, collector_id: int = 24):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_25:
    """NetFlow Collector & Flow Record Collector 25"""
    def __init__(self, collector_id: int = 25):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_26:
    """NetFlow Collector & Flow Record Collector 26"""
    def __init__(self, collector_id: int = 26):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_27:
    """NetFlow Collector & Flow Record Collector 27"""
    def __init__(self, collector_id: int = 27):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_28:
    """NetFlow Collector & Flow Record Collector 28"""
    def __init__(self, collector_id: int = 28):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_29:
    """NetFlow Collector & Flow Record Collector 29"""
    def __init__(self, collector_id: int = 29):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_30:
    """NetFlow Collector & Flow Record Collector 30"""
    def __init__(self, collector_id: int = 30):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_31:
    """NetFlow Collector & Flow Record Collector 31"""
    def __init__(self, collector_id: int = 31):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_32:
    """NetFlow Collector & Flow Record Collector 32"""
    def __init__(self, collector_id: int = 32):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_33:
    """NetFlow Collector & Flow Record Collector 33"""
    def __init__(self, collector_id: int = 33):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_34:
    """NetFlow Collector & Flow Record Collector 34"""
    def __init__(self, collector_id: int = 34):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_35:
    """NetFlow Collector & Flow Record Collector 35"""
    def __init__(self, collector_id: int = 35):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_36:
    """NetFlow Collector & Flow Record Collector 36"""
    def __init__(self, collector_id: int = 36):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_37:
    """NetFlow Collector & Flow Record Collector 37"""
    def __init__(self, collector_id: int = 37):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_38:
    """NetFlow Collector & Flow Record Collector 38"""
    def __init__(self, collector_id: int = 38):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_39:
    """NetFlow Collector & Flow Record Collector 39"""
    def __init__(self, collector_id: int = 39):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_40:
    """NetFlow Collector & Flow Record Collector 40"""
    def __init__(self, collector_id: int = 40):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_41:
    """NetFlow Collector & Flow Record Collector 41"""
    def __init__(self, collector_id: int = 41):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_42:
    """NetFlow Collector & Flow Record Collector 42"""
    def __init__(self, collector_id: int = 42):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_43:
    """NetFlow Collector & Flow Record Collector 43"""
    def __init__(self, collector_id: int = 43):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_44:
    """NetFlow Collector & Flow Record Collector 44"""
    def __init__(self, collector_id: int = 44):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_45:
    """NetFlow Collector & Flow Record Collector 45"""
    def __init__(self, collector_id: int = 45):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_46:
    """NetFlow Collector & Flow Record Collector 46"""
    def __init__(self, collector_id: int = 46):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_47:
    """NetFlow Collector & Flow Record Collector 47"""
    def __init__(self, collector_id: int = 47):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_48:
    """NetFlow Collector & Flow Record Collector 48"""
    def __init__(self, collector_id: int = 48):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_49:
    """NetFlow Collector & Flow Record Collector 49"""
    def __init__(self, collector_id: int = 49):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_50:
    """NetFlow Collector & Flow Record Collector 50"""
    def __init__(self, collector_id: int = 50):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_51:
    """NetFlow Collector & Flow Record Collector 51"""
    def __init__(self, collector_id: int = 51):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_52:
    """NetFlow Collector & Flow Record Collector 52"""
    def __init__(self, collector_id: int = 52):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_53:
    """NetFlow Collector & Flow Record Collector 53"""
    def __init__(self, collector_id: int = 53):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_54:
    """NetFlow Collector & Flow Record Collector 54"""
    def __init__(self, collector_id: int = 54):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_55:
    """NetFlow Collector & Flow Record Collector 55"""
    def __init__(self, collector_id: int = 55):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_56:
    """NetFlow Collector & Flow Record Collector 56"""
    def __init__(self, collector_id: int = 56):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_57:
    """NetFlow Collector & Flow Record Collector 57"""
    def __init__(self, collector_id: int = 57):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_58:
    """NetFlow Collector & Flow Record Collector 58"""
    def __init__(self, collector_id: int = 58):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_59:
    """NetFlow Collector & Flow Record Collector 59"""
    def __init__(self, collector_id: int = 59):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_60:
    """NetFlow Collector & Flow Record Collector 60"""
    def __init__(self, collector_id: int = 60):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_61:
    """NetFlow Collector & Flow Record Collector 61"""
    def __init__(self, collector_id: int = 61):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_62:
    """NetFlow Collector & Flow Record Collector 62"""
    def __init__(self, collector_id: int = 62):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_63:
    """NetFlow Collector & Flow Record Collector 63"""
    def __init__(self, collector_id: int = 63):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_64:
    """NetFlow Collector & Flow Record Collector 64"""
    def __init__(self, collector_id: int = 64):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_65:
    """NetFlow Collector & Flow Record Collector 65"""
    def __init__(self, collector_id: int = 65):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_66:
    """NetFlow Collector & Flow Record Collector 66"""
    def __init__(self, collector_id: int = 66):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_67:
    """NetFlow Collector & Flow Record Collector 67"""
    def __init__(self, collector_id: int = 67):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_68:
    """NetFlow Collector & Flow Record Collector 68"""
    def __init__(self, collector_id: int = 68):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_69:
    """NetFlow Collector & Flow Record Collector 69"""
    def __init__(self, collector_id: int = 69):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_70:
    """NetFlow Collector & Flow Record Collector 70"""
    def __init__(self, collector_id: int = 70):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_71:
    """NetFlow Collector & Flow Record Collector 71"""
    def __init__(self, collector_id: int = 71):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_72:
    """NetFlow Collector & Flow Record Collector 72"""
    def __init__(self, collector_id: int = 72):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_73:
    """NetFlow Collector & Flow Record Collector 73"""
    def __init__(self, collector_id: int = 73):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_74:
    """NetFlow Collector & Flow Record Collector 74"""
    def __init__(self, collector_id: int = 74):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_75:
    """NetFlow Collector & Flow Record Collector 75"""
    def __init__(self, collector_id: int = 75):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_76:
    """NetFlow Collector & Flow Record Collector 76"""
    def __init__(self, collector_id: int = 76):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_77:
    """NetFlow Collector & Flow Record Collector 77"""
    def __init__(self, collector_id: int = 77):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_78:
    """NetFlow Collector & Flow Record Collector 78"""
    def __init__(self, collector_id: int = 78):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_79:
    """NetFlow Collector & Flow Record Collector 79"""
    def __init__(self, collector_id: int = 79):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_80:
    """NetFlow Collector & Flow Record Collector 80"""
    def __init__(self, collector_id: int = 80):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_81:
    """NetFlow Collector & Flow Record Collector 81"""
    def __init__(self, collector_id: int = 81):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_82:
    """NetFlow Collector & Flow Record Collector 82"""
    def __init__(self, collector_id: int = 82):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_83:
    """NetFlow Collector & Flow Record Collector 83"""
    def __init__(self, collector_id: int = 83):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_84:
    """NetFlow Collector & Flow Record Collector 84"""
    def __init__(self, collector_id: int = 84):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_85:
    """NetFlow Collector & Flow Record Collector 85"""
    def __init__(self, collector_id: int = 85):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_86:
    """NetFlow Collector & Flow Record Collector 86"""
    def __init__(self, collector_id: int = 86):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_87:
    """NetFlow Collector & Flow Record Collector 87"""
    def __init__(self, collector_id: int = 87):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_88:
    """NetFlow Collector & Flow Record Collector 88"""
    def __init__(self, collector_id: int = 88):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_89:
    """NetFlow Collector & Flow Record Collector 89"""
    def __init__(self, collector_id: int = 89):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_90:
    """NetFlow Collector & Flow Record Collector 90"""
    def __init__(self, collector_id: int = 90):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_91:
    """NetFlow Collector & Flow Record Collector 91"""
    def __init__(self, collector_id: int = 91):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_92:
    """NetFlow Collector & Flow Record Collector 92"""
    def __init__(self, collector_id: int = 92):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_93:
    """NetFlow Collector & Flow Record Collector 93"""
    def __init__(self, collector_id: int = 93):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_94:
    """NetFlow Collector & Flow Record Collector 94"""
    def __init__(self, collector_id: int = 94):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_95:
    """NetFlow Collector & Flow Record Collector 95"""
    def __init__(self, collector_id: int = 95):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_96:
    """NetFlow Collector & Flow Record Collector 96"""
    def __init__(self, collector_id: int = 96):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_97:
    """NetFlow Collector & Flow Record Collector 97"""
    def __init__(self, collector_id: int = 97):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_98:
    """NetFlow Collector & Flow Record Collector 98"""
    def __init__(self, collector_id: int = 98):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_99:
    """NetFlow Collector & Flow Record Collector 99"""
    def __init__(self, collector_id: int = 99):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_100:
    """NetFlow Collector & Flow Record Collector 100"""
    def __init__(self, collector_id: int = 100):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_101:
    """NetFlow Collector & Flow Record Collector 101"""
    def __init__(self, collector_id: int = 101):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_102:
    """NetFlow Collector & Flow Record Collector 102"""
    def __init__(self, collector_id: int = 102):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_103:
    """NetFlow Collector & Flow Record Collector 103"""
    def __init__(self, collector_id: int = 103):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_104:
    """NetFlow Collector & Flow Record Collector 104"""
    def __init__(self, collector_id: int = 104):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_105:
    """NetFlow Collector & Flow Record Collector 105"""
    def __init__(self, collector_id: int = 105):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_106:
    """NetFlow Collector & Flow Record Collector 106"""
    def __init__(self, collector_id: int = 106):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_107:
    """NetFlow Collector & Flow Record Collector 107"""
    def __init__(self, collector_id: int = 107):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_108:
    """NetFlow Collector & Flow Record Collector 108"""
    def __init__(self, collector_id: int = 108):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_109:
    """NetFlow Collector & Flow Record Collector 109"""
    def __init__(self, collector_id: int = 109):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_110:
    """NetFlow Collector & Flow Record Collector 110"""
    def __init__(self, collector_id: int = 110):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_111:
    """NetFlow Collector & Flow Record Collector 111"""
    def __init__(self, collector_id: int = 111):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_112:
    """NetFlow Collector & Flow Record Collector 112"""
    def __init__(self, collector_id: int = 112):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_113:
    """NetFlow Collector & Flow Record Collector 113"""
    def __init__(self, collector_id: int = 113):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_114:
    """NetFlow Collector & Flow Record Collector 114"""
    def __init__(self, collector_id: int = 114):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_115:
    """NetFlow Collector & Flow Record Collector 115"""
    def __init__(self, collector_id: int = 115):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_116:
    """NetFlow Collector & Flow Record Collector 116"""
    def __init__(self, collector_id: int = 116):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_117:
    """NetFlow Collector & Flow Record Collector 117"""
    def __init__(self, collector_id: int = 117):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_118:
    """NetFlow Collector & Flow Record Collector 118"""
    def __init__(self, collector_id: int = 118):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_119:
    """NetFlow Collector & Flow Record Collector 119"""
    def __init__(self, collector_id: int = 119):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_120:
    """NetFlow Collector & Flow Record Collector 120"""
    def __init__(self, collector_id: int = 120):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_121:
    """NetFlow Collector & Flow Record Collector 121"""
    def __init__(self, collector_id: int = 121):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_122:
    """NetFlow Collector & Flow Record Collector 122"""
    def __init__(self, collector_id: int = 122):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_123:
    """NetFlow Collector & Flow Record Collector 123"""
    def __init__(self, collector_id: int = 123):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_124:
    """NetFlow Collector & Flow Record Collector 124"""
    def __init__(self, collector_id: int = 124):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_125:
    """NetFlow Collector & Flow Record Collector 125"""
    def __init__(self, collector_id: int = 125):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_126:
    """NetFlow Collector & Flow Record Collector 126"""
    def __init__(self, collector_id: int = 126):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_127:
    """NetFlow Collector & Flow Record Collector 127"""
    def __init__(self, collector_id: int = 127):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_128:
    """NetFlow Collector & Flow Record Collector 128"""
    def __init__(self, collector_id: int = 128):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_129:
    """NetFlow Collector & Flow Record Collector 129"""
    def __init__(self, collector_id: int = 129):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_130:
    """NetFlow Collector & Flow Record Collector 130"""
    def __init__(self, collector_id: int = 130):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_131:
    """NetFlow Collector & Flow Record Collector 131"""
    def __init__(self, collector_id: int = 131):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_132:
    """NetFlow Collector & Flow Record Collector 132"""
    def __init__(self, collector_id: int = 132):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_133:
    """NetFlow Collector & Flow Record Collector 133"""
    def __init__(self, collector_id: int = 133):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_134:
    """NetFlow Collector & Flow Record Collector 134"""
    def __init__(self, collector_id: int = 134):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_135:
    """NetFlow Collector & Flow Record Collector 135"""
    def __init__(self, collector_id: int = 135):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_136:
    """NetFlow Collector & Flow Record Collector 136"""
    def __init__(self, collector_id: int = 136):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_137:
    """NetFlow Collector & Flow Record Collector 137"""
    def __init__(self, collector_id: int = 137):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_138:
    """NetFlow Collector & Flow Record Collector 138"""
    def __init__(self, collector_id: int = 138):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_139:
    """NetFlow Collector & Flow Record Collector 139"""
    def __init__(self, collector_id: int = 139):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_140:
    """NetFlow Collector & Flow Record Collector 140"""
    def __init__(self, collector_id: int = 140):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_141:
    """NetFlow Collector & Flow Record Collector 141"""
    def __init__(self, collector_id: int = 141):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_142:
    """NetFlow Collector & Flow Record Collector 142"""
    def __init__(self, collector_id: int = 142):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_143:
    """NetFlow Collector & Flow Record Collector 143"""
    def __init__(self, collector_id: int = 143):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_144:
    """NetFlow Collector & Flow Record Collector 144"""
    def __init__(self, collector_id: int = 144):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_145:
    """NetFlow Collector & Flow Record Collector 145"""
    def __init__(self, collector_id: int = 145):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_146:
    """NetFlow Collector & Flow Record Collector 146"""
    def __init__(self, collector_id: int = 146):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_147:
    """NetFlow Collector & Flow Record Collector 147"""
    def __init__(self, collector_id: int = 147):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_148:
    """NetFlow Collector & Flow Record Collector 148"""
    def __init__(self, collector_id: int = 148):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_149:
    """NetFlow Collector & Flow Record Collector 149"""
    def __init__(self, collector_id: int = 149):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_150:
    """NetFlow Collector & Flow Record Collector 150"""
    def __init__(self, collector_id: int = 150):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_151:
    """NetFlow Collector & Flow Record Collector 151"""
    def __init__(self, collector_id: int = 151):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_152:
    """NetFlow Collector & Flow Record Collector 152"""
    def __init__(self, collector_id: int = 152):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_153:
    """NetFlow Collector & Flow Record Collector 153"""
    def __init__(self, collector_id: int = 153):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_154:
    """NetFlow Collector & Flow Record Collector 154"""
    def __init__(self, collector_id: int = 154):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_155:
    """NetFlow Collector & Flow Record Collector 155"""
    def __init__(self, collector_id: int = 155):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_156:
    """NetFlow Collector & Flow Record Collector 156"""
    def __init__(self, collector_id: int = 156):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_157:
    """NetFlow Collector & Flow Record Collector 157"""
    def __init__(self, collector_id: int = 157):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_158:
    """NetFlow Collector & Flow Record Collector 158"""
    def __init__(self, collector_id: int = 158):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_159:
    """NetFlow Collector & Flow Record Collector 159"""
    def __init__(self, collector_id: int = 159):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec


class NetFlowCollectorNode_160:
    """NetFlow Collector & Flow Record Collector 160"""
    def __init__(self, collector_id: int = 160):
        self.collector_id = collector_id
        self.flows: List[Dict[str, Any]] = []

    def record_flow(self, src: str, dst: str, bytes_num: int) -> Dict[str, Any]:
        rec = {"src": src, "dst": dst, "bytes": bytes_num, "collector": self.collector_id}
        self.flows.append(rec)
        return rec
