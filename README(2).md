# AIOps — Quick Practical Notes

## 1. Basic Git Workflow

```bash
git status
git add .
git commit -m "message"
git push
```

Remember:

**status → add → commit → push**

---

## 2. AIOps Anomaly Detection

### Core Pattern

```text
Dataset
   ↓
Pandas DataFrame
   ↓
Basic Statistics
   ↓
Set Thresholds
   ↓
Create Anomaly Condition
   ↓
Filter Anomalies
   ↓
Plot / Save Graph
```

### Imports

```python
import pandas as pd
import matplotlib.pyplot as plt
```

### Create DataFrame

```python
df = pd.DataFrame(data)
```

### Basic Statistics

```python
print(df.describe())
```

Useful functions:

```python
df.head()
df.info()
df.describe()
```

### Threshold-Based Anomaly Detection

Use `|` for **OR**:

```python
df["Anomaly"] = (
    (df["CPU Usage"] > CPU_THRESHOLD) |
    (df["Memory Usage"] > MEMORY_THRESHOLD) |
    (df["Response Time"] > RESPONSE_THRESHOLD)
)
```

Then:

```python
anomalies = df[df["Anomaly"]]
print(anomalies)
```

### Remember

- `>` = greater than threshold → anomaly
- `|` = OR
- `&` = AND
- `df[df["Anomaly"]]` = only anomalous rows

---

## 3. Graph Pattern

```python
plt.figure(figsize=(10, 5))

plt.plot(
    df["Timestamp"],
    df["CPU Usage"],
    marker="o",
    label="CPU Usage"
)

plt.scatter(
    anomalies["Timestamp"],
    anomalies["CPU Usage"],
    s=100,
    label="Anomaly"
)

plt.axhline(
    CPU_THRESHOLD,
    linestyle="--",
    label="CPU Threshold"
)

plt.xlabel("Timestamp")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage and Anomalies")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("anomaly_graph.png")
```

### Codespaces Graph

`plt.show()` may not display a GUI in Codespaces.

Use:

```python
plt.savefig("anomaly_graph.png")
```

Then open the PNG from the Explorer.

---

## 4. Same Pattern for Other AIOps Questions

### Server Monitoring

Possible columns:

```text
CPU
Memory
Disk
Response Time
```

### Network Monitoring

Possible columns:

```text
Incoming Traffic
Outgoing Traffic
Packet Loss
Latency
```

### General Formula

```text
Choose metric
     ↓
Set threshold
     ↓
Compare metric > threshold
     ↓
Create Anomaly column
     ↓
Filter rows
     ↓
Plot important metric
```

---

## 5. Important Python/Pandas Syntax

```python
df["Column"]
```

Select a column.

```python
df[df["Anomaly"]]
```

Filter rows.

```python
(df["CPU"] > 90)
```

Condition.

```python
condition1 | condition2
```

OR.

```python
condition1 & condition2
```

AND.

---

## 6. Exam Memory Trick

For AIOps anomaly questions:

**Data → Describe → Threshold → Condition → Filter → Graph**

Don't overthink it.
