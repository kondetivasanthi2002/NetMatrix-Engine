"""NetMatrix Configuration Management Module"""
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

class NetworkConfig(BaseModel):
    interface: str = "eth0"
    ip_address: str = "192.168.1.1"
    netmask: str = "255.255.255.0"
    mac_address: str = "00:11:22:33:44:55"
    mtu: int = 1500

class SecurityConfig(BaseModel):
    firewall_enabled: bool = True
    ids_enabled: bool = True
    default_policy: str = "DROP"

class AppConfig(BaseModel):
    app_name: str = "NetMatrix"
    network: NetworkConfig = Field(default_factory=NetworkConfig)
    security: SecurityConfig = Field(default_factory=SecurityConfig)

def get_default_config() -> AppConfig:
    return AppConfig()
