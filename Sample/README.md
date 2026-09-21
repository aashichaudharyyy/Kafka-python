# AIOps Sample Questions — Solutions Index

This folder contains complete, verified, executable solutions for all 5 AIOps sample assessment questions.

---

## Directory Overview

```text
sample/
├── question1/          # Question 1 — AIOps Log Anomaly Detection
│   ├── anomaly_detection.py
│   ├── server_logs.csv
│   ├── anomaly_graph.png
│   └── README.md
│
├── question2/          # Question 2 — Kafka Topic and Producer
│   ├── producer.py
│   ├── create_topic.py
│   ├── kafka_commands.sh
│   └── README.md
│
├── question3/          # Question 3 — Python Kafka Consumer
│   ├── consumer.py
│   ├── send_test_messages.py
│   └── README.md
│
├── question4/          # Question 4 — Build an AIOps Workflow using Airflow
│   ├── aiops_dag.py
│   ├── run_standalone.py
│   └── README.md
│
├── question5/          # Question 5 — Integrated AIOps Challenge
│   ├── aiops_monitoring_consumer.py
│   ├── simulate_stream.py
│   └── README.md
│
└── README.md           # Master index
```

---

## Questions Summary & Quick Execution

### [Question 1: AIOps Log Anomaly Detection](file:///c:/Users/User/OneDrive/Desktop/Kafka-python/sample/question1/README.md)
- **Concepts**: Pandas, `df.describe()`, threshold filtering (`CPU > 90%`), Matplotlib time-series visualization.
- **Run**:
  ```bash
  python sample/question1/anomaly_detection.py
  ```
- **Output**:
  ```text
  Total records: 20
  Anomalies detected: 3

  Timestamp       CPU       Status
  10:05           95%      ANOMALY
  10:12           97%      ANOMALY
  10:18           92%      ANOMALY
  ```

---

### [Question 2: Kafka Topic and Producer](file:///c:/Users/User/OneDrive/Desktop/Kafka-python/sample/question2/README.md)
- **Concepts**: Kafka broker, `KafkaAdminClient`, `KafkaProducer`, UTF-8 JSON serialization, batch publishing of 10 messages.
- **Run**:
  ```bash
  python sample/question2/producer.py
  ```

---

### [Question 3: Python Kafka Consumer](file:///c:/Users/User/OneDrive/Desktop/Kafka-python/sample/question3/README.md)
- **Concepts**: `KafkaConsumer`, JSON deserialization, continuous loop polling, CPU threshold detection (`CPU > 80%`), alert formatting.
- **Run**:
  ```bash
  python sample/question3/consumer.py
  ```

---

### [Question 4: Apache Airflow AIOps Workflow DAG](file:///c:/Users/User/OneDrive/Desktop/Kafka-python/sample/question4/README.md)
- **Concepts**: Apache Airflow DAG, `PythonOperator`, XCom data passing, task dependency ordering:
  `collect_metrics >> process_metrics >> detect_anomaly >> generate_report`.
- **Run**:
  ```bash
  python sample/question4/run_standalone.py
  ```

---

### [Question 5: Integrated AIOps Challenge](file:///c:/Users/User/OneDrive/Desktop/Kafka-python/sample/question5/README.md)
- **Concepts**: Stateful Kafka stream consumer, real-time alert dispatching, running anomaly counter, operational reporting.
- **Run**:
  ```bash
  python sample/question5/simulate_stream.py
  ```
