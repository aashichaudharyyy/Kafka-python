"""
Unit Tests for Event Generator Component.
Validates structured schema generation and field correctness.
"""

import pytest
from src.event_generator import generate_event, generate_events_from_anomalies


def test_event_type():
    """Exact test specification from exam guide Section 27."""
    event = generate_event(95)
    assert event["type"] == "CPU_ANOMALY"


def test_event_fields_from_single_cpu_value():
    """Validates complete event schema for single CPU value."""
    event = generate_event(95)
    assert event["type"] == "CPU_ANOMALY"
    assert event["metric"] == "cpu"
    assert event["value"] == 95.0
    assert event["threshold"] == 80.0
    assert event["severity"] == "critical"


def test_event_custom_metric():
    """Validates event generation with explicit metric, value, and threshold."""
    event = generate_event(metric="latency", value=650, threshold=500, severity="critical")
    assert event["type"] == "LATENCY_ANOMALY"
    assert event["metric"] == "latency"
    assert event["value"] == 650.0
    assert event["threshold"] == 500.0
    assert event["severity"] == "critical"


def test_generate_events_from_multiple_anomalies():
    """Validates batch event generation from multiple detected anomalies."""
    metrics = {
        "cpu": 95,
        "memory": 92,
        "latency": 300
    }
    anomalies = ["high_cpu", "high_memory"]
    events = generate_events_from_anomalies(metrics, anomalies)

    assert len(events) == 2
    types = [e["type"] for e in events]
    assert "CPU_ANOMALY" in types
    assert "MEMORY_ANOMALY" in types
