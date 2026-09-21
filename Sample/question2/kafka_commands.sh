#!/bin/bash
# Question 2 — Step-by-Step Kafka CLI Commands

# Step 1: Start / Check Kafka Container in Docker
docker ps
docker start kafka

# Step 2: Create the 'server_metrics' topic
docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --create \
  --topic server_metrics \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1

# Step 3: List Topics to verify creation
docker exec kafka /opt/kafka/bin/kafka-topics.sh \
  --list \
  --bootstrap-server localhost:9092

# Step 4: Interactive Console Producer (Send 10 JSON records)
# Enter the following JSON messages line by line:
# {"server_id": "server01", "cpu_usage": 72, "memory_usage": 56}
# {"server_id": "server02", "cpu_usage": 74, "memory_usage": 57}
# {"server_id": "server03", "cpu_usage": 76, "memory_usage": 58}
# {"server_id": "server04", "cpu_usage": 78, "memory_usage": 59}
# {"server_id": "server05", "cpu_usage": 80, "memory_usage": 60}
# {"server_id": "server06", "cpu_usage": 82, "memory_usage": 61}
# {"server_id": "server07", "cpu_usage": 84, "memory_usage": 62}
# {"server_id": "server08", "cpu_usage": 86, "memory_usage": 63}
# {"server_id": "server09", "cpu_usage": 88, "memory_usage": 64}
# {"server_id": "server10", "cpu_usage": 90, "memory_usage": 65}
docker exec -it kafka /opt/kafka/bin/kafka-console-producer.sh \
  --topic server_metrics \
  --bootstrap-server localhost:9092

# Step 5: Verify messages published using Console Consumer
docker exec -it kafka /opt/kafka/bin/kafka-console-consumer.sh \
  --topic server_metrics \
  --bootstrap-server localhost:9092 \
  --from-beginning
