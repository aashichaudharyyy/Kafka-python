"""
AIOps Processor Module
Evaluates consumed events, assesses severity, and generates actionable operations alerts.
"""

from typing import Dict, Any, Optional, List


def process_event(event: Optional[Dict[str, Any]]) -> str:
    """
    Processes an anomaly event and produces the final AIOps alert string.
    Handles None gracefully and supports case-insensitive severity evaluation.
    """
    if event is None:
        return "No event"

    severity = str(event.get("severity", "")).lower()
    metric = event.get("metric", "unknown")
    val = event.get("value", 0)
    thresh = event.get("threshold", "threshold")

    # Format expected by end-to-end simulation
    if severity in ["critical", "high", "warn", "warning"]:
        return f"AIOps ALERT: {metric} = {val} exceeded threshold {thresh}"

    return f"Event processed: {event.get('type', 'GENERIC_EVENT')}"


def format_alert(event: Dict[str, Any]) -> str:
    """
    Alternative alert format helper for detailed operational reporting.
    """
    return f"ALERT: {event.get('metric', 'unknown')} anomaly detected with value {event.get('value')}"


def process_events(events: List[Dict[str, Any]]) -> List[str]:
    """
    Batch processes a list of consumed events into alerts.
    """
    return [process_event(e) for e in events if e is not None]
