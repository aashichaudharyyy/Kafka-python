"""
Unit Tests for Anomaly Detection Component.
Validates normal vs anomalous threshold evaluation and multi-metric checks.
"""

import pytest
from src.anomaly_detector import (
    detect_anomaly,
    detect_anomalies,
    is_system_healthy,
    CPU_THRESHOLD,
    THRESHOLDS,
)


def test_high_cpu():
    """Validates that a CPU value above threshold is identified as an anomaly."""
    assert detect_anomaly(92) is True
    assert detect_anomaly(95) is True
    assert detect_anomaly(100) is True


def test_high_cpu_is_anomaly():
    """Exact test specification from exam guide Section 27."""
    assert detect_anomaly(95) is True


def test_normal_cpu_is_not_anomaly():
    """Validates that normal CPU values are not flagged as anomalies."""
    assert detect_anomaly(42) is False
    assert detect_anomaly(45) is False
    assert detect_anomaly(50) is False
    assert detect_anomaly(79) is False


def test_threshold_boundary():
    """
    Validates edge cases around the boundary condition (> 80).
    80 is normal; 80.1 or 81 is anomalous.
    """
    assert detect_anomaly(80) is False
    assert detect_anomaly(80.0) is False
    assert detect_anomaly(80.1) is True
    assert detect_anomaly(81) is True


def test_dict_input_anomaly():
    """Validates operational data passed as dictionary."""
    assert detect_anomaly({"cpu": 95}) is True
    assert detect_anomaly({"cpu": 45}) is False


def test_multi_metric_anomalies():
    """Validates multi-metric anomaly detection."""
    metrics = {
        "cpu": 95,
        "memory": 70,
        "latency": 620
    }
    anomalies = detect_anomalies(metrics)
    assert "high_cpu" in anomalies
    assert "high_latency" in anomalies
    assert "high_memory" not in anomalies


def test_healthy_system():
    """Validates system health when all metrics are within safe thresholds."""
    metrics = {
        "cpu": 50,
        "memory": 60,
        "latency": 200
    }
    assert is_system_healthy(metrics) is True
    assert detect_anomalies(metrics) == []
