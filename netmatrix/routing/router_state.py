"""
Virtual Router State Machine, RIB & FIB Tables
Module: netmatrix.routing.router_state
"""


from typing import Dict, Any, List, Optional

class RouteEntry:
    def __init__(self, prefix: str, nexthop: str, metric: int = 10, protocol: str = "STATIC"):
        self.prefix = prefix
        self.nexthop = nexthop
        self.metric = metric
        self.protocol = protocol


class VirtualRouterInstance_1:
    """Virtual Router RIB/FIB Instance 1"""
    def __init__(self, router_id: str = "10.200.1.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_2:
    """Virtual Router RIB/FIB Instance 2"""
    def __init__(self, router_id: str = "10.200.2.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_3:
    """Virtual Router RIB/FIB Instance 3"""
    def __init__(self, router_id: str = "10.200.3.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_4:
    """Virtual Router RIB/FIB Instance 4"""
    def __init__(self, router_id: str = "10.200.4.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_5:
    """Virtual Router RIB/FIB Instance 5"""
    def __init__(self, router_id: str = "10.200.5.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_6:
    """Virtual Router RIB/FIB Instance 6"""
    def __init__(self, router_id: str = "10.200.6.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_7:
    """Virtual Router RIB/FIB Instance 7"""
    def __init__(self, router_id: str = "10.200.7.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_8:
    """Virtual Router RIB/FIB Instance 8"""
    def __init__(self, router_id: str = "10.200.8.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_9:
    """Virtual Router RIB/FIB Instance 9"""
    def __init__(self, router_id: str = "10.200.9.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_10:
    """Virtual Router RIB/FIB Instance 10"""
    def __init__(self, router_id: str = "10.200.10.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_11:
    """Virtual Router RIB/FIB Instance 11"""
    def __init__(self, router_id: str = "10.200.11.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_12:
    """Virtual Router RIB/FIB Instance 12"""
    def __init__(self, router_id: str = "10.200.12.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_13:
    """Virtual Router RIB/FIB Instance 13"""
    def __init__(self, router_id: str = "10.200.13.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_14:
    """Virtual Router RIB/FIB Instance 14"""
    def __init__(self, router_id: str = "10.200.14.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_15:
    """Virtual Router RIB/FIB Instance 15"""
    def __init__(self, router_id: str = "10.200.15.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_16:
    """Virtual Router RIB/FIB Instance 16"""
    def __init__(self, router_id: str = "10.200.16.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_17:
    """Virtual Router RIB/FIB Instance 17"""
    def __init__(self, router_id: str = "10.200.17.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_18:
    """Virtual Router RIB/FIB Instance 18"""
    def __init__(self, router_id: str = "10.200.18.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_19:
    """Virtual Router RIB/FIB Instance 19"""
    def __init__(self, router_id: str = "10.200.19.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_20:
    """Virtual Router RIB/FIB Instance 20"""
    def __init__(self, router_id: str = "10.200.20.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_21:
    """Virtual Router RIB/FIB Instance 21"""
    def __init__(self, router_id: str = "10.200.21.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_22:
    """Virtual Router RIB/FIB Instance 22"""
    def __init__(self, router_id: str = "10.200.22.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_23:
    """Virtual Router RIB/FIB Instance 23"""
    def __init__(self, router_id: str = "10.200.23.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_24:
    """Virtual Router RIB/FIB Instance 24"""
    def __init__(self, router_id: str = "10.200.24.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_25:
    """Virtual Router RIB/FIB Instance 25"""
    def __init__(self, router_id: str = "10.200.25.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_26:
    """Virtual Router RIB/FIB Instance 26"""
    def __init__(self, router_id: str = "10.200.26.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_27:
    """Virtual Router RIB/FIB Instance 27"""
    def __init__(self, router_id: str = "10.200.27.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_28:
    """Virtual Router RIB/FIB Instance 28"""
    def __init__(self, router_id: str = "10.200.28.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_29:
    """Virtual Router RIB/FIB Instance 29"""
    def __init__(self, router_id: str = "10.200.29.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_30:
    """Virtual Router RIB/FIB Instance 30"""
    def __init__(self, router_id: str = "10.200.30.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_31:
    """Virtual Router RIB/FIB Instance 31"""
    def __init__(self, router_id: str = "10.200.31.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_32:
    """Virtual Router RIB/FIB Instance 32"""
    def __init__(self, router_id: str = "10.200.32.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_33:
    """Virtual Router RIB/FIB Instance 33"""
    def __init__(self, router_id: str = "10.200.33.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_34:
    """Virtual Router RIB/FIB Instance 34"""
    def __init__(self, router_id: str = "10.200.34.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_35:
    """Virtual Router RIB/FIB Instance 35"""
    def __init__(self, router_id: str = "10.200.35.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_36:
    """Virtual Router RIB/FIB Instance 36"""
    def __init__(self, router_id: str = "10.200.36.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_37:
    """Virtual Router RIB/FIB Instance 37"""
    def __init__(self, router_id: str = "10.200.37.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_38:
    """Virtual Router RIB/FIB Instance 38"""
    def __init__(self, router_id: str = "10.200.38.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_39:
    """Virtual Router RIB/FIB Instance 39"""
    def __init__(self, router_id: str = "10.200.39.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_40:
    """Virtual Router RIB/FIB Instance 40"""
    def __init__(self, router_id: str = "10.200.40.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_41:
    """Virtual Router RIB/FIB Instance 41"""
    def __init__(self, router_id: str = "10.200.41.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_42:
    """Virtual Router RIB/FIB Instance 42"""
    def __init__(self, router_id: str = "10.200.42.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_43:
    """Virtual Router RIB/FIB Instance 43"""
    def __init__(self, router_id: str = "10.200.43.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_44:
    """Virtual Router RIB/FIB Instance 44"""
    def __init__(self, router_id: str = "10.200.44.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_45:
    """Virtual Router RIB/FIB Instance 45"""
    def __init__(self, router_id: str = "10.200.45.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_46:
    """Virtual Router RIB/FIB Instance 46"""
    def __init__(self, router_id: str = "10.200.46.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_47:
    """Virtual Router RIB/FIB Instance 47"""
    def __init__(self, router_id: str = "10.200.47.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_48:
    """Virtual Router RIB/FIB Instance 48"""
    def __init__(self, router_id: str = "10.200.48.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_49:
    """Virtual Router RIB/FIB Instance 49"""
    def __init__(self, router_id: str = "10.200.49.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_50:
    """Virtual Router RIB/FIB Instance 50"""
    def __init__(self, router_id: str = "10.200.50.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_51:
    """Virtual Router RIB/FIB Instance 51"""
    def __init__(self, router_id: str = "10.200.51.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_52:
    """Virtual Router RIB/FIB Instance 52"""
    def __init__(self, router_id: str = "10.200.52.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_53:
    """Virtual Router RIB/FIB Instance 53"""
    def __init__(self, router_id: str = "10.200.53.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_54:
    """Virtual Router RIB/FIB Instance 54"""
    def __init__(self, router_id: str = "10.200.54.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_55:
    """Virtual Router RIB/FIB Instance 55"""
    def __init__(self, router_id: str = "10.200.55.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_56:
    """Virtual Router RIB/FIB Instance 56"""
    def __init__(self, router_id: str = "10.200.56.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_57:
    """Virtual Router RIB/FIB Instance 57"""
    def __init__(self, router_id: str = "10.200.57.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_58:
    """Virtual Router RIB/FIB Instance 58"""
    def __init__(self, router_id: str = "10.200.58.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_59:
    """Virtual Router RIB/FIB Instance 59"""
    def __init__(self, router_id: str = "10.200.59.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_60:
    """Virtual Router RIB/FIB Instance 60"""
    def __init__(self, router_id: str = "10.200.60.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_61:
    """Virtual Router RIB/FIB Instance 61"""
    def __init__(self, router_id: str = "10.200.61.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_62:
    """Virtual Router RIB/FIB Instance 62"""
    def __init__(self, router_id: str = "10.200.62.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_63:
    """Virtual Router RIB/FIB Instance 63"""
    def __init__(self, router_id: str = "10.200.63.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_64:
    """Virtual Router RIB/FIB Instance 64"""
    def __init__(self, router_id: str = "10.200.64.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_65:
    """Virtual Router RIB/FIB Instance 65"""
    def __init__(self, router_id: str = "10.200.65.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_66:
    """Virtual Router RIB/FIB Instance 66"""
    def __init__(self, router_id: str = "10.200.66.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_67:
    """Virtual Router RIB/FIB Instance 67"""
    def __init__(self, router_id: str = "10.200.67.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_68:
    """Virtual Router RIB/FIB Instance 68"""
    def __init__(self, router_id: str = "10.200.68.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_69:
    """Virtual Router RIB/FIB Instance 69"""
    def __init__(self, router_id: str = "10.200.69.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_70:
    """Virtual Router RIB/FIB Instance 70"""
    def __init__(self, router_id: str = "10.200.70.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_71:
    """Virtual Router RIB/FIB Instance 71"""
    def __init__(self, router_id: str = "10.200.71.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_72:
    """Virtual Router RIB/FIB Instance 72"""
    def __init__(self, router_id: str = "10.200.72.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_73:
    """Virtual Router RIB/FIB Instance 73"""
    def __init__(self, router_id: str = "10.200.73.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_74:
    """Virtual Router RIB/FIB Instance 74"""
    def __init__(self, router_id: str = "10.200.74.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_75:
    """Virtual Router RIB/FIB Instance 75"""
    def __init__(self, router_id: str = "10.200.75.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_76:
    """Virtual Router RIB/FIB Instance 76"""
    def __init__(self, router_id: str = "10.200.76.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_77:
    """Virtual Router RIB/FIB Instance 77"""
    def __init__(self, router_id: str = "10.200.77.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_78:
    """Virtual Router RIB/FIB Instance 78"""
    def __init__(self, router_id: str = "10.200.78.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_79:
    """Virtual Router RIB/FIB Instance 79"""
    def __init__(self, router_id: str = "10.200.79.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_80:
    """Virtual Router RIB/FIB Instance 80"""
    def __init__(self, router_id: str = "10.200.80.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_81:
    """Virtual Router RIB/FIB Instance 81"""
    def __init__(self, router_id: str = "10.200.81.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_82:
    """Virtual Router RIB/FIB Instance 82"""
    def __init__(self, router_id: str = "10.200.82.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_83:
    """Virtual Router RIB/FIB Instance 83"""
    def __init__(self, router_id: str = "10.200.83.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_84:
    """Virtual Router RIB/FIB Instance 84"""
    def __init__(self, router_id: str = "10.200.84.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_85:
    """Virtual Router RIB/FIB Instance 85"""
    def __init__(self, router_id: str = "10.200.85.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_86:
    """Virtual Router RIB/FIB Instance 86"""
    def __init__(self, router_id: str = "10.200.86.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_87:
    """Virtual Router RIB/FIB Instance 87"""
    def __init__(self, router_id: str = "10.200.87.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_88:
    """Virtual Router RIB/FIB Instance 88"""
    def __init__(self, router_id: str = "10.200.88.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_89:
    """Virtual Router RIB/FIB Instance 89"""
    def __init__(self, router_id: str = "10.200.89.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_90:
    """Virtual Router RIB/FIB Instance 90"""
    def __init__(self, router_id: str = "10.200.90.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_91:
    """Virtual Router RIB/FIB Instance 91"""
    def __init__(self, router_id: str = "10.200.91.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_92:
    """Virtual Router RIB/FIB Instance 92"""
    def __init__(self, router_id: str = "10.200.92.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_93:
    """Virtual Router RIB/FIB Instance 93"""
    def __init__(self, router_id: str = "10.200.93.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_94:
    """Virtual Router RIB/FIB Instance 94"""
    def __init__(self, router_id: str = "10.200.94.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_95:
    """Virtual Router RIB/FIB Instance 95"""
    def __init__(self, router_id: str = "10.200.95.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_96:
    """Virtual Router RIB/FIB Instance 96"""
    def __init__(self, router_id: str = "10.200.96.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_97:
    """Virtual Router RIB/FIB Instance 97"""
    def __init__(self, router_id: str = "10.200.97.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_98:
    """Virtual Router RIB/FIB Instance 98"""
    def __init__(self, router_id: str = "10.200.98.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_99:
    """Virtual Router RIB/FIB Instance 99"""
    def __init__(self, router_id: str = "10.200.99.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_100:
    """Virtual Router RIB/FIB Instance 100"""
    def __init__(self, router_id: str = "10.200.100.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_101:
    """Virtual Router RIB/FIB Instance 101"""
    def __init__(self, router_id: str = "10.200.101.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_102:
    """Virtual Router RIB/FIB Instance 102"""
    def __init__(self, router_id: str = "10.200.102.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_103:
    """Virtual Router RIB/FIB Instance 103"""
    def __init__(self, router_id: str = "10.200.103.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_104:
    """Virtual Router RIB/FIB Instance 104"""
    def __init__(self, router_id: str = "10.200.104.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_105:
    """Virtual Router RIB/FIB Instance 105"""
    def __init__(self, router_id: str = "10.200.105.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_106:
    """Virtual Router RIB/FIB Instance 106"""
    def __init__(self, router_id: str = "10.200.106.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_107:
    """Virtual Router RIB/FIB Instance 107"""
    def __init__(self, router_id: str = "10.200.107.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_108:
    """Virtual Router RIB/FIB Instance 108"""
    def __init__(self, router_id: str = "10.200.108.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_109:
    """Virtual Router RIB/FIB Instance 109"""
    def __init__(self, router_id: str = "10.200.109.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_110:
    """Virtual Router RIB/FIB Instance 110"""
    def __init__(self, router_id: str = "10.200.110.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_111:
    """Virtual Router RIB/FIB Instance 111"""
    def __init__(self, router_id: str = "10.200.111.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_112:
    """Virtual Router RIB/FIB Instance 112"""
    def __init__(self, router_id: str = "10.200.112.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_113:
    """Virtual Router RIB/FIB Instance 113"""
    def __init__(self, router_id: str = "10.200.113.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_114:
    """Virtual Router RIB/FIB Instance 114"""
    def __init__(self, router_id: str = "10.200.114.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_115:
    """Virtual Router RIB/FIB Instance 115"""
    def __init__(self, router_id: str = "10.200.115.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_116:
    """Virtual Router RIB/FIB Instance 116"""
    def __init__(self, router_id: str = "10.200.116.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_117:
    """Virtual Router RIB/FIB Instance 117"""
    def __init__(self, router_id: str = "10.200.117.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_118:
    """Virtual Router RIB/FIB Instance 118"""
    def __init__(self, router_id: str = "10.200.118.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_119:
    """Virtual Router RIB/FIB Instance 119"""
    def __init__(self, router_id: str = "10.200.119.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_120:
    """Virtual Router RIB/FIB Instance 120"""
    def __init__(self, router_id: str = "10.200.120.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_121:
    """Virtual Router RIB/FIB Instance 121"""
    def __init__(self, router_id: str = "10.200.121.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_122:
    """Virtual Router RIB/FIB Instance 122"""
    def __init__(self, router_id: str = "10.200.122.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_123:
    """Virtual Router RIB/FIB Instance 123"""
    def __init__(self, router_id: str = "10.200.123.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_124:
    """Virtual Router RIB/FIB Instance 124"""
    def __init__(self, router_id: str = "10.200.124.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_125:
    """Virtual Router RIB/FIB Instance 125"""
    def __init__(self, router_id: str = "10.200.125.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_126:
    """Virtual Router RIB/FIB Instance 126"""
    def __init__(self, router_id: str = "10.200.126.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_127:
    """Virtual Router RIB/FIB Instance 127"""
    def __init__(self, router_id: str = "10.200.127.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_128:
    """Virtual Router RIB/FIB Instance 128"""
    def __init__(self, router_id: str = "10.200.128.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_129:
    """Virtual Router RIB/FIB Instance 129"""
    def __init__(self, router_id: str = "10.200.129.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_130:
    """Virtual Router RIB/FIB Instance 130"""
    def __init__(self, router_id: str = "10.200.130.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_131:
    """Virtual Router RIB/FIB Instance 131"""
    def __init__(self, router_id: str = "10.200.131.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_132:
    """Virtual Router RIB/FIB Instance 132"""
    def __init__(self, router_id: str = "10.200.132.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_133:
    """Virtual Router RIB/FIB Instance 133"""
    def __init__(self, router_id: str = "10.200.133.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_134:
    """Virtual Router RIB/FIB Instance 134"""
    def __init__(self, router_id: str = "10.200.134.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_135:
    """Virtual Router RIB/FIB Instance 135"""
    def __init__(self, router_id: str = "10.200.135.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_136:
    """Virtual Router RIB/FIB Instance 136"""
    def __init__(self, router_id: str = "10.200.136.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_137:
    """Virtual Router RIB/FIB Instance 137"""
    def __init__(self, router_id: str = "10.200.137.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_138:
    """Virtual Router RIB/FIB Instance 138"""
    def __init__(self, router_id: str = "10.200.138.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_139:
    """Virtual Router RIB/FIB Instance 139"""
    def __init__(self, router_id: str = "10.200.139.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_140:
    """Virtual Router RIB/FIB Instance 140"""
    def __init__(self, router_id: str = "10.200.140.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_141:
    """Virtual Router RIB/FIB Instance 141"""
    def __init__(self, router_id: str = "10.200.141.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_142:
    """Virtual Router RIB/FIB Instance 142"""
    def __init__(self, router_id: str = "10.200.142.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_143:
    """Virtual Router RIB/FIB Instance 143"""
    def __init__(self, router_id: str = "10.200.143.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_144:
    """Virtual Router RIB/FIB Instance 144"""
    def __init__(self, router_id: str = "10.200.144.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_145:
    """Virtual Router RIB/FIB Instance 145"""
    def __init__(self, router_id: str = "10.200.145.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_146:
    """Virtual Router RIB/FIB Instance 146"""
    def __init__(self, router_id: str = "10.200.146.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_147:
    """Virtual Router RIB/FIB Instance 147"""
    def __init__(self, router_id: str = "10.200.147.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_148:
    """Virtual Router RIB/FIB Instance 148"""
    def __init__(self, router_id: str = "10.200.148.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_149:
    """Virtual Router RIB/FIB Instance 149"""
    def __init__(self, router_id: str = "10.200.149.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_150:
    """Virtual Router RIB/FIB Instance 150"""
    def __init__(self, router_id: str = "10.200.150.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_151:
    """Virtual Router RIB/FIB Instance 151"""
    def __init__(self, router_id: str = "10.200.151.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_152:
    """Virtual Router RIB/FIB Instance 152"""
    def __init__(self, router_id: str = "10.200.152.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_153:
    """Virtual Router RIB/FIB Instance 153"""
    def __init__(self, router_id: str = "10.200.153.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_154:
    """Virtual Router RIB/FIB Instance 154"""
    def __init__(self, router_id: str = "10.200.154.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_155:
    """Virtual Router RIB/FIB Instance 155"""
    def __init__(self, router_id: str = "10.200.155.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_156:
    """Virtual Router RIB/FIB Instance 156"""
    def __init__(self, router_id: str = "10.200.156.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_157:
    """Virtual Router RIB/FIB Instance 157"""
    def __init__(self, router_id: str = "10.200.157.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_158:
    """Virtual Router RIB/FIB Instance 158"""
    def __init__(self, router_id: str = "10.200.158.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_159:
    """Virtual Router RIB/FIB Instance 159"""
    def __init__(self, router_id: str = "10.200.159.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1


class VirtualRouterInstance_160:
    """Virtual Router RIB/FIB Instance 160"""
    def __init__(self, router_id: str = "10.200.160.1"):
        self.router_id = router_id
        self.rib: List[RouteEntry] = []
        self.fib: Dict[str, str] = {}

    def add_route(self, prefix: str, nexthop: str, metric: int = 10) -> None:
        self.rib.append(RouteEntry(prefix, nexthop, metric))
        self.fib[prefix] = nexthop

    def lookup(self, dst_ip: str) -> str:
        return self.fib.get(dst_ip, f"10.200.{self.router_id.split('.')[-2]}.254")

VirtualRouterInstance = VirtualRouterInstance_1
