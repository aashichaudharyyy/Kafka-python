"""
Integration Tests for End-to-End AIOps Workflow.
Validates the complete pipeline from Operational Data to final AIOps Alert.
"""

import pytest
from src.operational_data import load_metrics_csv, load_operational_json, get_sample_data
from src.anomaly_detector import detect_anomaly, detect_anomalies
from src.event_generator import generate_event
from src.topic import Topic
from src.producer import Producer
from src.consumer import Consumer
from src.aiops_processor import process_event


def test_complete_anomalous_workflow():
    """
    Validates end-to-end pipeline with anomalous operational data:
    Data -> Anomaly -> Event -> Producer -> Topic -> Consumer -> Alert
    """
    operational_data = {"cpu": 95}
    topic = Topic("system-events")
    producer = Producer(topic)
    consumer = Consumer(topic)

    cpu = operational_data["cpu"]
    assert detect_anomaly(cpu) is True

    event = generate_event(cpu)
    assert event["type"] == "CPU_ANOMALY"
    assert event["value"] == 95.0

    producer.send(event)
    assert topic.size() == 1

    received_event = consumer.receive()
    assert received_event == event

    output = process_event(received_event)
    assert "AIOps ALERT: cpu = 95.0 exceeded threshold 80.0" in output


def test_normal_operational_workflow():
    """
    Validates that normal operational data does not trigger an alert or event.
    """
    operational_data = {"cpu": 45}
    topic = Topic("system-events")
    producer = Producer(topic)
    consumer = Consumer(topic)

    cpu = operational_data["cpu"]
    is_anomaly = detect_anomaly(cpu)
    assert is_anomaly is False

    # No event should be sent to topic
    assert topic.is_empty() is True
    assert consumer.receive() is None


def test_csv_data_pipeline_execution():
    """
    Validates pipeline using real CSV metrics data.
    """
    metrics_records = load_metrics_csv("data/metrics.csv")
    assert len(metrics_records) > 0

    topic = Topic("system-events")
    producer = Producer(topic)
    consumer = Consumer(topic)

    anomalous_count = 0
    for record in metrics_records:
        cpu = record["cpu"]
        if detect_anomaly(cpu):
            anomalous_count += 1
            event = generate_event(cpu)
            producer.send(event)

    assert anomalous_count >= 2  # records 10:02 (95) and 10:04 (92)
    assert topic.size() == anomalous_count

    consumed_alerts = []
    while not topic.is_empty():
        event = consumer.receive()
        alert = process_event(event)
        consumed_alerts.append(alert)

    assert len(consumed_alerts) == anomalous_count
    for alert in consumed_alerts:
        assert "AIOps ALERT:" in alert
