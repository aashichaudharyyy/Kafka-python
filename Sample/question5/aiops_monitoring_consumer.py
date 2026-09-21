"""
Question 5 — Integrated AIOps Challenge
Kafka Consumer modified to act as an AIOps real-time monitoring system.
Tracks cumulative anomalies, detects CPU > 80%, and formats operational alerts.
"""

import json
import time

TOPIC_NAME = "server_metrics"
BOOTSTRAP_SERVERS = "localhost:9092"
CPU_THRESHOLD = 80


class AIOpsMonitor:
    """AIOps Real-time Metric Monitoring System."""
    def __init__(self, cpu_threshold: float = CPU_THRESHOLD):
        self.cpu_threshold = cpu_threshold
        self.total_anomalies = 0
        self.total_processed = 0

    def process_message(self, data: dict):
        """Processes a single metric payload and updates state."""
        self.total_processed += 1
        server = data.get("server_id", "unknown")
        cpu = data.get("cpu_usage", 0)

        print(f"Message received: {server} | CPU: {cpu}%")

        if cpu > self.cpu_threshold:
            self.total_anomalies += 1
            print("ALERT: High CPU detected\n")
        else:
            print("Normal\n")

    def print_summary(self):
        """Prints total detected anomaly count."""
        print(f"Total anomalies detected: {self.total_anomalies}")


def run_live_consumer():
    """Consumes from live Kafka topic."""
    monitor = AIOpsMonitor()
    try:
        from kafka import KafkaConsumer
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="aiops-integrated-monitor"
        )
        print(f"AIOps Monitoring System active on topic '{TOPIC_NAME}'.")
        print("Awaiting metric stream (Press Ctrl+C to terminate)...\n")

        for message in consumer:
            monitor.process_message(message.value)

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        monitor.print_summary()
    except Exception as e:
        print(f"Notice: Kafka connection unavailable ({e}).")
        print("Switching to simulation mode to verify monitor output:\n")
        run_simulation_stream(monitor)


def run_simulation_stream(monitor: AIOpsMonitor = None):
    """Replicates the exact sequence from the exam prompt."""
    if monitor is None:
        monitor = AIOpsMonitor()

    sample_messages = [
        {"server_id": "server01", "cpu_usage": 85, "memory_usage": 62},
        {"server_id": "server02", "cpu_usage": 45, "memory_usage": 50},
        {"server_id": "server03", "cpu_usage": 91, "memory_usage": 70}
    ]

    for msg in sample_messages:
        monitor.process_message(msg)
        time.sleep(0.4)

    monitor.print_summary()


if __name__ == "__main__":
    run_live_consumer()
