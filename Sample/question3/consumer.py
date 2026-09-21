"""
Question 3 — Python Kafka Consumer
Connects to Kafka, subscribes to 'server_metrics', displays received metrics,
and detects when CPU > 80% to issue an alert.
"""

import json
import time

TOPIC_NAME = "server_metrics"
BOOTSTRAP_SERVERS = "localhost:9092"
CPU_THRESHOLD = 80


def process_metric_record(data: dict):
    """
    Processes a single server metric record, displays its values,
    and alerts if CPU exceeds threshold.
    """
    server = data.get("server_id", "unknown")
    cpu = data.get("cpu_usage", 0)
    memory = data.get("memory_usage", 0)

    print("Received:")
    print(f"Server: {server}")
    print(f"CPU: {cpu}%")
    print(f"Memory: {memory}%")

    if cpu > CPU_THRESHOLD:
        print(f"\nALERT: High CPU detected on {server}\n")
    else:
        print()


def run_kafka_consumer():
    """Live Kafka consumer reading from broker."""
    try:
        from kafka import KafkaConsumer
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="aiops-monitoring-group"
        )
        print(f"Subscribed to topic '{TOPIC_NAME}' on {BOOTSTRAP_SERVERS}.")
        print("Listening for server metric events (Press Ctrl+C to stop)...\n")

        for message in consumer:
            data = message.value
            process_metric_record(data)

    except Exception as e:
        print(f"Could not connect to live Kafka broker: {e}")
        print("Running demonstration with sample stream to verify logic & output formatting:\n")
        run_simulation_consumer()


def run_simulation_consumer():
    """Demonstration simulation matching exact exam prompt."""
    test_stream = [
        {"server_id": "server01", "cpu_usage": 85, "memory_usage": 62},
        {"server_id": "server02", "cpu_usage": 65, "memory_usage": 58},
        {"server_id": "server03", "cpu_usage": 92, "memory_usage": 74}
    ]

    for data in test_stream:
        process_metric_record(data)
        time.sleep(0.5)


if __name__ == "__main__":
    run_kafka_consumer()
