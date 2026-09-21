"""
Question 5 — Simulation Stream Runner
Runs the exact test case from the Question 5 prompt:
server01 (85%), server02 (45%), server03 (91%) -> Total anomalies detected: 2
"""

from aiops_monitoring_consumer import AIOpsMonitor

def main():
    print("==========================================")
    print("   QUESTION 5 — AIOps MONITORING DEMO     ")
    print("==========================================\n")

    monitor = AIOpsMonitor()

    stream = [
        {"server_id": "server01", "cpu_usage": 85},
        {"server_id": "server02", "cpu_usage": 45},
        {"server_id": "server03", "cpu_usage": 91}
    ]

    for record in stream:
        monitor.process_message(record)

    monitor.print_summary()
    print("==========================================")

if __name__ == "__main__":
    main()
