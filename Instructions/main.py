"""
AIOps MSE Practical Assessment — Main Execution Workflow
Orchestrates the complete simulated event-processing pipeline:
Operational Data -> Anomaly Detection -> Event Generation -> Producer -> Topic -> Consumer -> AIOps Output
"""

import os
import sys

# Ensure local directory and src/ are importable regardless of working directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)
SRC_DIR = os.path.join(CURRENT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from src.anomaly_detector import detect_anomaly, CPU_THRESHOLD
from src.event_generator import generate_event
from src.topic import Topic
from src.producer import Producer
from src.consumer import Consumer
from src.aiops_processor import process_event
from src.operational_data import get_sample_data, load_metrics_csv


def run_simulation(operational_data=None):
    """
    Executes a single simulation cycle.
    """
    if operational_data is None:
        operational_data = {"cpu": 95}

    # Initialize simulated infrastructure
    topic = Topic(name="system-events")
    producer = Producer(topic, topic_name="system-events")
    consumer = Consumer(topic, topic_name="system-events")

    cpu = operational_data["cpu"]

    print("Operational data:", operational_data)

    if detect_anomaly(cpu):
        print("Anomaly detected")

        # Convert detected anomaly into structured event
        event = generate_event(cpu)
        print("Generated event:", event)

        # Publish event through producer
        producer.send(event)
        print("Event published")

        # Retrieve event from consumer
        received_event = consumer.receive()
        print("Consumer received:", received_event)

        # Generate final operations alert
        output = process_event(received_event)
        print(output)
        return output
    else:
        print("System normal")
        return "System normal"


def main():
    """
    Standard assessment entry point.
    """
    # Run the canonical assessment scenario
    run_simulation({"cpu": 95})


if __name__ == "__main__":
    main()
