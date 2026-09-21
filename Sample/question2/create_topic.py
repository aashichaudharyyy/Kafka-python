"""
Question 2 — Programmatic Topic Creation
Creates the 'server_metrics' topic in Kafka using KafkaAdminClient.
"""

TOPIC_NAME = "server_metrics"
BOOTSTRAP_SERVERS = "localhost:9092"

try:
    from kafka.admin import KafkaAdminClient, NewTopic
    from kafka.errors import TopicAlreadyExistsError

    admin = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS)

    topic = NewTopic(
        name=TOPIC_NAME,
        num_partitions=1,
        replication_factor=1
    )

    try:
        admin.create_topics(new_topics=[topic])
        print(f"Topic '{TOPIC_NAME}' created successfully!")
    except TopicAlreadyExistsError:
        print(f"Topic '{TOPIC_NAME}' already exists.")
    finally:
        admin.close()

except Exception as e:
    print(f"Kafka Admin Notice: {e}")
    print(f"Command-line alternative:\n  docker exec kafka /opt/kafka/bin/kafka-topics.sh --create --topic {TOPIC_NAME} --bootstrap-server {BOOTSTRAP_SERVERS}")
