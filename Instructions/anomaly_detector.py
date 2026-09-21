"""
Root-level re-export for anomaly_detector module.
Allows direct imports: `from anomaly_detector import detect_anomaly, CPU_THRESHOLD`
"""
from src.anomaly_detector import (
    CPU_THRESHOLD,
    MEMORY_THRESHOLD,
    LATENCY_THRESHOLD,
    THRESHOLDS,
    detect_anomaly,
    detect_anomalies,
    is_system_healthy,
)

__all__ = [
    "CPU_THRESHOLD",
    "MEMORY_THRESHOLD",
    "LATENCY_THRESHOLD",
    "THRESHOLDS",
    "detect_anomaly",
    "detect_anomalies",
    "is_system_healthy",
]
