# Question 4 — Build an AIOps Workflow using Airflow

## Problem Statement

Create an Apache Airflow DAG representing a basic AIOps workflow.

The workflow should contain the following tasks:
```text
Collect Metrics
      ↓
Process Metrics
      ↓
Detect Anomaly
      ↓
Generate Report
```

### Requirements:
- **Task 1 — `collect_metrics`**:
  Use `PythonOperator` to generate/sample server metrics.
  Example: `CPU = 87`, `Memory = 65`, `Response Time = 420ms`.
- **Task 2 — `process_metrics`**:
  Process the collected metrics and print them.
- **Task 3 — `detect_anomaly`**:
  Check whether `CPU > 80`.
  If yes, print: `Anomaly detected: High CPU usage`.
  Otherwise: `No anomaly detected`.
- **Task 4 — `generate_report`**:
  Print a final AIOps report:
  ```text
  ===== AIOps Report =====
  Metrics collected successfully
  Metrics processed successfully
  Anomaly detection completed
  ========================
  ```

### DAG Requirements:
Your DAG must:
- Use `PythonOperator`.
- Define all four tasks.
- Define the correct dependencies:
  ```python
  collect_metrics >> process_metrics >> detect_anomaly >> generate_report
  ```

---

## File Contents

- `sample/question4/aiops_dag.py`: The production Airflow DAG file.
- `sample/question4/run_standalone.py`: A standalone Python runner to execute the DAG tasks without needing an active Airflow service.

---

## How to Test

### Method A: Standalone Execution (Instant Verification)
Run:
```bash
python sample/question4/run_standalone.py
```

### Method B: Testing inside an Airflow Environment
1. Copy `aiops_dag.py` to your Airflow DAGs directory (usually `~/airflow/dags`).
2. Test the DAG execution via Airflow CLI:
   ```bash
   airflow dags test aiops_workflow_dag 2026-01-01
   ```
3. Or test individual tasks:
   ```bash
   airflow tasks test aiops_workflow_dag collect_metrics 2026-01-01
   airflow tasks test aiops_workflow_dag process_metrics 2026-01-01
   airflow tasks test aiops_workflow_dag detect_anomaly 2026-01-01
   airflow tasks test aiops_workflow_dag generate_report 2026-01-01
   ```
