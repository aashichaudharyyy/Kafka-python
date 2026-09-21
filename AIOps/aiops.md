# AIOps Practical Exam — Complete Hands-On Guide

This README is designed as a **single exam-preparation reference** for a practical AIOps exam involving:

- GitHub Codespaces
- Git and GitHub
- Python virtual environments
- Apache Kafka
- Kafka producers, consumers, topics, offsets, partitions, and consumer groups
- Apache Airflow
- DAGs, tasks, operators, scheduler, executor, XCom, catchup, and scheduling
- GitHub Actions
- GitHub repository administration
- AIOps-style statistics and anomaly detection
- Debugging and troubleshooting
- Step-by-step exam workflow
- Commands you should memorize

---

# 1. Likely Exam Pattern

The exam may work like this:

```text
Open exam portal
      ↓
Open GitHub repository / Codespace
      ↓
Read Task 1
      ↓
Make required change
      ↓
Run / test / verify
      ↓
git add
git commit
git push
      ↓
Portal validates task
      ↓
Next task unlocks
      ↓
Repeat
```

The safest mindset is:

```text
READ → DO → VERIFY → COMMIT → PUSH → CONTINUE
```

Do not complete many tasks and commit everything once if the exam expects one commit per task.

---

# 2. First Commands to Run in Codespaces

Whenever the Codespace opens, first inspect the environment.

```bash
pwd
ls
ls -la
git status
git branch
python3 --version
pip3 --version
```

Useful repository inspection commands:

```bash
find . -maxdepth 2 -type f
```

Read instructions:

```bash
cat README.md
```

Check recent commits:

```bash
git log --oneline -10
```

Check current changes:

```bash
git diff
```

Check configured Git remote:

```bash
git remote -v
```

---

# 3. Essential Linux Commands

GitHub Codespaces normally uses Linux.

## List files

```bash
ls
```

Detailed list:

```bash
ls -la
```

## Current directory

```bash
pwd
```

## Change directory

```bash
cd folder_name
```

Go one directory back:

```bash
cd ..
```

Go home:

```bash
cd ~
```

## Create directory

```bash
mkdir test
```

## Create empty file

```bash
touch example.py
```

## Read file

```bash
cat example.py
```

## Copy

```bash
cp source.txt destination.txt
```

## Move / rename

```bash
mv old.txt new.txt
```

## Delete file

```bash
rm file.txt
```

## Delete directory

```bash
rm -rf folder_name
```

Use `rm -rf` carefully.

## Search text

```bash
grep "Kafka" README.md
```

Recursive search:

```bash
grep -R "Kafka" .
```

## Running process search

```bash
ps aux
```

Search Kafka:

```bash
ps aux | grep kafka
```

Search Airflow:

```bash
ps aux | grep airflow
```

---

# 4. Git — Commands You Must Know

## Check repository status

```bash
git status
```

## See differences

```bash
git diff
```

## Stage everything

```bash
git add .
```

Stage one file:

```bash
git add producer.py
```

## Commit

```bash
git commit -m "completed kafka producer"
```

## Push

```bash
git push
```

If upstream is not configured:

```bash
git push -u origin main
```

Or:

```bash
git push -u origin <branch-name>
```

## Pull

```bash
git pull
```

## Show branches

```bash
git branch
```

## Create and switch branch

```bash
git switch -c feature-name
```

Older equivalent:

```bash
git checkout -b feature-name
```

## Switch branch

```bash
git switch main
```

## Recent commits

```bash
git log --oneline
```

Last 5:

```bash
git log --oneline -5
```

## View remotes

```bash
git remote -v
```

## Git identity

If Git asks for username/email:

```bash
git config user.name "Your Name"
git config user.email "your@email.com"
```

Check:

```bash
git config --list
```

---

# 5. Standard Exam Git Workflow

For every task:

```bash
git status
```

Make changes.

Then verify:

```bash
git diff
```

Stage:

```bash
git add .
```

Commit:

```bash
git commit -m "task 1: setup environment"
```

Push:

```bash
git push
```

Confirm:

```bash
git status
git log --oneline -3
```

---

# 6. Python Virtual Environment

Codespaces is Linux, so remember Linux commands.

## Create venv

```bash
python3 -m venv .venv
```

## Activate venv

```bash
source .venv/bin/activate
```

You should see:

```text
(.venv) user ➜ /workspaces/project
```

## Upgrade pip

```bash
python -m pip install --upgrade pip
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Install individual packages

```bash
pip install kafka-python
pip install apache-airflow
pip install pytest
```

## Show installed packages

```bash
pip list
```

## Save dependencies

```bash
pip freeze > requirements.txt
```

## Deactivate

```bash
deactivate
```

---

# 7. Windows vs Codespaces venv

Codespaces/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For a GitHub Codespaces exam, memorize the Linux command.

---

# 8. Kafka — Core Concepts

Kafka is an event-streaming system.

Basic architecture:

```text
Producer
   ↓
Kafka Broker
   ↓
Topic
   ↓
Partition
   ↓
Consumer
```

A possible AIOps project:

```text
producer.py
     ↓
sensor-data topic
     ↓
Kafka
     ↓
consumer.py
     ↓
stats.py
     ↓
detection.py
```

---

# 9. Important Kafka Terms

## Broker

Kafka server.

Example:

```text
localhost:9092
```

## Topic

A named stream of messages.

Examples:

```text
sensor-data
machine-metrics
cpu-metrics
alerts
```

## Producer

Sends data to Kafka.

## Consumer

Reads data from Kafka.

## Partition

A topic can be divided into partitions.

Example:

```text
metrics topic

partition 0
partition 1
partition 2
```

Partitions allow parallel processing.

## Offset

Position of a message inside a partition.

Example:

```text
offset 0
offset 1
offset 2
offset 3
```

## Consumer Group

Multiple consumers can work together.

Example:

```text
Topic Partition 0 → Consumer A
Topic Partition 1 → Consumer B
Topic Partition 2 → Consumer C
```

Consumers in the same group divide the partitions among themselves.

## Replication

Copies of Kafka partitions stored on multiple brokers.

## Bootstrap Server

Initial Kafka broker address.

Typical:

```text
localhost:9092
```

---

# 10. Starting Kafka

Always inspect the repository first:

```bash
ls -la
```

If you see:

```text
docker-compose.yml
```

or:

```text
compose.yaml
```

the expected startup may be:

```bash
docker compose up -d
```

Check status:

```bash
docker compose ps
```

Show logs:

```bash
docker compose logs
```

Follow logs continuously:

```bash
docker compose logs -f
```

Stop:

```bash
docker compose down
```

---

# 11. Kafka Script-Based Startup

If Kafka is locally extracted and configured:

```bash
bin/kafka-server-start.sh config/server.properties
```

Depending on Kafka/course version, older material may include ZooKeeper.

Example older commands:

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

Then:

```bash
bin/kafka-server-start.sh config/server.properties
```

However, modern Kafka commonly uses KRaft.

For the exam, follow the repository/instructor-provided setup.

---

# 12. Kafka Topic Commands

## Create topic

```bash
bin/kafka-topics.sh \
  --create \
  --topic sensor-data \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1
```

Simpler form:

```bash
bin/kafka-topics.sh \
  --create \
  --topic sensor-data \
  --bootstrap-server localhost:9092
```

## List topics

```bash
bin/kafka-topics.sh \
  --list \
  --bootstrap-server localhost:9092
```

## Describe topic

```bash
bin/kafka-topics.sh \
  --describe \
  --topic sensor-data \
  --bootstrap-server localhost:9092
```

## Delete topic

```bash
bin/kafka-topics.sh \
  --delete \
  --topic sensor-data \
  --bootstrap-server localhost:9092
```

Remember:

```text
CREATE → LIST → DESCRIBE → PRODUCE → CONSUME
```

---

# 13. Kafka Console Producer

Start producer:

```bash
bin/kafka-console-producer.sh \
  --topic sensor-data \
  --bootstrap-server localhost:9092
```

Then type:

```text
10
20
35
50
```

Each line is one message.

---

# 14. Kafka Console Consumer

In another terminal:

```bash
bin/kafka-console-consumer.sh \
  --topic sensor-data \
  --bootstrap-server localhost:9092 \
  --from-beginning
```

`--from-beginning` means read existing messages from the beginning of the topic.

Without it, you may only see newly arriving messages.

---

# 15. Kafka Producer in Python

Install library:

```bash
pip install kafka-python
```

Example `producer.py`:

```python
import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

data = {
    "machine_id": "M1",
    "temperature": 45,
    "vibration": 2.3,
    "cpu": 63
}

producer.send("sensor-data", value=data)

producer.flush()

print("Message sent successfully")
```

Important pieces:

```python
KafkaProducer
bootstrap_servers
value_serializer
producer.send()
producer.flush()
```

---

# 16. Continuous Kafka Producer Example

```python
import json
import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

while True:
    data = {
        "machine_id": "M1",
        "temperature": random.randint(30, 100),
        "vibration": round(random.uniform(0.5, 5.0), 2),
        "cpu": random.randint(10, 100)
    }

    producer.send("sensor-data", value=data)

    print("Sent:", data)

    time.sleep(2)
```

Stop using:

```text
Ctrl + C
```

---

# 17. Kafka Consumer in Python

Example `consumer.py`:

```python
import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="aiops-group",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)

print("Waiting for messages...")

for message in consumer:
    print(message.value)
```

Important fields:

```python
KafkaConsumer
bootstrap_servers
auto_offset_reset
group_id
value_deserializer
message.value
```

---

# 18. auto_offset_reset

Common values:

```text
earliest
latest
```

## earliest

Read from earliest available offset when no committed offset exists.

```python
auto_offset_reset="earliest"
```

## latest

Only consume newer messages when there is no existing offset.

```python
auto_offset_reset="latest"
```

---

# 19. Kafka Consumer Group Example

```python
consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers="localhost:9092",
    group_id="analytics-group",
    auto_offset_reset="earliest"
)
```

If several consumers use:

```text
analytics-group
```

Kafka distributes partitions between them.

---

# 20. Kafka Topic Creation Using Python

Example `topic.py`:

```python
from kafka.admin import KafkaAdminClient, NewTopic

admin = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id="aiops-admin"
)

topic = NewTopic(
    name="sensor-data",
    num_partitions=1,
    replication_factor=1
)

admin.create_topics(
    new_topics=[topic],
    validate_only=False
)

print("Topic created successfully")

admin.close()
```

Important:

```python
KafkaAdminClient
NewTopic
create_topics()
```

---

# 21. Safely Create Topic Only if Missing

```python
from kafka.admin import KafkaAdminClient, NewTopic

admin = KafkaAdminClient(
    bootstrap_servers="localhost:9092"
)

topic_name = "sensor-data"

existing_topics = admin.list_topics()

if topic_name not in existing_topics:
    topic = NewTopic(
        name=topic_name,
        num_partitions=1,
        replication_factor=1
    )

    admin.create_topics([topic])

    print("Topic created")
else:
    print("Topic already exists")

admin.close()
```

---

# 22. Kafka Topic Administration Commands

Describe consumer groups:

```bash
bin/kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --list
```

Describe specific group:

```bash
bin/kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --describe \
  --group aiops-group
```

This can show:

```text
CURRENT-OFFSET
LOG-END-OFFSET
LAG
```

---

# 23. Kafka Lag

Consumer lag roughly means:

```text
latest message offset - consumer processed offset
```

Example:

```text
Latest offset = 1000
Consumer offset = 920

Lag = 80
```

High lag can mean the consumer is too slow.

This is important in AIOps monitoring.

---

# 24. stats.py — Basic Statistics

Example:

```python
values = [10, 20, 30, 40, 50]

average = sum(values) / len(values)

minimum = min(values)

maximum = max(values)

print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)
```

---

# 25. stats.py Using statistics Module

```python
import statistics

values = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(values))
print("Median:", statistics.median(values))
print("Standard deviation:", statistics.stdev(values))
```

---

# 26. AIOps Statistics from Kafka Messages

Example:

```python
import json
import statistics
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="stats-group",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)

temperatures = []

for message in consumer:
    data = message.value

    temperature = data["temperature"]

    temperatures.append(temperature)

    if len(temperatures) >= 5:
        mean = statistics.mean(temperatures[-5:])

        print("Current:", temperature)
        print("Rolling mean:", mean)
```

---

# 27. detection.py — Threshold Detection

Simple anomaly detection:

```python
def detect_anomaly(cpu):
    if cpu > 90:
        return True
    return False


cpu = 95

if detect_anomaly(cpu):
    print("ALERT: High CPU detected")
else:
    print("CPU normal")
```

---

# 28. Temperature Detection Example

```python
def detect_temperature(temperature):
    threshold = 80

    if temperature > threshold:
        return "ANOMALY"

    return "NORMAL"


print(detect_temperature(95))
```

---

# 29. Z-Score Anomaly Detection

```python
import statistics

values = [45, 48, 50, 47, 49, 51, 46]

mean = statistics.mean(values)
std = statistics.stdev(values)

new_value = 90

z_score = abs((new_value - mean) / std)

print("Mean:", mean)
print("Std:", std)
print("Z-score:", z_score)

if z_score > 3:
    print("Anomaly detected")
else:
    print("Normal")
```

Concept:

```text
z-score > 3
```

is often used as a simple anomaly threshold.

---

# 30. Full Kafka + Detection Example

```python
import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="detection-group",
    value_deserializer=lambda value: json.loads(value.decode("utf-8"))
)

for message in consumer:
    data = message.value

    temperature = data["temperature"]

    print("Received:", data)

    if temperature > 80:
        print("ALERT: Temperature anomaly detected")
    else:
        print("Temperature normal")
```

---

# 31. AIOps Pipeline Mental Model

```text
Application / Sensors
        ↓
     Producer
        ↓
      Kafka
        ↓
      Topic
        ↓
     Consumer
        ↓
 Statistics / Aggregation
        ↓
 Anomaly Detection
        ↓
 Alert / Action
```

Airflow can orchestrate scheduled jobs around this pipeline.

---

# 32. Kafka Troubleshooting

## Error

```text
NoBrokersAvailable
```

Possible causes:

- Kafka not running
- Wrong host
- Wrong port
- Container failed
- Networking issue

Check:

```bash
docker compose ps
```

Logs:

```bash
docker compose logs
```

Check port:

```bash
ss -ltnp | grep 9092
```

---

# 33. Topic Does Not Exist

Check topics:

```bash
bin/kafka-topics.sh \
  --list \
  --bootstrap-server localhost:9092
```

Create it if necessary.

---

# 34. ModuleNotFoundError: kafka

Example:

```text
ModuleNotFoundError: No module named 'kafka'
```

Fix:

```bash
source .venv/bin/activate
pip install kafka-python
```

Check:

```bash
pip show kafka-python
```

---

# 35. Airflow — Core Concept

Apache Airflow is a workflow orchestration system.

Architecture:

```text
                  DAG Files
                     ↓
               DAG Processor
                     ↓
                  Scheduler
                     ↓
                  Executor
                     ↓
                   Tasks

                     ↕
              Metadata Database

                     ↕
                Airflow UI
```

---

# 36. Important Airflow Terms

## DAG

Directed Acyclic Graph.

Defines a workflow.

Example:

```text
extract → transform → train → evaluate
```

## Task

One unit of work.

Examples:

```text
download data
clean data
train model
send alert
```

## Operator

Template for performing an operation.

Examples:

```text
PythonOperator
BashOperator
EmptyOperator
```

## Scheduler

Determines when DAG/task instances should run.

## Executor

Controls how tasks are executed.

## Metadata Database

Stores:

- DAG run state
- task state
- users
- connections
- schedules
- execution metadata

## XCom

Small values passed between tasks.

## Triggerer

Handles deferred/asynchronous tasks.

## DAG Processor

Parses DAG definitions.

---

# 37. Check Airflow Version

Always do:

```bash
airflow version
```

This matters because Airflow 2 and 3 differ in some commands.

---

# 38. Airflow Quick Local Startup

A common development command:

```bash
airflow standalone
```

This sets up a simple local Airflow instance.

Airflow normally uses port:

```text
8080
```

So UI is typically:

```text
http://localhost:8080
```

In Codespaces, the port may be forwarded automatically.

---

# 39. Airflow 3.x Manual Components

You may see:

```bash
airflow db migrate
```

Then:

```bash
airflow api-server --port 8080
```

Another terminal:

```bash
airflow scheduler
```

Another:

```bash
airflow dag-processor
```

Another, when required:

```bash
airflow triggerer
```

---

# 40. Airflow 2.x Course Commands

Older course material may use:

```bash
airflow db init
```

or:

```bash
airflow db migrate
```

Start webserver:

```bash
airflow webserver --port 8080
```

Start scheduler:

```bash
airflow scheduler
```

In an exam, use the commands expected by the installed Airflow version and course instructions.

---

# 41. AIRFLOW_HOME

Set manually:

```bash
export AIRFLOW_HOME=~/airflow
```

Check:

```bash
echo $AIRFLOW_HOME
```

Typical DAG directory:

```bash
$AIRFLOW_HOME/dags
```

List DAG files:

```bash
ls $AIRFLOW_HOME/dags
```

---

# 42. First Airflow DAG

Example:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def extract():
    print("Extracting data")


def process():
    print("Processing data")


def detect():
    print("Detecting anomalies")


with DAG(
    dag_id="aiops_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    task2 = PythonOperator(
        task_id="process",
        python_callable=process
    )

    task3 = PythonOperator(
        task_id="detect",
        python_callable=detect
    )

    task1 >> task2 >> task3
```

Dependency:

```python
task1 >> task2 >> task3
```

means:

```text
task1
  ↓
task2
  ↓
task3
```

---

# 43. BashOperator Example

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id="bash_example",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    print_date = BashOperator(
        task_id="print_date",
        bash_command="date"
    )

    list_files = BashOperator(
        task_id="list_files",
        bash_command="ls -la"
    )

    print_date >> list_files
```

---

# 44. Airflow Scheduling

## Manual only

```python
schedule=None
```

## Hourly

```python
schedule="@hourly"
```

## Daily

```python
schedule="@daily"
```

## Weekly

```python
schedule="@weekly"
```

## Cron

Every hour:

```python
schedule="0 * * * *"
```

Every day at midnight:

```python
schedule="0 0 * * *"
```

Every 5 minutes:

```python
schedule="*/5 * * * *"
```

---

# 45. Cron Format

```text
* * * * *
│ │ │ │ │
│ │ │ │ └── day of week
│ │ │ └──── month
│ │ └────── day of month
│ └──────── hour
└────────── minute
```

Examples:

```text
0 * * * *
```

Hourly.

```text
0 0 * * *
```

Daily at 00:00.

```text
*/5 * * * *
```

Every 5 minutes.

---

# 46. catchup=False

```python
catchup=False
```

means Airflow does not automatically create historical runs for old schedule intervals.

Example:

If a DAG started on January 1 but is enabled on January 10:

- `catchup=True` may create missed historical runs.
- `catchup=False` normally avoids those historical catch-up runs.

---

# 47. Airflow CLI Commands

## List DAGs

```bash
airflow dags list
```

## Show import errors

```bash
airflow dags list-import-errors
```

This is one of the most useful debugging commands.

## List tasks

```bash
airflow tasks list aiops_pipeline
```

## Trigger DAG

```bash
airflow dags trigger aiops_pipeline
```

## Pause DAG

```bash
airflow dags pause aiops_pipeline
```

## Unpause DAG

```bash
airflow dags unpause aiops_pipeline
```

## Test task

```bash
airflow tasks test aiops_pipeline extract 2026-09-21
```

---

# 48. XCom

XCom allows tasks to exchange small values.

Example TaskFlow API:

```python
from airflow.decorators import dag, task
from datetime import datetime


@dag(
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
)
def xcom_example():

    @task
    def calculate_accuracy():
        return 0.92

    @task
    def evaluate(accuracy):
        print("Accuracy:", accuracy)

    accuracy = calculate_accuracy()

    evaluate(accuracy)


xcom_example()
```

Concept:

```text
Task A
  ↓
returns 0.92
  ↓
XCom
  ↓
Task B receives 0.92
```

Avoid using XCom for huge files/datasets.

---

# 49. Airflow Task States

Common task states:

```text
queued
running
success
failed
skipped
upstream_failed
retrying
```

---

# 50. Airflow Retry Example

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


def process():
    print("Running process")


default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=1)
}


with DAG(
    dag_id="retry_example",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args
) as dag:

    task = PythonOperator(
        task_id="process",
        python_callable=process
    )
```

---

# 51. Airflow Depends On Past

```python
depends_on_past=True
```

A task run can depend on the previous scheduled instance succeeding.

---

# 52. Airflow Backfill

Backfill means running workflows for previous historical periods.

This is related to:

```text
start_date
schedule
catchup
historical DAG runs
```

---

# 53. Airflow Debugging

If a DAG does not appear:

```bash
airflow dags list
```

Then:

```bash
airflow dags list-import-errors
```

Also run Python syntax check:

```bash
python -m py_compile dags/my_dag.py
```

Check Airflow processes:

```bash
ps aux | grep airflow
```

Check UI port:

```bash
ss -ltnp | grep 8080
```

---

# 54. Kafka + Airflow Together

Important:

```text
Kafka = Streaming
Airflow = Orchestration
```

Kafka handles events arriving continuously.

Airflow handles scheduled/workflow execution.

Example:

```text
Machines
  ↓
producer.py
  ↓
Kafka topic
  ↓
consumer.py
  ↓
real-time analytics

Airflow DAG
  ↓
daily aggregation
  ↓
model retraining
  ↓
report generation
```

---

# 55. GitHub Actions

GitHub Actions automates CI/CD and workflows.

Workflow files go inside:

```text
.github/workflows/
```

Example:

```text
.github/
└── workflows/
    └── ci.yml
```

---

# 56. Basic GitHub Actions Workflow

Example `ci.yml`:

```yaml
name: Python CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v6

      - name: Setup Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.11"

      - name: Upgrade pip
        run: python -m pip install --upgrade pip

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest -q
```

---

# 57. GitHub Actions Keywords

## name

```yaml
name: Python CI
```

Workflow name.

## on

```yaml
on:
  push:
```

Defines trigger.

## jobs

```yaml
jobs:
```

Defines workflow jobs.

## runs-on

```yaml
runs-on: ubuntu-latest
```

Defines runner OS.

## steps

```yaml
steps:
```

Commands/actions executed in sequence.

## uses

```yaml
uses: actions/checkout@v6
```

Uses reusable GitHub Action.

## run

```yaml
run: pytest
```

Runs shell command.

## with

```yaml
with:
  python-version: "3.11"
```

Passes configuration to an action.

---

# 58. GitHub Actions Triggers

## Push

```yaml
on:
  push:
```

## Pull request

```yaml
on:
  pull_request:
```

## Both

```yaml
on:
  push:
  pull_request:
```

## Main branch only

```yaml
on:
  push:
    branches:
      - main
```

## Manual trigger

```yaml
on:
  workflow_dispatch:
```

## Scheduled trigger

```yaml
on:
  schedule:
    - cron: "0 0 * * *"
```

---

# 59. GitHub Actions Multiple Jobs

```yaml
name: CI/CD

on:
  push:

jobs:

  test:
    runs-on: ubuntu-latest

    steps:
      - name: Test
        run: echo "Testing"

  deploy:
    needs: test
    runs-on: ubuntu-latest

    steps:
      - name: Deploy
        run: echo "Deploying"
```

Dependency:

```yaml
needs: test
```

means deploy runs after test succeeds.

---

# 60. Environment Variables in Actions

```yaml
env:
  APP_ENV: production

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - run: echo "$APP_ENV"
```

---

# 61. GitHub Secrets

Never hardcode:

```yaml
API_KEY: abc123
```

Instead store the secret in GitHub repository settings.

Then use:

```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}
```

Example:

```yaml
steps:
  - name: Run app
    env:
      API_KEY: ${{ secrets.API_KEY }}
    run: python app.py
```

---

# 62. GitHub Variables

For non-secret configuration:

```yaml
${{ vars.APP_ENV }}
```

Difference:

```text
Secrets → passwords, tokens, API keys
Variables → normal configuration
```

---

# 63. GitHub Actions Matrix

Example:

```yaml
name: Python Matrix

on:
  push:

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
      - uses: actions/checkout@v6

      - uses: actions/setup-python@v6
        with:
          python-version: ${{ matrix.python-version }}

      - run: pip install -r requirements.txt

      - run: pytest
```

This tests multiple Python versions.

---

# 64. GitHub Actions Conditions

```yaml
if: github.ref == 'refs/heads/main'
```

Example:

```yaml
- name: Deploy
  if: github.ref == 'refs/heads/main'
  run: echo "Deploying main"
```

---

# 65. GitHub Administration

Know where to find:

```text
Repository
└── Settings
    ├── General
    ├── Collaborators
    ├── Actions
    ├── Secrets and variables
    ├── Environments
    ├── Webhooks
    ├── Rules
    └── Branch settings
```

---

# 66. Branch Protection / Rulesets

Typical protection rules:

```text
Require pull request before merging
Require approvals
Require status checks
Prevent force pushes
Restrict deletion
Require signed commits
```

Purpose:

Protect important branches like:

```text
main
production
release
```

---

# 67. Pull Request Workflow

Typical:

```text
main
  ↑
feature branch
```

Commands:

```bash
git switch -c feature/kafka
```

Make changes.

```bash
git add .
git commit -m "add kafka producer"
git push -u origin feature/kafka
```

Then create pull request.

After review:

```text
feature/kafka → main
```

---

# 68. GitHub Environments

Examples:

```text
development
staging
production
```

Workflow:

```yaml
jobs:
  deploy:
    environment: production
    runs-on: ubuntu-latest

    steps:
      - run: echo "Deploying"
```

Production may require manual approval.

---

# 69. GitHub Codespaces Ports

Important ports:

Kafka:

```text
9092
```

Airflow UI:

```text
8080
```

In Codespaces, open the:

```text
PORTS
```

tab.

You may see:

```text
8080
```

Click the browser icon to open Airflow.

---

# 70. Python Syntax Validation

Before committing Python:

```bash
python -m py_compile producer.py
```

Multiple:

```bash
python -m py_compile producer.py consumer.py topic.py stats.py detection.py
```

Compile whole directory:

```bash
python -m compileall .
```

---

# 71. Run Tests

If repository has tests:

```bash
pytest
```

Compact output:

```bash
pytest -q
```

Specific file:

```bash
pytest tests/test_producer.py
```

Specific test:

```bash
pytest tests/test_producer.py::test_producer
```

---

# 72. requirements.txt Example

```text
kafka-python
pytest
apache-airflow
```

Install:

```bash
pip install -r requirements.txt
```

---

# 73. .gitignore Example

```gitignore
.venv/
__pycache__/
*.pyc
.env
.pytest_cache/
airflow.db
logs/
```

Do not normally commit:

```text
.venv/
API keys
.env
generated cache
```

---

# 74. Example .env File

```env
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_TOPIC=sensor-data
```

Never commit real secrets inside `.env`.

Add:

```gitignore
.env
```

---

# 75. Using Environment Variables in Python

```python
import os

bootstrap_server = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS",
    "localhost:9092"
)

topic = os.getenv(
    "KAFKA_TOPIC",
    "sensor-data"
)

print(bootstrap_server)
print(topic)
```

---

# 76. Full Example Project Structure

```text
aiops-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── dags/
│   └── aiops_pipeline.py
│
├── tests/
│   ├── test_stats.py
│   └── test_detection.py
│
├── producer.py
├── consumer.py
├── topic.py
├── stats.py
├── detection.py
├── requirements.txt
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

# 77. Example stats.py

```python
import statistics


def calculate_stats(values):
    if not values:
        return {
            "mean": 0,
            "min": 0,
            "max": 0,
            "std": 0
        }

    result = {
        "mean": statistics.mean(values),
        "min": min(values),
        "max": max(values)
    }

    if len(values) > 1:
        result["std"] = statistics.stdev(values)
    else:
        result["std"] = 0

    return result


if __name__ == "__main__":
    values = [10, 20, 30, 40, 50]

    print(calculate_stats(values))
```

---

# 78. Example detection.py

```python
def threshold_anomaly(value, threshold=80):
    return value > threshold


if __name__ == "__main__":
    temperature = 95

    if threshold_anomaly(temperature):
        print("Anomaly detected")
    else:
        print("Normal")
```

---

# 79. Unit Test Example

`tests/test_detection.py`

```python
from detection import threshold_anomaly


def test_normal_value():
    assert threshold_anomaly(50) is False


def test_anomaly_value():
    assert threshold_anomaly(95) is True
```

Run:

```bash
pytest -q
```

---

# 80. Unit Test for Statistics

`tests/test_stats.py`

```python
from stats import calculate_stats


def test_stats():
    result = calculate_stats([10, 20, 30])

    assert result["mean"] == 20
    assert result["min"] == 10
    assert result["max"] == 30
```

---

# 81. GitHub Actions Test Workflow

```yaml
name: AIOps CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Setup Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Syntax check
        run: |
          python -m compileall .

      - name: Unit tests
        run: |
          pytest -q
```

---

# 82. Typical Exam Task Sequence

## Task 1 — Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Verify:

```bash
python --version
pip list
```

Commit:

```bash
git add .
git commit -m "task 1: setup environment"
git push
```

---

## Task 2 — Start Kafka

```bash
docker compose up -d
```

Check:

```bash
docker compose ps
```

---

## Task 3 — Create Topic

```bash
bin/kafka-topics.sh \
  --create \
  --topic metrics \
  --bootstrap-server localhost:9092
```

Verify:

```bash
bin/kafka-topics.sh \
  --list \
  --bootstrap-server localhost:9092
```

---

## Task 4 — Implement Producer

Run:

```bash
python producer.py
```

Verify with consumer.

Commit:

```bash
git add producer.py
git commit -m "task 4: implement kafka producer"
git push
```

---

## Task 5 — Implement Consumer

Run:

```bash
python consumer.py
```

Commit:

```bash
git add consumer.py
git commit -m "task 5: implement kafka consumer"
git push
```

---

## Task 6 — Statistics

Run:

```bash
python stats.py
```

Then:

```bash
git add stats.py
git commit -m "task 6: add metric statistics"
git push
```

---

## Task 7 — Detection

Run:

```bash
python detection.py
```

Then:

```bash
git add detection.py
git commit -m "task 7: implement anomaly detection"
git push
```

---

## Task 8 — Airflow DAG

Check DAG:

```bash
airflow dags list
```

Check errors:

```bash
airflow dags list-import-errors
```

Tasks:

```bash
airflow tasks list aiops_pipeline
```

Trigger:

```bash
airflow dags trigger aiops_pipeline
```

Commit:

```bash
git add dags/
git commit -m "task 8: create airflow dag"
git push
```

---

## Task 9 — GitHub Action

Create:

```text
.github/workflows/ci.yml
```

Commit:

```bash
git add .github/workflows/ci.yml
git commit -m "task 9: add CI workflow"
git push
```

---

# 83. Common Errors and Fixes

| Error | Likely Cause | Fix |
|---|---|---|
| `ModuleNotFoundError` | venv/dependency missing | activate venv, `pip install` |
| `NoBrokersAvailable` | Kafka down/wrong port | inspect Kafka |
| Connection refused `9092` | Kafka not listening | start broker |
| DAG missing | import/syntax error | `airflow dags list-import-errors` |
| `airflow: command not found` | not installed/venv inactive | activate/install |
| `python: command not found` | system uses `python3` | use `python3` |
| YAML error | indentation/syntax | fix spacing |
| Action failure | test/setup problem | inspect Actions logs |
| `nothing to commit` | no changed files | `git status` |
| rejected push | remote ahead/branch issue | `git pull`, inspect branch |
| topic already exists | duplicate creation | list/check topic |
| address already in use | process already running | inspect port/process |

---

# 84. Useful Port Debugging

Kafka:

```bash
ss -ltnp | grep 9092
```

Airflow:

```bash
ss -ltnp | grep 8080
```

Generic:

```bash
ss -ltnp
```

---

# 85. Useful Process Debugging

Kafka:

```bash
ps aux | grep kafka
```

Airflow:

```bash
ps aux | grep airflow
```

Python:

```bash
ps aux | grep python
```

---

# 86. Kill Process

Find PID:

```bash
ps aux | grep python
```

Then:

```bash
kill <PID>
```

Force:

```bash
kill -9 <PID>
```

Use carefully.

---

# 87. Docker Commands to Know

## Running containers

```bash
docker ps
```

All:

```bash
docker ps -a
```

## Images

```bash
docker images
```

## Logs

```bash
docker logs <container>
```

Follow:

```bash
docker logs -f <container>
```

## Stop

```bash
docker stop <container>
```

## Remove

```bash
docker rm <container>
```

## Compose startup

```bash
docker compose up -d
```

## Compose shutdown

```bash
docker compose down
```

## Compose status

```bash
docker compose ps
```

## Compose logs

```bash
docker compose logs
```

---

# 88. YAML Indentation

Wrong:

```yaml
jobs:
test:
runs-on: ubuntu-latest
```

Correct:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
```

Use spaces consistently.

---

# 89. Debugging Strategy During Exam

When something fails:

```text
1. READ ERROR
2. CHECK STATUS
3. CHECK PROCESS/SERVICE
4. CHECK PORT
5. CHECK FILE
6. CHECK DEPENDENCY
7. RUN TEST
8. FIX
9. VERIFY
10. COMMIT
```

Do not randomly reinstall everything.

---

# 90. Golden Commands Before Every Commit

```bash
git status
git diff
python -m compileall .
pytest -q
```

Then:

```bash
git add .
git commit -m "task X: description"
git push
```

---

# 91. Git Recovery Basics

Undo unstaged changes to one file:

```bash
git restore file.py
```

Unstage:

```bash
git restore --staged file.py
```

See commit history:

```bash
git log --oneline
```

Show commit:

```bash
git show <commit-hash>
```

---

# 92. Important AIOps Concepts

AIOps combines:

```text
Monitoring
Logs
Metrics
Events
Automation
Machine Learning
Anomaly Detection
Root Cause Analysis
Alerting
Orchestration
```

Typical flow:

```text
Infrastructure
    ↓
Metrics / logs / events
    ↓
Collection
    ↓
Kafka
    ↓
Processing
    ↓
ML / statistics
    ↓
Anomaly Detection
    ↓
Alert
    ↓
Automated response
```

---

# 93. Batch vs Real-Time

## Batch

Data processed in groups.

Example:

```text
Process yesterday's logs at midnight.
```

Airflow is commonly used for scheduled batch orchestration.

## Real-Time

Data processed continuously.

Example:

```text
Process CPU metrics immediately as they arrive.
```

Kafka is commonly used for real-time streaming.

---

# 94. Kafka vs Airflow

| Kafka | Airflow |
|---|---|
| Event streaming | Workflow orchestration |
| Continuous data | Scheduled/dependency workflows |
| Producer/consumer | DAG/task |
| Topics | DAGs |
| Partitions | Task dependencies |
| Offsets | Task states |
| Real-time | Mostly orchestration/batch scheduling |

---

# 95. Kafka Producer vs Consumer

| Producer | Consumer |
|---|---|
| Sends messages | Reads messages |
| Writes to topic | Reads from topic |
| Uses `KafkaProducer` | Uses `KafkaConsumer` |
| `send()` | Iterates messages |

---

# 96. Topic vs Partition

Topic:

```text
sensor-data
```

Partitions:

```text
sensor-data-0
sensor-data-1
sensor-data-2
```

A topic is the logical stream.

Partitions divide its data for scalability.

---

# 97. Offset

Example:

```text
Partition 0

Offset 0 → Message A
Offset 1 → Message B
Offset 2 → Message C
```

The consumer tracks which offset it has processed.

---

# 98. Consumer Groups

If 3 partitions and 3 consumers in one group:

```text
P0 → C1
P1 → C2
P2 → C3
```

If 3 partitions and 5 consumers:

```text
3 consumers receive partitions
2 consumers may remain idle
```

A partition can normally be actively consumed by only one consumer within the same consumer group at a time.

---

# 99. Replication

Example:

```text
Replication factor = 3
```

Kafka stores 3 copies of each partition across brokers.

Purpose:

```text
fault tolerance
availability
```

---

# 100. Airflow DAG Rules

DAG must be acyclic.

Valid:

```text
A → B → C
```

Invalid:

```text
A → B → C
↑       ↓
└───────┘
```

Because that creates a cycle.

---

# 101. Airflow Dependencies

Sequential:

```python
task1 >> task2
```

Equivalent:

```python
task2.set_upstream(task1)
```

Multiple downstream tasks:

```python
task1 >> [task2, task3]
```

Then:

```text
      task2
     ↗
task1
     ↘
      task3
```

---

# 102. Airflow Operator Examples

Python:

```python
PythonOperator
```

Shell:

```python
BashOperator
```

No-operation placeholder:

```python
EmptyOperator
```

---

# 103. GitHub Actions CI/CD Meaning

CI:

```text
Continuous Integration
```

Typical:

```text
push code
↓
install dependencies
↓
lint
↓
test
↓
build
```

CD:

```text
Continuous Delivery / Deployment
```

Typical:

```text
tests pass
↓
deploy application
```

---

# 104. CI Pipeline Mental Model

```text
Developer push
     ↓
GitHub
     ↓
GitHub Actions trigger
     ↓
Runner starts
     ↓
Checkout
     ↓
Setup Python
     ↓
Install dependencies
     ↓
Run tests
     ↓
Pass / Fail
```

---

# 105. GitHub Actions Runner

Example:

```yaml
runs-on: ubuntu-latest
```

GitHub creates a temporary runner machine to execute the job.

---

# 106. Workflow vs Job vs Step

```text
Workflow
   ↓
Jobs
   ↓
Steps
```

Example:

```text
CI Workflow
│
├── Test Job
│   ├── Checkout
│   ├── Install
│   └── Test
│
└── Deploy Job
    ├── Login
    └── Deploy
```

---

# 107. GitHub Actions Failure Debugging

Check:

```text
GitHub repository
→ Actions
→ failed workflow
→ failed job
→ failed step
→ logs
```

Common issues:

```text
incorrect YAML
missing package
wrong path
failed tests
missing secret
wrong Python version
permission failure
```

---

# 108. Repository Security Basics

Never commit:

```text
password
API key
private key
secret token
database credentials
```

Use:

```text
GitHub Secrets
environment variables
.env file excluded by .gitignore
```

---

# 109. Codespaces Important Behavior

Codespaces gives you:

```text
VS Code-like editor
Linux terminal
Git repository integration
port forwarding
extensions
preconfigured environment
```

Therefore always think Linux commands during the practical.

---

# 110. Exam Checklist

Before starting:

```text
[ ] Correct repository
[ ] Correct branch
[ ] Codespace running
[ ] Read README
[ ] git status clean
[ ] Check Python version
[ ] Activate venv
```

Kafka:

```text
[ ] Kafka running
[ ] Port 9092 working
[ ] Topic exists
[ ] Producer works
[ ] Consumer works
```

Airflow:

```text
[ ] Airflow installed
[ ] Check version
[ ] Airflow services running
[ ] Port 8080 available
[ ] DAG appears
[ ] No import errors
[ ] Task runs
```

GitHub:

```text
[ ] Correct workflow location
[ ] YAML valid
[ ] Required trigger correct
[ ] Commit created
[ ] Push successful
[ ] Actions check passed
```

---

# 111. Priority Order for Studying

If you are short on time, study in this order.

## Priority 1 — Git

```bash
git status
git diff
git add .
git commit -m "message"
git push
git pull
git log --oneline
```

## Priority 2 — venv

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Priority 3 — Kafka Concepts

Know:

```text
broker
topic
partition
producer
consumer
offset
consumer group
replication
```

Commands:

```text
kafka-topics.sh
kafka-console-producer.sh
kafka-console-consumer.sh
```

## Priority 4 — Kafka Python

Know:

```python
KafkaProducer
KafkaConsumer
KafkaAdminClient
NewTopic
```

## Priority 5 — Airflow

Know:

```text
DAG
task
operator
scheduler
executor
metadata DB
XCom
catchup
schedule
```

Commands:

```bash
airflow version
airflow standalone
airflow dags list
airflow dags list-import-errors
airflow tasks list
airflow dags trigger
```

## Priority 6 — GitHub Actions

Know:

```yaml
name:
on:
jobs:
runs-on:
steps:
uses:
run:
with:
```

## Priority 7 — GitHub Admin

Know:

```text
Secrets
Variables
Collaborators
Rulesets
Branch protection
Actions permissions
Environments
```

---

# 112. Final Command Cheat Sheet

```bash
# =========================================================
# INITIAL INSPECTION
# =========================================================

pwd
ls -la
git status
git branch
git remote -v
git log --oneline -5
cat README.md
python3 --version


# =========================================================
# VIRTUAL ENVIRONMENT
# =========================================================

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt

pip list

pip freeze > requirements.txt


# =========================================================
# KAFKA / DOCKER
# =========================================================

docker compose up -d

docker compose ps

docker compose logs

docker compose logs -f


# =========================================================
# KAFKA TOPIC
# =========================================================

bin/kafka-topics.sh \
  --create \
  --topic sensor-data \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1

bin/kafka-topics.sh \
  --list \
  --bootstrap-server localhost:9092

bin/kafka-topics.sh \
  --describe \
  --topic sensor-data \
  --bootstrap-server localhost:9092


# =========================================================
# KAFKA PRODUCER
# =========================================================

bin/kafka-console-producer.sh \
  --topic sensor-data \
  --bootstrap-server localhost:9092


# =========================================================
# KAFKA CONSUMER
# =========================================================

bin/kafka-console-consumer.sh \
  --topic sensor-data \
  --bootstrap-server localhost:9092 \
  --from-beginning


# =========================================================
# AIRFLOW
# =========================================================

airflow version

airflow standalone

airflow dags list

airflow dags list-import-errors

airflow tasks list aiops_pipeline

airflow dags trigger aiops_pipeline


# =========================================================
# TESTING
# =========================================================

python -m py_compile producer.py

python -m compileall .

pytest -q


# =========================================================
# PORT DEBUGGING
# =========================================================

ss -ltnp | grep 9092

ss -ltnp | grep 8080


# =========================================================
# PROCESS DEBUGGING
# =========================================================

ps aux | grep kafka

ps aux | grep airflow

ps aux | grep python


# =========================================================
# GIT CHECKPOINT
# =========================================================

git status

git diff

git add .

git commit -m "completed task"

git push

git log --oneline -5
```

---

# 113. Final Mental Model

Remember this entire exam as one flow:

```text
SETUP
  ↓
Codespace + venv + dependencies
  ↓
INFRASTRUCTURE
  ↓
Kafka broker
  ↓
STREAM
  ↓
Topic → Producer → Consumer
  ↓
PROCESS
  ↓
Statistics → Detection
  ↓
ORCHESTRATE
  ↓
Airflow DAG
  ↓
AUTOMATE
  ↓
GitHub Actions
  ↓
VERSION
  ↓
git add → commit → push
  ↓
VALIDATE
  ↓
Portal unlocks next step
```

If you can perform this whole sequence from a fresh Codespace without looking things up constantly, you are in good shape for a practical AIOps exam.

---

# 114. Ultra-Short Last-Minute Revision

```text
GIT:
status → diff → add → commit → push

VENV:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

KAFKA:
Broker → Topic → Producer → Consumer
9092
Topic → Partition → Offset
Consumer Group
Replication

AIRFLOW:
DAG → Tasks → Scheduler → Executor
8080
airflow dags list
airflow dags list-import-errors
airflow dags trigger

GITHUB ACTIONS:
.github/workflows/*.yml
name
on
jobs
runs-on
steps
uses
run

EXAM:
READ → DO → VERIFY → COMMIT → PUSH
```

---

# 115. Best Practice Before the Exam

Create a throwaway GitHub repository and practice this exact sequence:

```text
1. Open Codespace
2. Create venv
3. Install dependencies
4. Start Kafka
5. Create topic
6. Run producer
7. Run consumer
8. Calculate statistics
9. Detect anomaly
10. Create Airflow DAG
11. Run/test DAG
12. Create GitHub Action
13. Commit each stage separately
14. Push everything
15. Break something intentionally
16. Debug it
```

That single practice run will teach you more than simply memorizing commands.
