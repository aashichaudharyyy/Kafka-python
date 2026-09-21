# Question 1 — AIOps Log Anomaly Detection

## Problem Statement

You are working as an AIOps engineer for an application server. The server generates logs containing CPU usage, memory usage, and response time.

Create a Python program that:
1. Creates or reads a sample dataset containing:
   - Timestamp
   - CPU Usage
   - Memory Usage
   - Response Time
2. Calculates basic statistics for the metrics.
3. Detects anomalous values using a simple threshold-based approach.
4. Prints the anomalous records.
5. Displays a graph showing the metric values and anomalies.

---

## Expected Output

```text
Total records: 20
Anomalies detected: 3

Timestamp       CPU       Status
10:05           95%      ANOMALY
10:12           97%      ANOMALY
10:18           92%      ANOMALY
```

---

## Core Concepts & Implementation Steps

1. **DataFrame Ingestion**: Create or read operational logs into a pandas DataFrame:
   ```python
   df = pd.DataFrame(data)
   ```
2. **Basic Statistics**: Use `df.describe()` to calculate count, mean, standard deviation, min, and quartiles.
3. **Threshold-Based Anomaly Detection**:
   Define baseline limits:
   ```python
   CPU_THRESHOLD = 90
   MEMORY_THRESHOLD = 90
   RESPONSE_THRESHOLD = 500

   df["Anomaly"] = (
       (df["CPU Usage"] > CPU_THRESHOLD) |
       (df["Memory Usage"] > MEMORY_THRESHOLD) |
       (df["Response Time"] > RESPONSE_THRESHOLD)
   )
   ```
4. **Filter & Display**: Filter records where `df["Anomaly"] == True`.
5. **Visualization**: Plot CPU time series, overlay red scatter points for detected anomalies, and draw horizontal threshold line (`plt.axhline()`).

---

## How to Run

```bash
python sample/question1/anomaly_detection.py
```

The script will:
- Print summary statistics.
- Print the exact 3 anomalous records matching the exam requirement.
- Save the plot to `sample/question1/anomaly_graph.png`.
