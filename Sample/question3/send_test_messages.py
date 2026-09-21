"""
Question 3 — Helper Producer to feed test messages into Kafka.
"""

import json
import time

TOPIC_NAME = "server_metrics"
BOOTSTRAP_SERVERS = "localhost:9092"

test_data = [
    {"server_id": "server01", "cpu_usage": 85, "memory_usage": 62},
    {"server_id": "server02", "cpu_usage": 45, "memory_usage": 50},
    {"server_id": "server03", "cpu_usage": 91, "memory_usage": 70}
]

try:
    from kafka import KafkaProducer
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )
    for record in test_data:
        producer.send(TOPIC_NAME, record)
        print(f"Sent: {record}")
        time.sleep(0.5)
    producer.flush()
    producer.close()
    print("Test messages sent.")
except Exception as e:
    print(f"Could not connect to Kafka: {e}")
