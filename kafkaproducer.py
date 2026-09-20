from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)


for i in range(1, 11):
    producer.send("server_metrics2", {
        "server_id": f"server{i:02d}",
        "cpu_usage": 70 + i,
        "memory_usage": 60 + i
    })

producer.flush()