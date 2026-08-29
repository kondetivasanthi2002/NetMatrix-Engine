"""
BGP Community Attribute Filtering & Path Selection Engine
"""
from typing import List, Set, Dict, Any

class BGPCommunityFilter:
    NO_EXPORT = 0xFFFFFF01
    NO_ADVERTISE = 0xFFFFFF02

    def __init__(self):
        self.communities: Set[int] = set()

    def add_community(self, community_val: int):
        self.communities.add(community_val)

    def is_exportable(self) -> bool:
        return self.NO_EXPORT not in self.communities and self.NO_ADVERTISE not in self.communities
