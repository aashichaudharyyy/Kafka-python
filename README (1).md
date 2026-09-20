# Kafka — Quick Practical Notes

## 1. Kafka Flow

```text
Kafka Server / Broker
        ↓
      Topic
        ↓
    Producer
        ↓
     Messages
        ↓
     Consumer
```

### Remember
- **Broker** = Kafka server
- **Topic** = category/place where messages are stored
- **Producer** = sends messages
- **Consumer** = reads messages

---

## 2. Start Kafka

For our Codespaces Docker setup, check whether Kafka is running:

```bash
docker ps
```

If the Kafka container already exists but is stopped:

```bash
docker start kafka
```

For the exam, remember the flow rather than the long Docker configuration:

```text
Start Kafka → Create Topic → Producer → Consumer
```

---

## 3. Create Topic

Topic name:

```text
server_metrics
```

Docker command:

```bash
docker exec kafka /opt/kafka/bin/kafka-topics.sh --create --topic server_metrics --bootstrap-server localhost:9092
```

### List Topics

```bash
docker exec kafka /opt/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

---

## 4. Start Producer

```bash
docker exec -it kafka /opt/kafka/bin/kafka-console-producer.sh --topic server_metrics --bootstrap-server localhost:9092
```

After starting, the producer waits for messages:

```text
>
```

Type one JSON message per line.

---

## 5. Message Format

```json
{"server_id":"server01","cpu_usage":82,"memory_usage":65}
```

### Remember the structure

```text
server_id
cpu_usage
memory_usage
```

For Q2, send at least 10 messages.

---

# 6. Consumer — Two Ways

After the producer sends messages, there are **two possible consumers**.

```text
                 server_metrics
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
      Console Consumer     Python Consumer
              ↓                 ↓
        Just display       Read + process
        messages           JSON + logic
```

---

## 6A. Simple Console Consumer — Q2

```bash
docker exec -it kafka /opt/kafka/bin/kafka-console-consumer.sh --topic server_metrics --bootstrap-server localhost:9092 --from-beginning
```

`--from-beginning` means:

**Read available messages from the beginning of the topic.**

This consumer simply displays the messages.

```text
Producer → Topic → Console Consumer
```

If the messages appear, they were successfully published and received.

---

## 6B. Python Kafka Consumer — Q3

Install the library:

```bash
pip install kafka-python
```

Create a Python file:

```bash
touch kafkaconsumer.py
```

Basic code:

```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "server_metrics",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
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
        print(f"ALERT: High CPU detected on {server}")
```

Run:

```bash
python kafkaconsumer.py
```

### Q3 Pattern

```text
Kafka
  ↓
Python Consumer
  ↓
Receive JSON
  ↓
Convert JSON → Python dictionary
  ↓
Extract CPU
  ↓
CPU > 80?
  ↓
ALERT
```

### Important lines

**Connect + subscribe:**

```python
consumer = KafkaConsumer(
    "server_metrics",
    bootstrap_servers="localhost:9092"
)
```

**Continuously receive:**

```python
for message in consumer:
```

**Get message data:**

```python
data = message.value
```

**Detect anomaly:**

```python
if cpu > 80:
```

**Generate alert:**

```python
print(f"ALERT: High CPU detected on {server}")
```

---

## 7. Q2 vs Q3

### Q2 — Simple Kafka Consumer

```text
Producer
   ↓
Kafka Topic
   ↓
Console Consumer
   ↓
Just display messages
```

### Q3 — Python Kafka Consumer

```text
Producer
   ↓
Kafka Topic
   ↓
Python Consumer
   ↓
Read JSON
   ↓
Extract CPU / Memory
   ↓
Apply condition
   ↓
ALERT
```

**Same Kafka setup. Only the consumer changes.**

---

## 8. Complete Exam Flow

```text
1. Start Kafka
       ↓
2. Create Topic
       ↓
3. Start Producer
       ↓
4. Send JSON Messages
       ↓
5. Choose Consumer
       ↓
   ┌───────────────┐
   ↓               ↓
Q2 Console       Q3 Python
Consumer         Consumer
   ↓               ↓
Display          Read + Logic
Messages         + Alert
```

### One-line memory trick

**Start → Topic → Producer → Messages → Consumer**

For Q3:

**Consumer → Read JSON → Check CPU → Alert**

---

## 9. Important Commands

### Check Kafka

```bash
docker ps
```

### Start existing Kafka container

```bash
docker start kafka
```

### Create topic

```bash
docker exec kafka /opt/kafka/bin/kafka-topics.sh --create --topic server_metrics --bootstrap-server localhost:9092
```

### Producer

```bash
docker exec -it kafka /opt/kafka/bin/kafka-console-producer.sh --topic server_metrics --bootstrap-server localhost:9092
```

### Console Consumer

```bash
docker exec -it kafka /opt/kafka/bin/kafka-console-consumer.sh --topic server_metrics --bootstrap-server localhost:9092 --from-beginning
```

### Python Consumer

```bash
python kafkaconsumer.py
```

### Stop interactive Producer/Consumer

```text
Ctrl + C
```

---

## 10. Viva — One-Liners

**What is Kafka?**  
A distributed event-streaming/message-broker platform.

**What is a topic?**  
A named category where Kafka messages are stored.

**What is a producer?**  
An application/process that sends messages to a topic.

**What is a consumer?**  
An application/process that reads messages from a topic.

**What is a broker?**  
A Kafka server that stores and serves messages.

**What does `--from-beginning` do?**  
Reads available messages from the beginning of the topic.

**What is the difference between Q2 and Q3?**  
Q2 uses a console consumer to display messages. Q3 uses a Python consumer to read the JSON and apply logic such as CPU anomaly detection.

---

## Exam Memory Trick

**Broker → Topic → Producer → Consumer**

Producer **puts** messages in the topic.

Consumer **gets** messages from the topic.

For Q3:

**Get → Read → Check → Alert**
