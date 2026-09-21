"""
Unit Tests for Producer, Topic, and Consumer Components.
Validates event publishing, consumption, empty checks, and FIFO ordering.
"""

import pytest
from src.topic import Topic, QueueTopic
from src.producer import Producer
from src.consumer import Consumer


def test_producer_and_consumer_flow():
    """Validates basic send and receive cycle."""
    topic = Topic("system-events")
    producer = Producer(topic, "system-events")
    consumer = Consumer(topic, "system-events")

    event = {"type": "CPU_ANOMALY", "value": 95}
    producer.send(event)

    assert topic.size() == 1
    received = consumer.receive()
    assert received == event
    assert topic.size() == 0


def test_consumer_empty_topic():
    """Validates consumer returns None when no messages are queued."""
    topic = Topic("system-events")
    consumer = Consumer(topic)

    assert consumer.receive() is None


def test_fifo_message_order():
    """Validates messages are consumed in the order they were published (First-In, First-Out)."""
    topic = Topic("system-events")
    producer = Producer(topic)
    consumer = Consumer(topic)

    events = [
        {"id": 1, "value": 85},
        {"id": 2, "value": 90},
        {"id": 3, "value": 95}
    ]

    for ev in events:
        producer.send(ev)

    assert consumer.receive()["id"] == 1
    assert consumer.receive()["id"] == 2
    assert consumer.receive()["id"] == 3
    assert consumer.receive() is None


def test_list_topic_compatibility():
    """Validates Producer and Consumer work with raw Python list as topic."""
    raw_list = []
    producer = Producer(raw_list)
    consumer = Consumer(raw_list)

    producer.send({"msg": "test"})
    assert len(raw_list) == 1
    assert consumer.receive() == {"msg": "test"}
    assert consumer.receive() is None


def test_queue_topic():
    """Validates QueueTopic thread-safe implementation."""
    q_topic = QueueTopic("system-events")
    q_topic.publish({"type": "EVENT_1"})
    assert q_topic.size() == 1
    assert q_topic.consume() == {"type": "EVENT_1"}
    assert q_topic.consume() is None
