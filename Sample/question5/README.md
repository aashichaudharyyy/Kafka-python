# Question 5 — Integrated AIOps Challenge

## Problem Statement

Modify your Kafka consumer from Question 3 so that it behaves like a simple AIOps monitoring system.

The consumer should:
1. Receive server metrics from Kafka.
2. Check CPU usage.
3. Detect an anomaly when CPU > 80%.
4. Print an alert (`ALERT: High CPU detected`) or status (`Normal`).
5. Maintain a running count of detected anomalies.

### Example Output
```text
Message received: server01 | CPU: 85%
ALERT: High CPU detected

Message received: server02 | CPU: 45%
Normal

Message received: server03 | CPU: 91%
ALERT: High CPU detected

Total anomalies detected: 2
```

---

## Comparison: Question 3 vs Question 5

| Feature | Question 3 (Basic Consumer) | Question 5 (AIOps Monitoring System) |
|---|---|---|
| **Goal** | Simple message display + threshold print | Stateful AIOps stream monitoring |
| **Output Style** | Multi-line raw dump | Clean operational event logs |
| **Normal Behavior** | Silent or standard print | Explicit `Normal` status output |
| **State Tracking** | Stateless | Stateful running tally of anomalies |
| **Summary** | None | Prints `Total anomalies detected: N` |

---

## How to Run

### Standalone / Simulation Test
```bash
python sample/question5/simulate_stream.py
```

### Live Kafka Consumer
```bash
python sample/question5/aiops_monitoring_consumer.py
```
Send messages from the Question 2 producer or console producer and view real-time stateful detection.
