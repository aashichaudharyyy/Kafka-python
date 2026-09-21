"""
Anomaly Detector Module
Performs threshold-based anomaly detection on system metrics.
Identifies whether metrics fall within normal operating bounds or indicate anomalies.
"""

from typing import Dict, List, Union, Any

CPU_THRESHOLD: float = 80.0
MEMORY_THRESHOLD: float = 90.0
LATENCY_THRESHOLD: float = 500.0

THRESHOLDS: Dict[str, float] = {
    "cpu": CPU_THRESHOLD,
    "memory": MEMORY_THRESHOLD,
    "latency": LATENCY_THRESHOLD,
}


def detect_anomaly(val: Union[float, int, Dict[str, Any]], threshold: float = CPU_THRESHOLD) -> bool:
    """
    Checks if a given CPU metric value (or operational data dict) exceeds the threshold.
    Returns True if an anomaly is detected, False otherwise.
    """
    if isinstance(val, dict):
        cpu_val = float(val.get("cpu", 0))
    else:
        cpu_val = float(val)

    return cpu_val > threshold


def detect_anomalies(metrics: Dict[str, Any], thresholds: Dict[str, float] = THRESHOLDS) -> List[str]:
    """
    Evaluates multiple metrics against configured thresholds.
    Returns a list of detected anomaly identifiers (e.g. ['high_cpu', 'high_latency']).
    """
    anomalies: List[str] = []

    if "cpu" in metrics and float(metrics["cpu"]) > thresholds.get("cpu", CPU_THRESHOLD):
        anomalies.append("high_cpu")

    if "memory" in metrics and float(metrics["memory"]) > thresholds.get("memory", MEMORY_THRESHOLD):
        anomalies.append("high_memory")

    if "latency" in metrics and float(metrics["latency"]) > thresholds.get("latency", LATENCY_THRESHOLD):
        anomalies.append("high_latency")

    return anomalies


def is_system_healthy(metrics: Dict[str, Any]) -> bool:
    """
    Returns True if no anomalies are detected in the given metric snapshot.
    """
    return len(detect_anomalies(metrics)) == 0
