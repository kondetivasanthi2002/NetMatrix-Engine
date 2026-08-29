# NetMatrix Enterprise Network Observability & Management Suite

NetMatrix is a modern, high-performance, modular enterprise networking platform.

## Key Capabilities
- **Core Packet Processing Engine**: Ethernet, IPv4/IPv6, TCP/UDP, ICMP, DNS, DHCP, NetFlow v9/IPFIX, VXLAN, MPLS.
- **Routing & Topology Simulator**: OSPF Link-State, BGP Path Attribute Engine, Dijkstra Shortest Pathfinder, Spanning Tree (STP), IPAM CIDR Subnet Calculator.
- **Security & Inspection**: Stateful Packet Inspection Firewall, Access Control Lists (ACLs), Dynamic NAT Engine (SNAT/DNAT/PAT), Deep Packet Inspection (DPI) IDS/IPS Matcher, TLS Handshake Validator.
- **Telemetry & Observability**: Prometheus Metrics Exporter, Bandwidth Throughput Analytics, RFC 3550 Latency & Jitter Tracker, Event Logger & Alerting Engine.
- **APIs & Visualization**: FastAPI REST Endpoints, WebSocket Packet Streamer, Single-Page Visual Web Dashboard.
- **Automated Test Suite**: 5+ comprehensive unit & integration test suites covering packet parsing, IP routing, firewall rules, network topology pathfinding, and NAT translation.

## Installation & Running Tests
```bash
pip install -e .
pytest tests/
```
