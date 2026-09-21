"""
Event Generator Module
Converts raw metric anomaly detections into structured, standardized event messages
for publication through the event channel.
"""

from typing import Dict, Any, Optional, List
from .anomaly_detector import CPU_THRESHOLD, THRESHOLDS


def generate_event(
    arg1: Any = None,
    value: Optional[float] = None,
    threshold: Optional[float] = None,
    severity: str = "critical",
    **kwargs: Any
) -> Dict[str, Any]:
    """
    Generates a structured anomaly event.
    Supports flexible invocation styles:
      - generate_event(95) -> CPU_ANOMALY event with default CPU threshold
      - generate_event("cpu", 95, 80, "critical")
      - generate_event(metric="cpu", value=95, threshold=80, severity="critical")
    """
    # Case 1: single numeric argument passed -> treated as CPU value (e.g., generate_event(95))
    if isinstance(arg1, (int, float)) and value is None:
        metric = "cpu"
        val = float(arg1)
        thresh = threshold if threshold is not None else CPU_THRESHOLD
    # Case 2: metric name passed as first argument
    elif isinstance(arg1, str):
        metric = arg1
        val = float(value) if value is not None else kwargs.get("value", 0.0)
        thresh = threshold if threshold is not None else THRESHOLDS.get(metric, 80.0)
    # Case 3: keyword argument invocation or dict
    elif isinstance(arg1, dict):
        metric = arg1.get("metric", "cpu")
        val = float(arg1.get("value", 0.0))
        thresh = arg1.get("threshold", THRESHOLDS.get(metric, 80.0))
        severity = arg1.get("severity", severity)
    else:
        metric = kwargs.get("metric", "cpu")
        val = float(value) if value is not None else float(kwargs.get("value", 0.0))
        thresh = threshold if threshold is not None else float(kwargs.get("threshold", THRESHOLDS.get(metric, 80.0)))

    event = {
        "type": f"{metric.upper()}_ANOMALY",
        "metric": metric,
        "value": val,
        "threshold": thresh,
        "severity": severity,
    }

    if "timestamp" in kwargs:
        event["timestamp"] = kwargs["timestamp"]

    return event


def generate_events_from_anomalies(metrics: Dict[str, Any], anomalies: List[str]) -> List[Dict[str, Any]]:
    """
    Converts a list of anomaly names (e.g. ['high_cpu', 'high_latency'])
    into a list of structured event dictionaries.
    """
    events = []
    anomaly_to_metric = {
        "high_cpu": "cpu",
        "high_memory": "memory",
        "high_latency": "latency"
    }

    for anomaly in anomalies:
        metric_name = anomaly_to_metric.get(anomaly, anomaly.replace("high_", ""))
        if metric_name in metrics:
            val = float(metrics[metric_name])
            thresh = THRESHOLDS.get(metric_name, 0.0)
            events.append(generate_event(metric=metric_name, value=val, threshold=thresh, severity="critical"))

    return events
