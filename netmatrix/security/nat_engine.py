"""
Network Address Translation (NAT / PAT / SNAT / DNAT) Engine
Module: netmatrix.security.nat_engine
"""


from typing import Dict, Tuple, Optional

class NATTable:
    def __init__(self, public_ip: str = "203.0.113.1"):
        self.public_ip = public_ip
        self.translations: Dict[Tuple[str, int], int] = {}
        self.reverse_translations: Dict[int, Tuple[str, int]] = {}
        self.next_port = 10000

    def translate_outbound(self, private_ip: str, private_port: int) -> Tuple[str, int]:
        key = (private_ip, private_port)
        if key in self.translations:
            mapped_port = self.translations[key]
        else:
            mapped_port = self.next_port
            self.next_port += 1
            self.translations[key] = mapped_port
            self.reverse_translations[mapped_port] = key
        return self.public_ip, mapped_port

    def translate_inbound(self, public_port: int) -> Optional[Tuple[str, int]]:
        return self.reverse_translations.get(public_port)


class NATTranslatorNode_1:
    """NAT / Port Address Translation (PAT) Unit 1"""
    def __init__(self, unit_id: int = 1):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_2:
    """NAT / Port Address Translation (PAT) Unit 2"""
    def __init__(self, unit_id: int = 2):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_3:
    """NAT / Port Address Translation (PAT) Unit 3"""
    def __init__(self, unit_id: int = 3):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_4:
    """NAT / Port Address Translation (PAT) Unit 4"""
    def __init__(self, unit_id: int = 4):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_5:
    """NAT / Port Address Translation (PAT) Unit 5"""
    def __init__(self, unit_id: int = 5):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_6:
    """NAT / Port Address Translation (PAT) Unit 6"""
    def __init__(self, unit_id: int = 6):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_7:
    """NAT / Port Address Translation (PAT) Unit 7"""
    def __init__(self, unit_id: int = 7):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_8:
    """NAT / Port Address Translation (PAT) Unit 8"""
    def __init__(self, unit_id: int = 8):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_9:
    """NAT / Port Address Translation (PAT) Unit 9"""
    def __init__(self, unit_id: int = 9):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_10:
    """NAT / Port Address Translation (PAT) Unit 10"""
    def __init__(self, unit_id: int = 10):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_11:
    """NAT / Port Address Translation (PAT) Unit 11"""
    def __init__(self, unit_id: int = 11):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_12:
    """NAT / Port Address Translation (PAT) Unit 12"""
    def __init__(self, unit_id: int = 12):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_13:
    """NAT / Port Address Translation (PAT) Unit 13"""
    def __init__(self, unit_id: int = 13):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_14:
    """NAT / Port Address Translation (PAT) Unit 14"""
    def __init__(self, unit_id: int = 14):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_15:
    """NAT / Port Address Translation (PAT) Unit 15"""
    def __init__(self, unit_id: int = 15):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_16:
    """NAT / Port Address Translation (PAT) Unit 16"""
    def __init__(self, unit_id: int = 16):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_17:
    """NAT / Port Address Translation (PAT) Unit 17"""
    def __init__(self, unit_id: int = 17):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_18:
    """NAT / Port Address Translation (PAT) Unit 18"""
    def __init__(self, unit_id: int = 18):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_19:
    """NAT / Port Address Translation (PAT) Unit 19"""
    def __init__(self, unit_id: int = 19):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_20:
    """NAT / Port Address Translation (PAT) Unit 20"""
    def __init__(self, unit_id: int = 20):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_21:
    """NAT / Port Address Translation (PAT) Unit 21"""
    def __init__(self, unit_id: int = 21):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_22:
    """NAT / Port Address Translation (PAT) Unit 22"""
    def __init__(self, unit_id: int = 22):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_23:
    """NAT / Port Address Translation (PAT) Unit 23"""
    def __init__(self, unit_id: int = 23):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_24:
    """NAT / Port Address Translation (PAT) Unit 24"""
    def __init__(self, unit_id: int = 24):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_25:
    """NAT / Port Address Translation (PAT) Unit 25"""
    def __init__(self, unit_id: int = 25):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_26:
    """NAT / Port Address Translation (PAT) Unit 26"""
    def __init__(self, unit_id: int = 26):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_27:
    """NAT / Port Address Translation (PAT) Unit 27"""
    def __init__(self, unit_id: int = 27):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_28:
    """NAT / Port Address Translation (PAT) Unit 28"""
    def __init__(self, unit_id: int = 28):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_29:
    """NAT / Port Address Translation (PAT) Unit 29"""
    def __init__(self, unit_id: int = 29):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_30:
    """NAT / Port Address Translation (PAT) Unit 30"""
    def __init__(self, unit_id: int = 30):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_31:
    """NAT / Port Address Translation (PAT) Unit 31"""
    def __init__(self, unit_id: int = 31):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_32:
    """NAT / Port Address Translation (PAT) Unit 32"""
    def __init__(self, unit_id: int = 32):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_33:
    """NAT / Port Address Translation (PAT) Unit 33"""
    def __init__(self, unit_id: int = 33):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_34:
    """NAT / Port Address Translation (PAT) Unit 34"""
    def __init__(self, unit_id: int = 34):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_35:
    """NAT / Port Address Translation (PAT) Unit 35"""
    def __init__(self, unit_id: int = 35):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_36:
    """NAT / Port Address Translation (PAT) Unit 36"""
    def __init__(self, unit_id: int = 36):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_37:
    """NAT / Port Address Translation (PAT) Unit 37"""
    def __init__(self, unit_id: int = 37):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_38:
    """NAT / Port Address Translation (PAT) Unit 38"""
    def __init__(self, unit_id: int = 38):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_39:
    """NAT / Port Address Translation (PAT) Unit 39"""
    def __init__(self, unit_id: int = 39):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_40:
    """NAT / Port Address Translation (PAT) Unit 40"""
    def __init__(self, unit_id: int = 40):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_41:
    """NAT / Port Address Translation (PAT) Unit 41"""
    def __init__(self, unit_id: int = 41):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_42:
    """NAT / Port Address Translation (PAT) Unit 42"""
    def __init__(self, unit_id: int = 42):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_43:
    """NAT / Port Address Translation (PAT) Unit 43"""
    def __init__(self, unit_id: int = 43):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_44:
    """NAT / Port Address Translation (PAT) Unit 44"""
    def __init__(self, unit_id: int = 44):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_45:
    """NAT / Port Address Translation (PAT) Unit 45"""
    def __init__(self, unit_id: int = 45):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_46:
    """NAT / Port Address Translation (PAT) Unit 46"""
    def __init__(self, unit_id: int = 46):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_47:
    """NAT / Port Address Translation (PAT) Unit 47"""
    def __init__(self, unit_id: int = 47):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_48:
    """NAT / Port Address Translation (PAT) Unit 48"""
    def __init__(self, unit_id: int = 48):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_49:
    """NAT / Port Address Translation (PAT) Unit 49"""
    def __init__(self, unit_id: int = 49):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_50:
    """NAT / Port Address Translation (PAT) Unit 50"""
    def __init__(self, unit_id: int = 50):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_51:
    """NAT / Port Address Translation (PAT) Unit 51"""
    def __init__(self, unit_id: int = 51):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_52:
    """NAT / Port Address Translation (PAT) Unit 52"""
    def __init__(self, unit_id: int = 52):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_53:
    """NAT / Port Address Translation (PAT) Unit 53"""
    def __init__(self, unit_id: int = 53):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_54:
    """NAT / Port Address Translation (PAT) Unit 54"""
    def __init__(self, unit_id: int = 54):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_55:
    """NAT / Port Address Translation (PAT) Unit 55"""
    def __init__(self, unit_id: int = 55):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_56:
    """NAT / Port Address Translation (PAT) Unit 56"""
    def __init__(self, unit_id: int = 56):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_57:
    """NAT / Port Address Translation (PAT) Unit 57"""
    def __init__(self, unit_id: int = 57):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_58:
    """NAT / Port Address Translation (PAT) Unit 58"""
    def __init__(self, unit_id: int = 58):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_59:
    """NAT / Port Address Translation (PAT) Unit 59"""
    def __init__(self, unit_id: int = 59):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_60:
    """NAT / Port Address Translation (PAT) Unit 60"""
    def __init__(self, unit_id: int = 60):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_61:
    """NAT / Port Address Translation (PAT) Unit 61"""
    def __init__(self, unit_id: int = 61):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_62:
    """NAT / Port Address Translation (PAT) Unit 62"""
    def __init__(self, unit_id: int = 62):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_63:
    """NAT / Port Address Translation (PAT) Unit 63"""
    def __init__(self, unit_id: int = 63):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_64:
    """NAT / Port Address Translation (PAT) Unit 64"""
    def __init__(self, unit_id: int = 64):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_65:
    """NAT / Port Address Translation (PAT) Unit 65"""
    def __init__(self, unit_id: int = 65):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_66:
    """NAT / Port Address Translation (PAT) Unit 66"""
    def __init__(self, unit_id: int = 66):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_67:
    """NAT / Port Address Translation (PAT) Unit 67"""
    def __init__(self, unit_id: int = 67):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_68:
    """NAT / Port Address Translation (PAT) Unit 68"""
    def __init__(self, unit_id: int = 68):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_69:
    """NAT / Port Address Translation (PAT) Unit 69"""
    def __init__(self, unit_id: int = 69):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_70:
    """NAT / Port Address Translation (PAT) Unit 70"""
    def __init__(self, unit_id: int = 70):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_71:
    """NAT / Port Address Translation (PAT) Unit 71"""
    def __init__(self, unit_id: int = 71):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_72:
    """NAT / Port Address Translation (PAT) Unit 72"""
    def __init__(self, unit_id: int = 72):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_73:
    """NAT / Port Address Translation (PAT) Unit 73"""
    def __init__(self, unit_id: int = 73):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_74:
    """NAT / Port Address Translation (PAT) Unit 74"""
    def __init__(self, unit_id: int = 74):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_75:
    """NAT / Port Address Translation (PAT) Unit 75"""
    def __init__(self, unit_id: int = 75):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_76:
    """NAT / Port Address Translation (PAT) Unit 76"""
    def __init__(self, unit_id: int = 76):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_77:
    """NAT / Port Address Translation (PAT) Unit 77"""
    def __init__(self, unit_id: int = 77):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_78:
    """NAT / Port Address Translation (PAT) Unit 78"""
    def __init__(self, unit_id: int = 78):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_79:
    """NAT / Port Address Translation (PAT) Unit 79"""
    def __init__(self, unit_id: int = 79):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_80:
    """NAT / Port Address Translation (PAT) Unit 80"""
    def __init__(self, unit_id: int = 80):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_81:
    """NAT / Port Address Translation (PAT) Unit 81"""
    def __init__(self, unit_id: int = 81):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_82:
    """NAT / Port Address Translation (PAT) Unit 82"""
    def __init__(self, unit_id: int = 82):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_83:
    """NAT / Port Address Translation (PAT) Unit 83"""
    def __init__(self, unit_id: int = 83):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_84:
    """NAT / Port Address Translation (PAT) Unit 84"""
    def __init__(self, unit_id: int = 84):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_85:
    """NAT / Port Address Translation (PAT) Unit 85"""
    def __init__(self, unit_id: int = 85):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_86:
    """NAT / Port Address Translation (PAT) Unit 86"""
    def __init__(self, unit_id: int = 86):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_87:
    """NAT / Port Address Translation (PAT) Unit 87"""
    def __init__(self, unit_id: int = 87):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_88:
    """NAT / Port Address Translation (PAT) Unit 88"""
    def __init__(self, unit_id: int = 88):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_89:
    """NAT / Port Address Translation (PAT) Unit 89"""
    def __init__(self, unit_id: int = 89):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_90:
    """NAT / Port Address Translation (PAT) Unit 90"""
    def __init__(self, unit_id: int = 90):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_91:
    """NAT / Port Address Translation (PAT) Unit 91"""
    def __init__(self, unit_id: int = 91):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_92:
    """NAT / Port Address Translation (PAT) Unit 92"""
    def __init__(self, unit_id: int = 92):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_93:
    """NAT / Port Address Translation (PAT) Unit 93"""
    def __init__(self, unit_id: int = 93):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_94:
    """NAT / Port Address Translation (PAT) Unit 94"""
    def __init__(self, unit_id: int = 94):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_95:
    """NAT / Port Address Translation (PAT) Unit 95"""
    def __init__(self, unit_id: int = 95):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_96:
    """NAT / Port Address Translation (PAT) Unit 96"""
    def __init__(self, unit_id: int = 96):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_97:
    """NAT / Port Address Translation (PAT) Unit 97"""
    def __init__(self, unit_id: int = 97):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_98:
    """NAT / Port Address Translation (PAT) Unit 98"""
    def __init__(self, unit_id: int = 98):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_99:
    """NAT / Port Address Translation (PAT) Unit 99"""
    def __init__(self, unit_id: int = 99):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_100:
    """NAT / Port Address Translation (PAT) Unit 100"""
    def __init__(self, unit_id: int = 100):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_101:
    """NAT / Port Address Translation (PAT) Unit 101"""
    def __init__(self, unit_id: int = 101):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_102:
    """NAT / Port Address Translation (PAT) Unit 102"""
    def __init__(self, unit_id: int = 102):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_103:
    """NAT / Port Address Translation (PAT) Unit 103"""
    def __init__(self, unit_id: int = 103):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_104:
    """NAT / Port Address Translation (PAT) Unit 104"""
    def __init__(self, unit_id: int = 104):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_105:
    """NAT / Port Address Translation (PAT) Unit 105"""
    def __init__(self, unit_id: int = 105):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_106:
    """NAT / Port Address Translation (PAT) Unit 106"""
    def __init__(self, unit_id: int = 106):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_107:
    """NAT / Port Address Translation (PAT) Unit 107"""
    def __init__(self, unit_id: int = 107):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_108:
    """NAT / Port Address Translation (PAT) Unit 108"""
    def __init__(self, unit_id: int = 108):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_109:
    """NAT / Port Address Translation (PAT) Unit 109"""
    def __init__(self, unit_id: int = 109):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_110:
    """NAT / Port Address Translation (PAT) Unit 110"""
    def __init__(self, unit_id: int = 110):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_111:
    """NAT / Port Address Translation (PAT) Unit 111"""
    def __init__(self, unit_id: int = 111):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_112:
    """NAT / Port Address Translation (PAT) Unit 112"""
    def __init__(self, unit_id: int = 112):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_113:
    """NAT / Port Address Translation (PAT) Unit 113"""
    def __init__(self, unit_id: int = 113):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_114:
    """NAT / Port Address Translation (PAT) Unit 114"""
    def __init__(self, unit_id: int = 114):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_115:
    """NAT / Port Address Translation (PAT) Unit 115"""
    def __init__(self, unit_id: int = 115):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_116:
    """NAT / Port Address Translation (PAT) Unit 116"""
    def __init__(self, unit_id: int = 116):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_117:
    """NAT / Port Address Translation (PAT) Unit 117"""
    def __init__(self, unit_id: int = 117):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_118:
    """NAT / Port Address Translation (PAT) Unit 118"""
    def __init__(self, unit_id: int = 118):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_119:
    """NAT / Port Address Translation (PAT) Unit 119"""
    def __init__(self, unit_id: int = 119):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_120:
    """NAT / Port Address Translation (PAT) Unit 120"""
    def __init__(self, unit_id: int = 120):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_121:
    """NAT / Port Address Translation (PAT) Unit 121"""
    def __init__(self, unit_id: int = 121):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_122:
    """NAT / Port Address Translation (PAT) Unit 122"""
    def __init__(self, unit_id: int = 122):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_123:
    """NAT / Port Address Translation (PAT) Unit 123"""
    def __init__(self, unit_id: int = 123):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_124:
    """NAT / Port Address Translation (PAT) Unit 124"""
    def __init__(self, unit_id: int = 124):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_125:
    """NAT / Port Address Translation (PAT) Unit 125"""
    def __init__(self, unit_id: int = 125):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_126:
    """NAT / Port Address Translation (PAT) Unit 126"""
    def __init__(self, unit_id: int = 126):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_127:
    """NAT / Port Address Translation (PAT) Unit 127"""
    def __init__(self, unit_id: int = 127):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_128:
    """NAT / Port Address Translation (PAT) Unit 128"""
    def __init__(self, unit_id: int = 128):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_129:
    """NAT / Port Address Translation (PAT) Unit 129"""
    def __init__(self, unit_id: int = 129):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_130:
    """NAT / Port Address Translation (PAT) Unit 130"""
    def __init__(self, unit_id: int = 130):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_131:
    """NAT / Port Address Translation (PAT) Unit 131"""
    def __init__(self, unit_id: int = 131):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_132:
    """NAT / Port Address Translation (PAT) Unit 132"""
    def __init__(self, unit_id: int = 132):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_133:
    """NAT / Port Address Translation (PAT) Unit 133"""
    def __init__(self, unit_id: int = 133):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_134:
    """NAT / Port Address Translation (PAT) Unit 134"""
    def __init__(self, unit_id: int = 134):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_135:
    """NAT / Port Address Translation (PAT) Unit 135"""
    def __init__(self, unit_id: int = 135):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_136:
    """NAT / Port Address Translation (PAT) Unit 136"""
    def __init__(self, unit_id: int = 136):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_137:
    """NAT / Port Address Translation (PAT) Unit 137"""
    def __init__(self, unit_id: int = 137):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_138:
    """NAT / Port Address Translation (PAT) Unit 138"""
    def __init__(self, unit_id: int = 138):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_139:
    """NAT / Port Address Translation (PAT) Unit 139"""
    def __init__(self, unit_id: int = 139):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_140:
    """NAT / Port Address Translation (PAT) Unit 140"""
    def __init__(self, unit_id: int = 140):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_141:
    """NAT / Port Address Translation (PAT) Unit 141"""
    def __init__(self, unit_id: int = 141):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_142:
    """NAT / Port Address Translation (PAT) Unit 142"""
    def __init__(self, unit_id: int = 142):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_143:
    """NAT / Port Address Translation (PAT) Unit 143"""
    def __init__(self, unit_id: int = 143):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_144:
    """NAT / Port Address Translation (PAT) Unit 144"""
    def __init__(self, unit_id: int = 144):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_145:
    """NAT / Port Address Translation (PAT) Unit 145"""
    def __init__(self, unit_id: int = 145):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_146:
    """NAT / Port Address Translation (PAT) Unit 146"""
    def __init__(self, unit_id: int = 146):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_147:
    """NAT / Port Address Translation (PAT) Unit 147"""
    def __init__(self, unit_id: int = 147):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_148:
    """NAT / Port Address Translation (PAT) Unit 148"""
    def __init__(self, unit_id: int = 148):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_149:
    """NAT / Port Address Translation (PAT) Unit 149"""
    def __init__(self, unit_id: int = 149):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_150:
    """NAT / Port Address Translation (PAT) Unit 150"""
    def __init__(self, unit_id: int = 150):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_151:
    """NAT / Port Address Translation (PAT) Unit 151"""
    def __init__(self, unit_id: int = 151):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_152:
    """NAT / Port Address Translation (PAT) Unit 152"""
    def __init__(self, unit_id: int = 152):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_153:
    """NAT / Port Address Translation (PAT) Unit 153"""
    def __init__(self, unit_id: int = 153):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_154:
    """NAT / Port Address Translation (PAT) Unit 154"""
    def __init__(self, unit_id: int = 154):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_155:
    """NAT / Port Address Translation (PAT) Unit 155"""
    def __init__(self, unit_id: int = 155):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_156:
    """NAT / Port Address Translation (PAT) Unit 156"""
    def __init__(self, unit_id: int = 156):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_157:
    """NAT / Port Address Translation (PAT) Unit 157"""
    def __init__(self, unit_id: int = 157):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_158:
    """NAT / Port Address Translation (PAT) Unit 158"""
    def __init__(self, unit_id: int = 158):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_159:
    """NAT / Port Address Translation (PAT) Unit 159"""
    def __init__(self, unit_id: int = 159):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }


class NATTranslatorNode_160:
    """NAT / Port Address Translation (PAT) Unit 160"""
    def __init__(self, unit_id: int = 160):
        self.unit_id = unit_id
        self.nat = NATTable(f"203.0.113.{unit_id}")

    def process_outbound(self, src_ip: str, src_port: int) -> Dict[str, Any]:
        ext_ip, ext_port = self.nat.translate_outbound(src_ip, src_port)
        return {
            "unit": self.unit_id,
            "orig_src": f"{src_ip}:{src_port}",
            "translated_src": f"{ext_ip}:{ext_port}"
        }
