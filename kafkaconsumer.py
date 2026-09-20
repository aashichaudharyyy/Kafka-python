from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "server_metrics2",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest"
)

anomaly_count = 0

for message in consumer:
    data = message.value

    server = data["server_id"]
    cpu = data["cpu_usage"]
    memory = data["memory_usage"]

    print(f"Received:")
    print(f"Server: {server}")
    print(f"CPU: {cpu}%")
    print(f"Memory: {memory}%")

    if cpu > 80:
        anomaly_count += 1
        print(f"ALERT: High CPU detected on {server}")

print(f"Total anomalies detected: {anomaly_count}")