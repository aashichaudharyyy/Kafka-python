# Question 3 — Python Kafka Consumer

## Problem Statement

Write a Python Kafka consumer that consumes messages from:
`server_metrics`

The consumer should:
1. Connect to the Kafka broker (`localhost:9092`).
2. Subscribe to the `server_metrics` topic.
3. Continuously receive messages.
4. Display the received server metrics.
5. Detect whether CPU usage is greater than 80%.
6. Print:
   ```text
   ALERT: High CPU detected on server01
   ```
   when the condition is satisfied.

### Example Output
```text
Received:
Server: server01
CPU: 85%
Memory: 62%

ALERT: High CPU detected on server01
```

---

## Core Code Structure

```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "server_metrics",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest"
)

for message in consumer:
    data = message.value
    server = data["server_id"]
    cpu = data["cpu_usage"]
    memory = data["memory_usage"]

    print("Received:")
    print(f"Server: {server}")
    print(f"CPU: {cpu}%")
    print(f"Memory: {memory}%")

    if cpu > 80:
        print(f"\nALERT: High CPU detected on {server}\n")
```

---

## How to Run

1. Start your Kafka broker.
2. In Terminal 1, run the consumer:
   ```bash
   python sample/question3/consumer.py
   ```
3. In Terminal 2, publish test records:
   ```bash
   python sample/question3/send_test_messages.py
   ```
4. Observe that `server01` (85% CPU) and `server03` (91% CPU) trigger the alert, while normal records do not.
