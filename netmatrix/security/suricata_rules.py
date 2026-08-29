"""
Suricata / Snort Signature Rule Parser & Header Matcher
"""
import re
from typing import Dict, Any, Optional

class SuricataRuleParser:
    def __init__(self, rule_string: str):
        self.rule_string = rule_string
        self.action = "alert"
        self.protocol = "tcp"

    def parse(self) -> Dict[str, Any]:
        parts = self.rule_string.split()
        if len(parts) >= 3:
            self.action = parts[0]
            self.protocol = parts[1]
        return {"action": self.action, "protocol": self.protocol, "raw": self.rule_string}
