"""
IP Address Management (IPAM) & DHCP Reservation Engine
Module: netmatrix.routing.ipam_service
"""


from typing import Dict, Any, Set

class IPAMAllocator:
    def __init__(self, subnet_cidr: str = "10.100.0.0/16"):
        self.subnet_cidr = subnet_cidr
        self.allocated_ips: Set[str] = set()

    def allocate(self, requested_ip: str) -> bool:
        if requested_ip in self.allocated_ips:
            return False
        self.allocated_ips.add(requested_ip)
        return True

    def release(self, ip: str) -> None:
        self.allocated_ips.discard(ip)


class IPAMDomainPool_1:
    """IPAM Subdomain Address Allocation Controller 1"""
    def __init__(self, pool_id: int = 1):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_2:
    """IPAM Subdomain Address Allocation Controller 2"""
    def __init__(self, pool_id: int = 2):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_3:
    """IPAM Subdomain Address Allocation Controller 3"""
    def __init__(self, pool_id: int = 3):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_4:
    """IPAM Subdomain Address Allocation Controller 4"""
    def __init__(self, pool_id: int = 4):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_5:
    """IPAM Subdomain Address Allocation Controller 5"""
    def __init__(self, pool_id: int = 5):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_6:
    """IPAM Subdomain Address Allocation Controller 6"""
    def __init__(self, pool_id: int = 6):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_7:
    """IPAM Subdomain Address Allocation Controller 7"""
    def __init__(self, pool_id: int = 7):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_8:
    """IPAM Subdomain Address Allocation Controller 8"""
    def __init__(self, pool_id: int = 8):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_9:
    """IPAM Subdomain Address Allocation Controller 9"""
    def __init__(self, pool_id: int = 9):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_10:
    """IPAM Subdomain Address Allocation Controller 10"""
    def __init__(self, pool_id: int = 10):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_11:
    """IPAM Subdomain Address Allocation Controller 11"""
    def __init__(self, pool_id: int = 11):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_12:
    """IPAM Subdomain Address Allocation Controller 12"""
    def __init__(self, pool_id: int = 12):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_13:
    """IPAM Subdomain Address Allocation Controller 13"""
    def __init__(self, pool_id: int = 13):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_14:
    """IPAM Subdomain Address Allocation Controller 14"""
    def __init__(self, pool_id: int = 14):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_15:
    """IPAM Subdomain Address Allocation Controller 15"""
    def __init__(self, pool_id: int = 15):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_16:
    """IPAM Subdomain Address Allocation Controller 16"""
    def __init__(self, pool_id: int = 16):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_17:
    """IPAM Subdomain Address Allocation Controller 17"""
    def __init__(self, pool_id: int = 17):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_18:
    """IPAM Subdomain Address Allocation Controller 18"""
    def __init__(self, pool_id: int = 18):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_19:
    """IPAM Subdomain Address Allocation Controller 19"""
    def __init__(self, pool_id: int = 19):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_20:
    """IPAM Subdomain Address Allocation Controller 20"""
    def __init__(self, pool_id: int = 20):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_21:
    """IPAM Subdomain Address Allocation Controller 21"""
    def __init__(self, pool_id: int = 21):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_22:
    """IPAM Subdomain Address Allocation Controller 22"""
    def __init__(self, pool_id: int = 22):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_23:
    """IPAM Subdomain Address Allocation Controller 23"""
    def __init__(self, pool_id: int = 23):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_24:
    """IPAM Subdomain Address Allocation Controller 24"""
    def __init__(self, pool_id: int = 24):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_25:
    """IPAM Subdomain Address Allocation Controller 25"""
    def __init__(self, pool_id: int = 25):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_26:
    """IPAM Subdomain Address Allocation Controller 26"""
    def __init__(self, pool_id: int = 26):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_27:
    """IPAM Subdomain Address Allocation Controller 27"""
    def __init__(self, pool_id: int = 27):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_28:
    """IPAM Subdomain Address Allocation Controller 28"""
    def __init__(self, pool_id: int = 28):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_29:
    """IPAM Subdomain Address Allocation Controller 29"""
    def __init__(self, pool_id: int = 29):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_30:
    """IPAM Subdomain Address Allocation Controller 30"""
    def __init__(self, pool_id: int = 30):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_31:
    """IPAM Subdomain Address Allocation Controller 31"""
    def __init__(self, pool_id: int = 31):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_32:
    """IPAM Subdomain Address Allocation Controller 32"""
    def __init__(self, pool_id: int = 32):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_33:
    """IPAM Subdomain Address Allocation Controller 33"""
    def __init__(self, pool_id: int = 33):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_34:
    """IPAM Subdomain Address Allocation Controller 34"""
    def __init__(self, pool_id: int = 34):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_35:
    """IPAM Subdomain Address Allocation Controller 35"""
    def __init__(self, pool_id: int = 35):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_36:
    """IPAM Subdomain Address Allocation Controller 36"""
    def __init__(self, pool_id: int = 36):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_37:
    """IPAM Subdomain Address Allocation Controller 37"""
    def __init__(self, pool_id: int = 37):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_38:
    """IPAM Subdomain Address Allocation Controller 38"""
    def __init__(self, pool_id: int = 38):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_39:
    """IPAM Subdomain Address Allocation Controller 39"""
    def __init__(self, pool_id: int = 39):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_40:
    """IPAM Subdomain Address Allocation Controller 40"""
    def __init__(self, pool_id: int = 40):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_41:
    """IPAM Subdomain Address Allocation Controller 41"""
    def __init__(self, pool_id: int = 41):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_42:
    """IPAM Subdomain Address Allocation Controller 42"""
    def __init__(self, pool_id: int = 42):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_43:
    """IPAM Subdomain Address Allocation Controller 43"""
    def __init__(self, pool_id: int = 43):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_44:
    """IPAM Subdomain Address Allocation Controller 44"""
    def __init__(self, pool_id: int = 44):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_45:
    """IPAM Subdomain Address Allocation Controller 45"""
    def __init__(self, pool_id: int = 45):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_46:
    """IPAM Subdomain Address Allocation Controller 46"""
    def __init__(self, pool_id: int = 46):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_47:
    """IPAM Subdomain Address Allocation Controller 47"""
    def __init__(self, pool_id: int = 47):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_48:
    """IPAM Subdomain Address Allocation Controller 48"""
    def __init__(self, pool_id: int = 48):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_49:
    """IPAM Subdomain Address Allocation Controller 49"""
    def __init__(self, pool_id: int = 49):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_50:
    """IPAM Subdomain Address Allocation Controller 50"""
    def __init__(self, pool_id: int = 50):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_51:
    """IPAM Subdomain Address Allocation Controller 51"""
    def __init__(self, pool_id: int = 51):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_52:
    """IPAM Subdomain Address Allocation Controller 52"""
    def __init__(self, pool_id: int = 52):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_53:
    """IPAM Subdomain Address Allocation Controller 53"""
    def __init__(self, pool_id: int = 53):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_54:
    """IPAM Subdomain Address Allocation Controller 54"""
    def __init__(self, pool_id: int = 54):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_55:
    """IPAM Subdomain Address Allocation Controller 55"""
    def __init__(self, pool_id: int = 55):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_56:
    """IPAM Subdomain Address Allocation Controller 56"""
    def __init__(self, pool_id: int = 56):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_57:
    """IPAM Subdomain Address Allocation Controller 57"""
    def __init__(self, pool_id: int = 57):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_58:
    """IPAM Subdomain Address Allocation Controller 58"""
    def __init__(self, pool_id: int = 58):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_59:
    """IPAM Subdomain Address Allocation Controller 59"""
    def __init__(self, pool_id: int = 59):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_60:
    """IPAM Subdomain Address Allocation Controller 60"""
    def __init__(self, pool_id: int = 60):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_61:
    """IPAM Subdomain Address Allocation Controller 61"""
    def __init__(self, pool_id: int = 61):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_62:
    """IPAM Subdomain Address Allocation Controller 62"""
    def __init__(self, pool_id: int = 62):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_63:
    """IPAM Subdomain Address Allocation Controller 63"""
    def __init__(self, pool_id: int = 63):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_64:
    """IPAM Subdomain Address Allocation Controller 64"""
    def __init__(self, pool_id: int = 64):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_65:
    """IPAM Subdomain Address Allocation Controller 65"""
    def __init__(self, pool_id: int = 65):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_66:
    """IPAM Subdomain Address Allocation Controller 66"""
    def __init__(self, pool_id: int = 66):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_67:
    """IPAM Subdomain Address Allocation Controller 67"""
    def __init__(self, pool_id: int = 67):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_68:
    """IPAM Subdomain Address Allocation Controller 68"""
    def __init__(self, pool_id: int = 68):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_69:
    """IPAM Subdomain Address Allocation Controller 69"""
    def __init__(self, pool_id: int = 69):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_70:
    """IPAM Subdomain Address Allocation Controller 70"""
    def __init__(self, pool_id: int = 70):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_71:
    """IPAM Subdomain Address Allocation Controller 71"""
    def __init__(self, pool_id: int = 71):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_72:
    """IPAM Subdomain Address Allocation Controller 72"""
    def __init__(self, pool_id: int = 72):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_73:
    """IPAM Subdomain Address Allocation Controller 73"""
    def __init__(self, pool_id: int = 73):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_74:
    """IPAM Subdomain Address Allocation Controller 74"""
    def __init__(self, pool_id: int = 74):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_75:
    """IPAM Subdomain Address Allocation Controller 75"""
    def __init__(self, pool_id: int = 75):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_76:
    """IPAM Subdomain Address Allocation Controller 76"""
    def __init__(self, pool_id: int = 76):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_77:
    """IPAM Subdomain Address Allocation Controller 77"""
    def __init__(self, pool_id: int = 77):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_78:
    """IPAM Subdomain Address Allocation Controller 78"""
    def __init__(self, pool_id: int = 78):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_79:
    """IPAM Subdomain Address Allocation Controller 79"""
    def __init__(self, pool_id: int = 79):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_80:
    """IPAM Subdomain Address Allocation Controller 80"""
    def __init__(self, pool_id: int = 80):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_81:
    """IPAM Subdomain Address Allocation Controller 81"""
    def __init__(self, pool_id: int = 81):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_82:
    """IPAM Subdomain Address Allocation Controller 82"""
    def __init__(self, pool_id: int = 82):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_83:
    """IPAM Subdomain Address Allocation Controller 83"""
    def __init__(self, pool_id: int = 83):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_84:
    """IPAM Subdomain Address Allocation Controller 84"""
    def __init__(self, pool_id: int = 84):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_85:
    """IPAM Subdomain Address Allocation Controller 85"""
    def __init__(self, pool_id: int = 85):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_86:
    """IPAM Subdomain Address Allocation Controller 86"""
    def __init__(self, pool_id: int = 86):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_87:
    """IPAM Subdomain Address Allocation Controller 87"""
    def __init__(self, pool_id: int = 87):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_88:
    """IPAM Subdomain Address Allocation Controller 88"""
    def __init__(self, pool_id: int = 88):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_89:
    """IPAM Subdomain Address Allocation Controller 89"""
    def __init__(self, pool_id: int = 89):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_90:
    """IPAM Subdomain Address Allocation Controller 90"""
    def __init__(self, pool_id: int = 90):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_91:
    """IPAM Subdomain Address Allocation Controller 91"""
    def __init__(self, pool_id: int = 91):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_92:
    """IPAM Subdomain Address Allocation Controller 92"""
    def __init__(self, pool_id: int = 92):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_93:
    """IPAM Subdomain Address Allocation Controller 93"""
    def __init__(self, pool_id: int = 93):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_94:
    """IPAM Subdomain Address Allocation Controller 94"""
    def __init__(self, pool_id: int = 94):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_95:
    """IPAM Subdomain Address Allocation Controller 95"""
    def __init__(self, pool_id: int = 95):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_96:
    """IPAM Subdomain Address Allocation Controller 96"""
    def __init__(self, pool_id: int = 96):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_97:
    """IPAM Subdomain Address Allocation Controller 97"""
    def __init__(self, pool_id: int = 97):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_98:
    """IPAM Subdomain Address Allocation Controller 98"""
    def __init__(self, pool_id: int = 98):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_99:
    """IPAM Subdomain Address Allocation Controller 99"""
    def __init__(self, pool_id: int = 99):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_100:
    """IPAM Subdomain Address Allocation Controller 100"""
    def __init__(self, pool_id: int = 100):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_101:
    """IPAM Subdomain Address Allocation Controller 101"""
    def __init__(self, pool_id: int = 101):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_102:
    """IPAM Subdomain Address Allocation Controller 102"""
    def __init__(self, pool_id: int = 102):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_103:
    """IPAM Subdomain Address Allocation Controller 103"""
    def __init__(self, pool_id: int = 103):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_104:
    """IPAM Subdomain Address Allocation Controller 104"""
    def __init__(self, pool_id: int = 104):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_105:
    """IPAM Subdomain Address Allocation Controller 105"""
    def __init__(self, pool_id: int = 105):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_106:
    """IPAM Subdomain Address Allocation Controller 106"""
    def __init__(self, pool_id: int = 106):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_107:
    """IPAM Subdomain Address Allocation Controller 107"""
    def __init__(self, pool_id: int = 107):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_108:
    """IPAM Subdomain Address Allocation Controller 108"""
    def __init__(self, pool_id: int = 108):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_109:
    """IPAM Subdomain Address Allocation Controller 109"""
    def __init__(self, pool_id: int = 109):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_110:
    """IPAM Subdomain Address Allocation Controller 110"""
    def __init__(self, pool_id: int = 110):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_111:
    """IPAM Subdomain Address Allocation Controller 111"""
    def __init__(self, pool_id: int = 111):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_112:
    """IPAM Subdomain Address Allocation Controller 112"""
    def __init__(self, pool_id: int = 112):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_113:
    """IPAM Subdomain Address Allocation Controller 113"""
    def __init__(self, pool_id: int = 113):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_114:
    """IPAM Subdomain Address Allocation Controller 114"""
    def __init__(self, pool_id: int = 114):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_115:
    """IPAM Subdomain Address Allocation Controller 115"""
    def __init__(self, pool_id: int = 115):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_116:
    """IPAM Subdomain Address Allocation Controller 116"""
    def __init__(self, pool_id: int = 116):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_117:
    """IPAM Subdomain Address Allocation Controller 117"""
    def __init__(self, pool_id: int = 117):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_118:
    """IPAM Subdomain Address Allocation Controller 118"""
    def __init__(self, pool_id: int = 118):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_119:
    """IPAM Subdomain Address Allocation Controller 119"""
    def __init__(self, pool_id: int = 119):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_120:
    """IPAM Subdomain Address Allocation Controller 120"""
    def __init__(self, pool_id: int = 120):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_121:
    """IPAM Subdomain Address Allocation Controller 121"""
    def __init__(self, pool_id: int = 121):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_122:
    """IPAM Subdomain Address Allocation Controller 122"""
    def __init__(self, pool_id: int = 122):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_123:
    """IPAM Subdomain Address Allocation Controller 123"""
    def __init__(self, pool_id: int = 123):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_124:
    """IPAM Subdomain Address Allocation Controller 124"""
    def __init__(self, pool_id: int = 124):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_125:
    """IPAM Subdomain Address Allocation Controller 125"""
    def __init__(self, pool_id: int = 125):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_126:
    """IPAM Subdomain Address Allocation Controller 126"""
    def __init__(self, pool_id: int = 126):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_127:
    """IPAM Subdomain Address Allocation Controller 127"""
    def __init__(self, pool_id: int = 127):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_128:
    """IPAM Subdomain Address Allocation Controller 128"""
    def __init__(self, pool_id: int = 128):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_129:
    """IPAM Subdomain Address Allocation Controller 129"""
    def __init__(self, pool_id: int = 129):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_130:
    """IPAM Subdomain Address Allocation Controller 130"""
    def __init__(self, pool_id: int = 130):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_131:
    """IPAM Subdomain Address Allocation Controller 131"""
    def __init__(self, pool_id: int = 131):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_132:
    """IPAM Subdomain Address Allocation Controller 132"""
    def __init__(self, pool_id: int = 132):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_133:
    """IPAM Subdomain Address Allocation Controller 133"""
    def __init__(self, pool_id: int = 133):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_134:
    """IPAM Subdomain Address Allocation Controller 134"""
    def __init__(self, pool_id: int = 134):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_135:
    """IPAM Subdomain Address Allocation Controller 135"""
    def __init__(self, pool_id: int = 135):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_136:
    """IPAM Subdomain Address Allocation Controller 136"""
    def __init__(self, pool_id: int = 136):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_137:
    """IPAM Subdomain Address Allocation Controller 137"""
    def __init__(self, pool_id: int = 137):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_138:
    """IPAM Subdomain Address Allocation Controller 138"""
    def __init__(self, pool_id: int = 138):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_139:
    """IPAM Subdomain Address Allocation Controller 139"""
    def __init__(self, pool_id: int = 139):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_140:
    """IPAM Subdomain Address Allocation Controller 140"""
    def __init__(self, pool_id: int = 140):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_141:
    """IPAM Subdomain Address Allocation Controller 141"""
    def __init__(self, pool_id: int = 141):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_142:
    """IPAM Subdomain Address Allocation Controller 142"""
    def __init__(self, pool_id: int = 142):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_143:
    """IPAM Subdomain Address Allocation Controller 143"""
    def __init__(self, pool_id: int = 143):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_144:
    """IPAM Subdomain Address Allocation Controller 144"""
    def __init__(self, pool_id: int = 144):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_145:
    """IPAM Subdomain Address Allocation Controller 145"""
    def __init__(self, pool_id: int = 145):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_146:
    """IPAM Subdomain Address Allocation Controller 146"""
    def __init__(self, pool_id: int = 146):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_147:
    """IPAM Subdomain Address Allocation Controller 147"""
    def __init__(self, pool_id: int = 147):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_148:
    """IPAM Subdomain Address Allocation Controller 148"""
    def __init__(self, pool_id: int = 148):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_149:
    """IPAM Subdomain Address Allocation Controller 149"""
    def __init__(self, pool_id: int = 149):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_150:
    """IPAM Subdomain Address Allocation Controller 150"""
    def __init__(self, pool_id: int = 150):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_151:
    """IPAM Subdomain Address Allocation Controller 151"""
    def __init__(self, pool_id: int = 151):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_152:
    """IPAM Subdomain Address Allocation Controller 152"""
    def __init__(self, pool_id: int = 152):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_153:
    """IPAM Subdomain Address Allocation Controller 153"""
    def __init__(self, pool_id: int = 153):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_154:
    """IPAM Subdomain Address Allocation Controller 154"""
    def __init__(self, pool_id: int = 154):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_155:
    """IPAM Subdomain Address Allocation Controller 155"""
    def __init__(self, pool_id: int = 155):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_156:
    """IPAM Subdomain Address Allocation Controller 156"""
    def __init__(self, pool_id: int = 156):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_157:
    """IPAM Subdomain Address Allocation Controller 157"""
    def __init__(self, pool_id: int = 157):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_158:
    """IPAM Subdomain Address Allocation Controller 158"""
    def __init__(self, pool_id: int = 158):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_159:
    """IPAM Subdomain Address Allocation Controller 159"""
    def __init__(self, pool_id: int = 159):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"


class IPAMDomainPool_160:
    """IPAM Subdomain Address Allocation Controller 160"""
    def __init__(self, pool_id: int = 160):
        self.pool_id = pool_id
        self.allocator = IPAMAllocator(f"10.{pool_id}.0.0/16")

    def claim_ip(self, host_id: int) -> str:
        ip = f"10.{self.pool_id}.0.{host_id}"
        res = self.allocator.allocate(ip)
        return ip if res else "ALLOCATION_FAILED"
