# Question 2 — Kafka Topic and Producer

## Problem Statement

Set up a Kafka environment and create a topic called:
`server_metrics`

Perform the following:
1. Start the Kafka server/cluster.
2. Create the `server_metrics` topic.
3. Configure a Kafka producer.
4. Send at least 10 server metric messages. Each message should contain:
   - `server_id`
   - `cpu_usage`
   - `memory_usage`
5. Verify that the messages are successfully published to the topic.

### Example Message
```json
{
    "server_id": "server01",
    "cpu_usage": 82,
    "memory_usage": 65
}
```

---

## Step-by-Step Implementation

### Step 1: Start the Kafka Broker
If using Docker (e.g. in GitHub Codespaces):
```bash
docker ps
docker start kafka
```

### Step 2: Create the Topic (`server_metrics`)
Using CLI:
```bash
docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --create \
  --topic server_metrics \
  --bootstrap-server localhost:9092
```
Or via Python:
```bash
python sample/question2/create_topic.py
```

### Step 3: Run the Python Producer
The script `sample/question2/producer.py` creates a `KafkaProducer`, formats 10 messages with `server_id`, `cpu_usage`, and `memory_usage`, encodes them as UTF-8 JSON, and publishes them to `server_metrics`.

Run:
```bash
python sample/question2/producer.py
```

### Step 4: Verify Publication
Consume messages from the beginning of the topic:
```bash
docker exec -it kafka /opt/kafka/bin/kafka-console-consumer.sh \
  --topic server_metrics \
  --bootstrap-server localhost:9092 \
  --from-beginning
```
If the 10 messages appear in the terminal, the topic creation and producer setup are verified!
