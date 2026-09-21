# AIOps MSE Practical Assessment — Complete Exam Guide

This is the **final exam-focused guide** for the AIOps MSE Practical Assessment.

> **Important:** You are NOT required to set up real Kafka, Airflow, Docker, Kubernetes, AWS, GCP, or other external infrastructure.  
> The assessment uses a **Python-based AIOps simulation**.

The expected workflow is:

```text
Operational Data
      ↓
Anomaly Detection
      ↓
Event Generation
      ↓
Producer
      ↓
Topic
      ↓
Consumer
      ↓
AIOps Output
```

Your job is to understand the provided repository, run it, identify what is normal/abnormal, trace events through the code, debug any fault, fix it minimally, validate everything, document your work, commit/push it, create the required PR, and submit the repository URL/evidence.

---

# 1. What the Exam is Really Testing

The exam mainly checks whether you can:

1. Understand an unfamiliar Python repository.
2. Identify the purpose of different files/components.
3. Understand operational metrics and logs.
4. Identify normal vs unusual behaviour.
5. Understand threshold/anomaly logic.
6. Understand event generation.
7. Understand simulated Producer → Topic → Consumer flow.
8. Trace data end-to-end.
9. Debug broken code logically.
10. Identify root cause.
11. Apply a minimal correction.
12. Run validation/tests.
13. Verify the complete workflow.
14. Document observations, issue, fix and result.
15. Use Git/GitHub correctly.
16. Push to your fork.
17. Create a Pull Request.
18. Keep evidence/screenshots.
19. Submit the required repository URL.

The exam mindset should be:

```text
READ
  ↓
UNDERSTAND
  ↓
RUN
  ↓
OBSERVE
  ↓
TRACE
  ↓
DEBUG
  ↓
FIX
  ↓
TEST
  ↓
VERIFY
  ↓
DOCUMENT
  ↓
COMMIT
  ↓
PUSH
  ↓
PR
```

---

# 2. Likely Repository Structure

The exact filenames may differ, but a repository may look like:

```text
aiops-mse/
│
├── data/
│   ├── metrics.csv
│   ├── logs.txt
│   └── operational_data.json
│
├── src/
│   ├── operational_data.py
│   ├── anomaly_detector.py
│   ├── event_generator.py
│   ├── producer.py
│   ├── topic.py
│   ├── consumer.py
│   └── aiops_processor.py
│
├── tests/
│   ├── test_anomaly_detector.py
│   ├── test_event_generator.py
│   ├── test_producer_consumer.py
│   └── test_workflow.py
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .github/
```

A simpler repository may instead look like:

```text
aiops-mse/
│
├── operational_data.py
├── detector.py
├── event_generator.py
├── producer.py
├── topic.py
├── consumer.py
├── aiops.py
├── main.py
├── tests/
├── requirements.txt
└── README.md
```

Do **not** memorize filenames. Identify the role of each component.

---

# 3. Component Responsibility Map

| Component | Purpose |
|---|---|
| Operational Data | Provides metrics/logs |
| Metrics | Numeric measurements such as CPU/latency |
| Logs | Textual operational records |
| Anomaly Detector | Detects unusual behaviour |
| Event Generator | Converts anomaly into structured event |
| Producer | Publishes/sends event |
| Topic | Simulated event channel |
| Consumer | Receives event |
| AIOps Processor | Generates final alert/output |
| Main | Connects and runs the workflow |
| Tests | Validate expected behaviour |
| README | Documents observations, fixes and reproduction |

---

# 4. First 5 Minutes of the Exam

Do **not** start editing immediately.

Run:

```bash
pwd
ls
ls -la
git status
git branch
git remote -v
git log --oneline -5
```

Inspect the repository:

```bash
find . -maxdepth 2 -type f
```

Read instructions:

```bash
cat README.md
```

Read dependencies:

```bash
cat requirements.txt
```

Look for the program entry point:

```bash
grep -R "__main__" .
```

You may find:

```python
if __name__ == "__main__":
    main()
```

Then the project may run using:

```bash
python main.py
```

or:

```bash
python3 main.py
```

Always follow the repository instructions first.

---

# 5. Understand Every File Before Changing Anything

For every important file ask:

```text
1. What input does this file/function receive?
2. What does it do?
3. What output does it return?
4. Which component receives that output next?
```

Typical trace:

```text
operational_data.py
      ↓
anomaly_detector.py
      ↓
event_generator.py
      ↓
producer.py
      ↓
topic.py
      ↓
consumer.py
      ↓
aiops_processor.py
```

---

# 6. Operational Data

Operational data represents the current behaviour of a system/application.

Example:

```python
data = {
    "cpu": 45,
    "memory": 60,
    "latency": 120,
    "error_rate": 1.2
}
```

Another observation:

```python
data = {
    "cpu": 95,
    "memory": 68,
    "latency": 650,
    "error_rate": 9.4
}
```

The second observation may be abnormal depending on configured thresholds.

---

# 7. Metrics

Metrics are **numeric measurements**.

Examples:

```text
CPU usage = 92%
Memory usage = 74%
Latency = 650 ms
Disk usage = 91%
Error rate = 7.5%
Request count = 1000
Throughput = 250 requests/sec
```

Example Python object:

```python
metrics = {
    "cpu": 92,
    "memory": 74,
    "latency": 650
}
```

---

# 8. Logs

Logs are **textual operational records**.

Example:

```text
INFO Application started
INFO Request processed
WARN CPU usage exceeded expected range
ERROR Database connection failed
ERROR Service unavailable
```

Example parsing:

```python
with open("logs.txt") as file:
    for line in file:
        print(line.strip())
```

Find errors:

```python
with open("logs.txt") as file:
    for line in file:
        if "ERROR" in line:
            print("Error:", line.strip())
```

---

# 9. Metrics vs Logs

| Metrics | Logs |
|---|---|
| Numeric | Textual |
| CPU = 92% | `WARN CPU high` |
| Latency = 500 ms | `ERROR timeout` |
| Useful for threshold/statistical analysis | Useful for event/context analysis |

---

# 10. Normal vs Abnormal Behaviour

Suppose CPU values are:

```text
42
45
47
50
93
```

and the configured threshold is:

```python
CPU_THRESHOLD = 80
```

Then:

```text
42 → normal
45 → normal
47 → normal
50 → normal
93 → anomaly
```

Never invent the threshold.

Find it:

```bash
grep -R "threshold" .
grep -R "THRESHOLD" .
```

---

# 11. Basic Anomaly Detection Code

```python
CPU_THRESHOLD = 80

def detect_anomaly(cpu):
    return cpu > CPU_THRESHOLD
```

Usage:

```python
cpu = 92

if detect_anomaly(cpu):
    print("Anomaly detected")
else:
    print("Normal")
```

---

# 12. Multi-Metric Anomaly Detection

```python
THRESHOLDS = {
    "cpu": 80,
    "memory": 90,
    "latency": 500
}

def detect_anomalies(metrics):
    anomalies = []

    if metrics["cpu"] > THRESHOLDS["cpu"]:
        anomalies.append("high_cpu")

    if metrics["memory"] > THRESHOLDS["memory"]:
        anomalies.append("high_memory")

    if metrics["latency"] > THRESHOLDS["latency"]:
        anomalies.append("high_latency")

    return anomalies
```

Example:

```python
metrics = {
    "cpu": 95,
    "memory": 70,
    "latency": 620
}

print(detect_anomalies(metrics))
```

Possible result:

```text
['high_cpu', 'high_latency']
```

---

# 13. Event Generation

Anomaly detection says:

```text
CPU is abnormal
```

Event generation converts that into a structured event:

```python
event = {
    "type": "CPU_ANOMALY",
    "metric": "cpu",
    "value": 95,
    "threshold": 80,
    "severity": "critical"
}
```

Example:

```python
def generate_event(metric, value, threshold):
    return {
        "type": f"{metric.upper()}_ANOMALY",
        "metric": metric,
        "value": value,
        "threshold": threshold,
        "severity": "critical"
    }
```

---

# 14. Producer

The producer publishes/sends an event.

A simulation may use a Python list:

```python
class Producer:
    def __init__(self, topic):
        self.topic = topic

    def send(self, event):
        self.topic.append(event)
```

Usage:

```python
topic = []

producer = Producer(topic)

producer.send({
    "type": "CPU_ANOMALY",
    "value": 95
})
```

---

# 15. Topic

The topic is the event channel.

The simulation may simply use:

```python
topic = []
```

Producer:

```python
topic.append(event)
```

Consumer:

```python
event = topic.pop(0)
```

Conceptually:

```text
Producer
   ↓
 Topic
   ↓
Consumer
```

No real Kafka broker is required.

---

# 16. Topic Class Example

```python
class Topic:
    def __init__(self):
        self.messages = []

    def publish(self, event):
        self.messages.append(event)

    def consume(self):
        if self.messages:
            return self.messages.pop(0)

        return None
```

Usage:

```python
topic = Topic()

topic.publish({
    "type": "CPU_ANOMALY",
    "value": 95
})

print(topic.consume())
```

---

# 17. Queue-Based Topic Simulation

The project may use `queue.Queue`.

```python
from queue import Queue

topic = Queue()
```

Producer:

```python
topic.put(event)
```

Consumer:

```python
event = topic.get()
```

Complete example:

```python
from queue import Queue

topic = Queue()

event = {
    "type": "CPU_ANOMALY",
    "value": 95
}

topic.put(event)

received_event = topic.get()

print(received_event)
```

---

# 18. Consumer

Example:

```python
class Consumer:
    def __init__(self, topic):
        self.topic = topic

    def receive(self):
        if self.topic:
            return self.topic.pop(0)

        return None
```

Its responsibility is:

```text
Topic → Receive event → Pass to AIOps processing
```

---

# 19. Final AIOps Processor

Example:

```python
def process_event(event):
    if event is None:
        return "No event"

    if event["severity"] == "critical":
        return (
            f"ALERT: {event['metric']} anomaly detected "
            f"with value {event['value']}"
        )

    return "Event processed"
```

Possible output:

```text
ALERT: cpu anomaly detected with value 95
```

---

# 20. Complete End-to-End Python Simulation

```python
CPU_THRESHOLD = 80


class Topic:
    def __init__(self):
        self.messages = []

    def publish(self, event):
        self.messages.append(event)

    def consume(self):
        if self.messages:
            return self.messages.pop(0)

        return None


class Producer:
    def __init__(self, topic):
        self.topic = topic

    def send(self, event):
        self.topic.publish(event)


class Consumer:
    def __init__(self, topic):
        self.topic = topic

    def receive(self):
        return self.topic.consume()


def detect_anomaly(cpu):
    return cpu > CPU_THRESHOLD


def generate_event(cpu):
    return {
        "type": "CPU_ANOMALY",
        "metric": "cpu",
        "value": cpu,
        "threshold": CPU_THRESHOLD,
        "severity": "critical"
    }


def process_event(event):
    return (
        f"AIOps ALERT: {event['metric']} = {event['value']} "
        f"exceeded threshold {event['threshold']}"
    )


def main():
    operational_data = {
        "cpu": 95
    }

    topic = Topic()
    producer = Producer(topic)
    consumer = Consumer(topic)

    cpu = operational_data["cpu"]

    print("Operational data:", operational_data)

    if detect_anomaly(cpu):
        print("Anomaly detected")

        event = generate_event(cpu)

        print("Generated event:", event)

        producer.send(event)

        print("Event published")

        received_event = consumer.receive()

        print("Consumer received:", received_event)

        output = process_event(received_event)

        print(output)

    else:
        print("System normal")


if __name__ == "__main__":
    main()
```

Expected conceptual output:

```text
Operational data: {'cpu': 95}
Anomaly detected
Generated event: {...}
Event published
Consumer received: {...}
AIOps ALERT: cpu = 95 exceeded threshold 80
```

---

# 21. CSV Operational Data

You may receive:

```csv
timestamp,cpu,memory,latency
10:00,45,50,110
10:01,52,55,125
10:02,95,61,700
```

Read:

```python
import csv

with open("data/metrics.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

Important:

CSV values are strings.

Convert:

```python
cpu = float(row["cpu"])
memory = float(row["memory"])
latency = float(row["latency"])
```

A common bug is:

```python
if row["cpu"] > 80:
```

because:

```python
row["cpu"]
```

may be:

```python
"95"
```

Correct:

```python
cpu = float(row["cpu"])

if cpu > 80:
    ...
```

---

# 22. JSON Operational Data

Example:

```json
[
  {
    "cpu": 45,
    "memory": 55
  },
  {
    "cpu": 95,
    "memory": 68
  }
]
```

Read:

```python
import json

with open("data/operational_data.json") as file:
    data = json.load(file)

print(data)
```

---

# 23. Python Skills You Must Know

Dictionary:

```python
metric = {
    "cpu": 92,
    "memory": 60
}

print(metric["cpu"])
```

List:

```python
values = [45, 50, 92]

for value in values:
    print(value)
```

Condition:

```python
if cpu > 80:
    print("anomaly")
else:
    print("normal")
```

Function:

```python
def detect(cpu):
    return cpu > 80
```

Class:

```python
class Producer:
    def __init__(self, topic):
        self.topic = topic

    def send(self, event):
        self.topic.append(event)
```

Exception handling:

```python
try:
    cpu = float(value)
except ValueError:
    print("Invalid CPU value")
```

---

# 24. Virtual Environment

If required:

```bash
python3 -m venv .venv
```

Activate in Codespaces/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Check:

```bash
pip list
```

Remember:

```text
Codespaces = Linux
```

So use:

```bash
source .venv/bin/activate
```

---

# 25. Run the Workflow Before Fixing Anything

Run the program before editing:

```bash
python main.py
```

Observe:

```text
What works?
Where does it fail?
What output should appear?
What output actually appears?
```

Do not make random changes first.

---

# 26. Run Tests Before Editing

Run:

```bash
pytest
```

or:

```bash
pytest -q
```

Verbose:

```bash
pytest -v
```

Stop on first failure:

```bash
pytest -x -v
```

This tells you:

```text
what currently fails
which component is affected
what behaviour is expected
```

---

# 27. Tests Are Documentation

Inspect:

```bash
ls tests
```

Then:

```bash
cat tests/test_workflow.py
```

Example:

```python
def test_high_cpu_is_anomaly():
    assert detect_anomaly(95) is True
```

This tells you:

```text
95 must be classified as anomalous.
```

Example:

```python
def test_event_type():
    event = generate_event(95)

    assert event["type"] == "CPU_ANOMALY"
```

This tells you the required event schema.

---

# 28. Common Debugging Bug — Wrong Threshold

Wrong:

```python
CPU_THRESHOLD = 800
```

Correct:

```python
CPU_THRESHOLD = 80
```

---

# 29. Common Bug — Reversed Comparison

Wrong:

```python
def detect_anomaly(cpu):
    return cpu < 80
```

Correct:

```python
def detect_anomaly(cpu):
    return cpu > 80
```

---

# 30. Common Bug — Wrong Key

Data:

```python
{
    "cpu": 95
}
```

Wrong:

```python
cpu = data["cpu_usage"]
```

Correct:

```python
cpu = data["cpu"]
```

---

# 31. Common Bug — Wrong Metric

Wrong:

```python
memory = data["cpu"]
```

Correct:

```python
memory = data["memory"]
```

---

# 32. Common Bug — Missing Return

Wrong:

```python
def generate_event(cpu):
    event = {
        "metric": "cpu",
        "value": cpu
    }
```

This returns `None`.

Correct:

```python
def generate_event(cpu):
    event = {
        "metric": "cpu",
        "value": cpu
    }

    return event
```

---

# 33. Common Bug — Topic Mismatch

Producer:

```python
producer.send("alerts", event)
```

Consumer:

```python
consumer.receive("alert")
```

Mismatch:

```text
alerts != alert
```

Both sides must use the same topic/channel.

---

# 34. Common Bug — Event Key Mismatch

Event:

```python
event = {
    "metric": "cpu",
    "value": 95
}
```

Wrong:

```python
print(event["metric_value"])
```

Correct:

```python
print(event["value"])
```

---

# 35. Common Bug — String vs Number

Wrong:

```python
cpu = row["cpu"]

if cpu > 80:
    ...
```

Correct:

```python
cpu = float(row["cpu"])

if cpu > 80:
    ...
```

---

# 36. Common Bug — Consumer Not Called

Wrong:

```python
producer.send(event)

print("Done")
```

Missing:

```python
received = consumer.receive()
```

---

# 37. Common Bug — Reversed Empty Check

Wrong:

```python
if not self.messages:
    return self.messages.pop(0)
```

Correct:

```python
if self.messages:
    return self.messages.pop(0)
```

---

# 38. Common Bug — Severity Mismatch

Generated:

```python
"severity": "critical"
```

Processor checks:

```python
if event["severity"] == "HIGH":
```

Mismatch.

Make processor match the expected schema.

---

# 39. Best Debugging Strategy

Trace the pipeline:

```text
Operational Data
      ↓
Anomaly Detection
      ↓
Event Generation
      ↓
Producer
      ↓
Topic
      ↓
Consumer
      ↓
AIOps Output
```

At every step ask:

> Is the expected value still correct here?

The **first stage where the value becomes wrong** is where you investigate.

---

# 40. Temporary Debug Prints

Use temporary print statements:

```python
print("Operational data:", data)
print("Anomaly result:", anomaly)
print("Generated event:", event)
print("Producer sending:", event)
print("Topic contents:", topic)
print("Consumer received:", received)
print("AIOps output:", output)
```

Remove unnecessary debug prints before final submission.

---

# 41. Debug Trace Example

Suppose:

```text
Operational Data ✅
Anomaly Detection ✅
Event Generation ✅
Producer ✅
Topic ✅
Consumer ❌
AIOps Output ❌
```

Investigate:

```text
Topic ↔ Consumer
```

Possible problems:

```text
wrong channel name
incorrect consume method
reversed empty check
incorrect object reference
event removed too early
```

---

# 42. Do Not Rewrite the Architecture

The official instructions explicitly say not to replace the provided architecture unnecessarily.

Bad:

```text
Replace simulated topic with Kafka.
Add Redis.
Add FastAPI.
Create Docker setup.
Rewrite entire project.
```

Good:

```text
Identify the actual bug.
Fix only necessary lines.
Preserve file structure.
Preserve expected function names.
Keep tests compatible.
```

---

# 43. Hidden Tests

Do not hardcode visible cases.

Bad:

```python
def detect(cpu):
    return cpu == 95
```

Correct:

```python
def detect(cpu):
    return cpu > CPU_THRESHOLD
```

Hidden tests might use:

```text
81
90
100
40
79
```

---

# 44. Edge Cases

If:

```python
CPU_THRESHOLD = 80
```

Check whether the requirement is:

```python
cpu > 80
```

or:

```python
cpu >= 80
```

Difference:

```text
> 80  → 80 is normal
>= 80 → 80 is anomaly
```

Use tests/instructions to decide.

---

# 45. Syntax Validation

Whole project:

```bash
python -m compileall .
```

Specific file:

```bash
python -m py_compile anomaly_detector.py
```

---

# 46. Test Commands

All:

```bash
pytest -q
```

Verbose:

```bash
pytest -v
```

Stop after first failure:

```bash
pytest -x -v
```

Specific file:

```bash
pytest tests/test_anomaly_detector.py -v
```

Specific test:

```bash
pytest tests/test_anomaly_detector.py::test_high_cpu -v
```

---

# 47. Validation Order After a Fix

Use this order:

```text
1. Run targeted failing test
2. Run full tests
3. Run complete workflow
4. Verify final output
5. Review git diff
```

Commands:

```bash
pytest tests/test_anomaly_detector.py -v
pytest -q
python main.py
git diff
```

---

# 48. Useful Linux Commands

```bash
pwd
ls
ls -la
cd folder
cd ..
cat file.py
```

Search:

```bash
grep "threshold" detector.py
```

Recursive:

```bash
grep -R "threshold" .
grep -R "producer" .
grep -R "consumer" .
grep -R "__main__" .
```

---

# 49. Git Workflow

Before changes:

```bash
git status
```

After changes:

```bash
git diff
git status
```

Stage:

```bash
git add .
```

Commit:

```bash
git commit -m "Fix AIOps workflow and document validation"
```

Push:

```bash
git push
```

---

# 50. Fork Workflow

The instructions say to push to your GitHub fork.

Typical flow:

```text
Instructor Repository
        ↓
      Fork
        ↓
Your GitHub Repository
        ↓
   GitHub Codespace
        ↓
      Changes
        ↓
      Commit
        ↓
       Push
```

Check:

```bash
git remote -v
```

Usually:

```text
origin → your fork
```

There may also be:

```text
upstream → original/instructor repository
```

---

# 51. Branch Workflow

If required:

```bash
git switch -c mse-solution
```

Then:

```bash
git add .
git commit -m "Complete AIOps practical assessment"
git push -u origin mse-solution
```

---

# 52. Pull Request

After pushing:

```text
GitHub
  ↓
Your Fork
  ↓
Pull Requests
  ↓
New Pull Request
```

Follow the exact exam instruction for:

```text
base repository
base branch
compare branch
```

Do not assume if they specify it.

---

# 53. Example PR Description

```markdown
## Summary

Completed the AIOps practical assessment.

### Work Completed

- Analysed operational metrics and logs
- Identified anomalous behaviour
- Traced the event flow
- Located the affected component
- Identified the root cause
- Applied the required correction
- Validated the complete workflow
- Ran the provided tests
- Updated the README with observations and reproduction steps

### Validation

- End-to-end workflow completed successfully
- Provided tests pass
- Final AIOps output verified
```

---

# 54. README Structure You Should Use in the Exam

Your submitted repository README should include:

```markdown
# AIOps MSE Assessment

## 1. Project Overview

## 2. Repository Structure

## 3. Architecture

## 4. Operational Data Analysis

## 5. Metrics and Logs

## 6. Observations

## 7. Issues Identified

## 8. Root Cause Analysis

## 9. Corrections Made

## 10. End-to-End Workflow Result

## 11. Validation / Test Results

## 12. Reproduction Steps

## 13. Final Output

## 14. Screenshots / Evidence
```

---

# 55. README — Project Overview Example

```markdown
## Project Overview

This project simulates an end-to-end AIOps event processing workflow.

Operational metrics and logs are analysed to identify abnormal
behaviour. When an anomaly is detected, a structured event is
generated. The event is published through a simulated producer/topic
mechanism and consumed by the event consumer. The final AIOps
processing stage generates the required output or alert.
```

---

# 56. README — Repository Structure Example

```text
.
├── data/
│   ├── metrics.csv
│   └── logs.txt
├── anomaly_detector.py
├── event_generator.py
├── producer.py
├── topic.py
├── consumer.py
├── aiops_processor.py
├── main.py
├── tests/
├── requirements.txt
└── README.md
```

Replace this with the actual repository tree.

---

# 57. README — Architecture Example

```text
Operational Data
      ↓
Anomaly Detector
      ↓
Event Generator
      ↓
Producer
      ↓
Simulated Topic
      ↓
Consumer
      ↓
AIOps Processor
```

---

# 58. README — Operational Data Analysis Example

```markdown
## Operational Data Analysis

The supplied operational data contains system metrics including CPU,
memory and request latency.

Most metric values remain within the configured operating range.

One CPU observation exceeds the configured anomaly threshold and
therefore triggers the event-processing workflow.
```

---

# 59. README — Observations Example

```markdown
## Observations

- CPU values below the configured threshold are classified as normal.
- CPU values above the configured threshold are classified as anomalies.
- The anomaly detector produces the expected anomaly state.
- An anomaly is converted into a structured event.
- The producer publishes the generated event to the simulated topic.
- The consumer retrieves the event.
- The final AIOps processor generates the expected alert.
```

---

# 60. README — Issue Example

```markdown
## Issue Identified

The producer and consumer were configured with different topic names.

The producer published anomaly events to:

`system-events`

while the consumer attempted to read from:

`system-event`

Because the topic names differed, events generated by the producer
were not reaching the consumer.
```

---

# 61. README — Root Cause Example

```markdown
## Root Cause

The root cause was inconsistent topic configuration between the
producer and consumer components.

The operational data, anomaly detector and event generator were
working correctly, but the topic mismatch interrupted the event flow
before the consumer stage.
```

---

# 62. README — Correction Example

```markdown
## Correction

The consumer topic configuration was changed from:

`system-event`

to:

`system-events`

This ensures the producer and consumer use the same simulated event
channel.
```

---

# 63. README — Validation Example

```markdown
## Validation

After applying the correction:

1. Operational data was loaded successfully.
2. The anomalous metric was detected.
3. The anomaly event was generated.
4. The producer published the event.
5. The consumer received the event.
6. The final AIOps processor produced the expected output.
7. All provided tests passed.
```

---

# 64. README — Test Result Example

Command:

```bash
pytest -q
```

Example result:

```text
8 passed
```

Use your actual result in the exam.

---

# 65. README — Reproduction Steps Example

```markdown
## Reproduction Steps

1. Open the repository using GitHub Codespaces.

2. Create a virtual environment if required:

   `python3 -m venv .venv`

3. Activate it:

   `source .venv/bin/activate`

4. Install dependencies:

   `pip install -r requirements.txt`

5. Run tests:

   `pytest -q`

6. Run the workflow:

   `python main.py`

7. Verify:
   - operational data loads
   - anomaly is detected
   - event is generated
   - producer publishes event
   - consumer receives event
   - final AIOps output appears
```

---

# 66. Screenshots / Evidence

The exam explicitly asks for evidence.

Useful screenshots:

```text
1. Repository opened in Codespaces
2. Initial failing workflow/test
3. Relevant buggy component
4. Corrected code
5. Passing test suite
6. Successful end-to-end output
7. Git commit/push
8. Pull Request
```

Every screenshot should prove something.

---

# 67. Before Submission Checklist

Run:

```bash
git status
git diff
pytest -q
python main.py
```

Then verify README.

Then:

```bash
git add .
git commit -m "Complete AIOps MSE practical assessment"
git push
```

Then:

```text
Create required PR
Capture PR evidence
Copy repository URL
Submit URL as instructed
```

---

# 68. Do Not Commit Junk

Watch for:

```text
.venv/
__pycache__/
.pytest_cache/
*.pyc
```

Typical `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
.pytest_cache/
```

Always check:

```bash
git status
```

---

# 69. Full Exam Workflow

```text
STEP 1
Read all instructions.

STEP 2
Open Codespace.

STEP 3
Run:
pwd
ls -la
git status

STEP 4
Read README.

STEP 5
Inspect repository tree.

STEP 6
Find the entry point.

STEP 7
Identify:
operational data
metrics
logs
anomaly detector
event generator
producer
topic
consumer
AIOps processor

STEP 8
Read tests.

STEP 9
Run tests before changing code.

STEP 10
Run complete workflow before changing code.

STEP 11
Observe failure.

STEP 12
Trace data stage-by-stage.

STEP 13
Identify first incorrect stage.

STEP 14
Find root cause.

STEP 15
Make minimum required correction.

STEP 16
Run targeted test.

STEP 17
Run all tests.

STEP 18
Run full workflow.

STEP 19
Verify final AIOps output.

STEP 20
Capture screenshots/evidence.

STEP 21
Update README.

STEP 22
Run git diff.

STEP 23
Run git status.

STEP 24
Commit.

STEP 25
Push to fork.

STEP 26
Create Pull Request.

STEP 27
Submit repository URL.
```

---

# 70. Commands to Memorize

```bash
# Repository inspection

pwd
ls -la
find . -maxdepth 2 -type f

cat README.md
cat requirements.txt


# Git

git status
git branch
git remote -v
git log --oneline -5
git diff


# Search

grep -R "__main__" .
grep -R "threshold" .
grep -R "producer" .
grep -R "consumer" .


# Environment

python3 --version
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


# Run

python main.py


# Syntax

python -m compileall .


# Tests

pytest -q
pytest -v
pytest -x -v


# Final Git

git status
git diff
git add .
git commit -m "Complete AIOps MSE practical assessment"
git push
```

---

# 71. Debugging Cheat Sheet

```text
READ ERROR
   ↓
CHECK OPERATIONAL DATA
   ↓
CHECK DETECTOR
   ↓
CHECK GENERATED EVENT
   ↓
CHECK PRODUCER
   ↓
CHECK TOPIC
   ↓
CHECK CONSUMER
   ↓
CHECK FINAL OUTPUT
```

Always ask:

> Where is the first point at which the actual value differs from the expected value?

That is where you investigate.

---

# 72. What NOT to Study Heavily Now

Based on the final exam instructions, these are low priority:

```text
Installing Kafka
Starting Kafka brokers
ZooKeeper
KRaft
Docker Kafka
Installing Airflow
Airflow scheduler
Airflow webserver
Airflow DAG setup
AWS
GCP
Kubernetes
Production cloud deployment
```

You still need to understand the concepts:

```text
Producer
Topic
Consumer
```

but not real infrastructure setup.

---

# 73. What to Study Heavily

High priority:

```text
Python functions
Python classes
lists
dictionaries
conditions
loops
CSV
JSON
file reading
exceptions
pytest
Git
GitHub
repo navigation
debugging
metrics
logs
thresholds
events
producer/topic/consumer
root cause analysis
README documentation
Pull Requests
```

---

# 74. Fast Concept Revision

Operational Data:

```text
Metrics + logs describing system behaviour.
```

Metric:

```text
Numeric measurement.
```

Example:

```text
CPU = 92%
```

Log:

```text
Textual record.
```

Example:

```text
ERROR database unavailable
```

Anomaly:

```text
Behaviour outside the expected range.
```

Event:

```text
Structured representation of something that happened.
```

Producer:

```text
Publishes event.
```

Topic:

```text
Event channel.
```

Consumer:

```text
Receives event.
```

AIOps Output:

```text
Alert / recommendation / incident / final processed result.
```

---

# 75. Strong Viva Answer — Explain the Project

You can say:

> The project simulates an end-to-end AIOps event-processing workflow. Operational metrics and logs are first analysed for unusual behaviour. When an anomaly is detected, the system converts it into a structured event. A producer publishes that event to a simulated topic, a consumer retrieves it, and the final AIOps processor generates the required alert or output. During the assessment, I traced this flow, identified the faulty component, applied a minimal correction, reran the tests, verified the complete workflow and documented the result.

---

# 76. Strong Viva Answer — Why No Real Kafka?

> The assessment uses a Python simulation of an event-driven AIOps architecture. The producer, topic and consumer reproduce the logical behaviour of Kafka-style components without requiring an actual Kafka broker or external infrastructure.

---

# 77. Strong Viva Answer — How Did You Debug?

> I traced the data sequentially through operational data, anomaly detection, event generation, producer, topic, consumer and final AIOps processing. I found the first stage where the actual result differed from the expected result, isolated the root cause, made a minimal correction and then validated it using targeted tests, the complete test suite and the end-to-end workflow.

---

# 78. Strong Viva Answer — Why Minimal Fix?

> The assessment requires working within the existing project architecture. I therefore changed only the affected logic, which reduces regression risk and keeps the solution compatible with the provided tests and project structure.

---

# 79. Strong Viva Answer — Why Run Tests?

> The tests define expected component behaviour and help confirm that the correction fixes the intended issue without breaking other parts of the workflow. I first ran the relevant targeted test and then the complete test suite.

---

# 80. Ultra-Short Last-Minute Cheat Sheet

```text
ARCHITECTURE:

Operational Data
→ Anomaly Detection
→ Event Generation
→ Producer
→ Topic
→ Consumer
→ AIOps Output


FIRST:

pwd
ls -la
git status
cat README.md
find . -maxdepth 2 -type f


UNDERSTAND:

input
logic
output
next component


RUN:

pytest -q
python main.py


DEBUG:

data
detector
event
producer
topic
consumer
output


FIX:

minimal change


VERIFY:

targeted test
full tests
full workflow


DOCUMENT:

observations
issue
root cause
correction
result
reproduction


SUBMIT:

git diff
git status
git add .
git commit
git push
PR
repository URL
screenshots
```

---

# 81. Final Mental Model

You are not being tested on whether you can build a production Kafka or Airflow cluster.

You are being tested on whether you can reason correctly about an existing AIOps codebase.

Remember:

```text
Understand Repository
        ↓
Understand Operational Data
        ↓
Identify Normal / Abnormal Behaviour
        ↓
Trace Event Generation
        ↓
Trace Producer / Topic / Consumer
        ↓
Observe Failure
        ↓
Locate Affected Component
        ↓
Find Root Cause
        ↓
Apply Minimal Fix
        ↓
Run Tests
        ↓
Run Complete Pipeline
        ↓
Verify AIOps Output
        ↓
Document Everything
        ↓
Commit
        ↓
Push to Fork
        ↓
Create PR
        ↓
Submit Evidence
```

If you can confidently follow this sequence, you are prepared for the MSE.
