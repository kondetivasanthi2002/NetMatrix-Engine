# NetMatrix Architecture & Core Specifications

## Component Layering
1. **Core Network Layer**: Low level socket buffer management, Ethernet II frame encoding/decoding, IPv4/IPv6 packet parsing, TCP/UDP state tracking.
2. **Routing & Subnetting**: CIDR VLSM arithmetic, OSPF Link-State Advertisements, BGP Path Attribute Engine, Dijkstra shortest-path PCE.
3. **Security Engine**: Stateful Packet Inspection Firewall, Access Control Lists, NAT/PAT translation engine, Deep Packet Inspection (DPI) IDS signature matcher.
4. **Telemetry & Observability**: Prometheus metrics exporter, OpenTelemetry trace headers, Real-time throughput calculations, Latency/Jitter trackers.
5. **REST API & Web UI**: FastAPI async endpoints, WebSocket telemetry broadcaster, and single-page HTML5 monitoring console.
