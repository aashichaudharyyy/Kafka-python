"""
Question 4 — Apache Airflow AIOps Workflow DAG
Defines an AIOps lifecycle pipeline using PythonOperator:
collect_metrics >> process_metrics >> detect_anomaly >> generate_report
"""

from datetime import datetime, timedelta
from airflow import DAG

# In modern Airflow 2.x+, PythonOperator is available from standard or operators module
try:
    from airflow.operators.python import PythonOperator
except ImportError:
    from airflow.providers.standard.operators.python import PythonOperator


# -------------------------------------------------------------
# Task Definitions
# -------------------------------------------------------------

def collect_metrics(**context):
    """
    Task 1: collect_metrics
    Generates / samples operational server metrics.
    Pushes data via XCom for downstream task consumption.
    """
    metrics = {
        "CPU": 87,
        "Memory": 65,
        "Response Time": "420ms"
    }
    print("--- Task 1: Collect Metrics ---")
    print(f"Sampled Metrics: CPU={metrics['CPU']}%, Memory={metrics['Memory']}%, Response Time={metrics['Response Time']}")
    
    # Store in XCom if context is available
    if "ti" in context:
        context["ti"].xcom_push(key="server_metrics", value=metrics)
    return metrics


def process_metrics(**context):
    """
    Task 2: process_metrics
    Processes and logs the collected metrics.
    """
    print("--- Task 2: Process Metrics ---")
    metrics = None
    if "ti" in context and context["ti"] is not None:
        metrics = context["ti"].xcom_pull(task_ids="collect_metrics", key="server_metrics")

    # Fallback to default if testing without XCom
    if not metrics:
        metrics = {"CPU": 87, "Memory": 65, "Response Time": "420ms"}

    print("Processed Operational Metrics:")
    for metric_name, value in metrics.items():
        print(f"  {metric_name}: {value}")
    return metrics


def detect_anomaly(**context):
    """
    Task 3: detect_anomaly
    Checks whether CPU > 80 and logs anomaly status.
    """
    print("--- Task 3: Detect Anomaly ---")
    metrics = None
    if "ti" in context and context["ti"] is not None:
        metrics = context["ti"].xcom_pull(task_ids="collect_metrics", key="server_metrics")

    if not metrics:
        metrics = {"CPU": 87, "Memory": 65, "Response Time": "420ms"}

    cpu_val = float(metrics.get("CPU", 0))
    print(f"Evaluating CPU Threshold (Threshold = 80%, Current = {cpu_val}%)...")

    if cpu_val > 80:
        print("Anomaly detected: High CPU usage")
        is_anomaly = True
    else:
        print("No anomaly detected")
        is_anomaly = False

    if "ti" in context:
        context["ti"].xcom_push(key="is_anomaly", value=is_anomaly)
    return is_anomaly


def generate_report(**context):
    """
    Task 4: generate_report
    Prints the final AIOps execution report.
    """
    print("--- Task 4: Generate Report ---")
    print("===== AIOps Report =====")
    print("Metrics collected successfully")
    print("Metrics processed successfully")
    print("Anomaly detection completed")
    print("========================")


# -------------------------------------------------------------
# DAG Configuration & Dependency Definition
# -------------------------------------------------------------

default_args = {
    "owner": "aiops_engineer",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="aiops_workflow_dag",
    default_args=default_args,
    description="AIOps Lifecycle: Collect -> Process -> Detect -> Report",
    schedule_interval=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["aiops", "metrics", "monitoring"],
) as dag:

    task_collect = PythonOperator(
        task_id="collect_metrics",
        python_callable=collect_metrics,
        provide_context=True,
    )

    task_process = PythonOperator(
        task_id="process_metrics",
        python_callable=process_metrics,
        provide_context=True,
    )

    task_detect = PythonOperator(
        task_id="detect_anomaly",
        python_callable=detect_anomaly,
        provide_context=True,
    )

    task_report = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
        provide_context=True,
    )

    # Required linear workflow dependency
    task_collect >> task_process >> task_detect >> task_report
