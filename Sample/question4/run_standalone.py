"""
Question 4 — Standalone Runner for Airflow DAG Tasks
Allows running and demonstrating the 4 AIOps tasks sequentially without
requiring a running Airflow scheduler or webserver.
"""


def run_standalone_pipeline():
    print("==========================================")
    print("  SIMULATING APACHE AIRFLOW AIOps DAG     ")
    print("  collect >> process >> detect >> report  ")
    print("==========================================\n")

    # Shared execution context mimicking Airflow XCom
    context = {}

    # Task 1: collect_metrics
    print("[TASK 1: collect_metrics]")
    metrics = {
        "CPU": 87,
        "Memory": 65,
        "Response Time": "420ms"
    }
    print(f"Sampled Metrics: CPU = {metrics['CPU']}, Memory = {metrics['Memory']}, Response Time = {metrics['Response Time']}")
    context["server_metrics"] = metrics
    print("Task 1 completed.\n")

    # Task 2: process_metrics
    print("[TASK 2: process_metrics]")
    data = context["server_metrics"]
    print(f"Processing collected metrics: CPU={data['CPU']}%, Memory={data['Memory']}%, Latency={data['Response Time']}")
    print("Task 2 completed.\n")

    # Task 3: detect_anomaly
    print("[TASK 3: detect_anomaly]")
    cpu_val = data["CPU"]
    if cpu_val > 80:
        print("Anomaly detected: High CPU usage")
        context["anomaly"] = True
    else:
        print("No anomaly detected")
        context["anomaly"] = False
    print("Task 3 completed.\n")

    # Task 4: generate_report
    print("[TASK 4: generate_report]")
    print("===== AIOps Report =====")
    print("Metrics collected successfully")
    print("Metrics processed successfully")
    print("Anomaly detection completed")
    print("========================\n")
    print("AIOps Airflow Workflow completed successfully!")


if __name__ == "__main__":
    run_standalone_pipeline()
