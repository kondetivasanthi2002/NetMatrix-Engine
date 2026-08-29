"""
OpenTelemetry W3C Trace Context Propagator & Span Collector
"""
import time
from typing import Dict, Any, List

class OpenTelemetrySpan:
    def __init__(self, trace_id: str, span_id: str, name: str):
        self.trace_id = trace_id
        self.span_id = span_id
        self.name = name
        self.start_time = time.time()

    def export_w3c_header(self) -> str:
        return f"00-{self.trace_id}-{self.span_id}-01"
