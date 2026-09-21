import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Create / Read Sample Dataset (20 records)
data = {
    "Timestamp": [
        "10:00", "10:01", "10:02", "10:03", "10:04",
        "10:05", "10:06", "10:07", "10:08", "10:09",
        "10:10", "10:11", "10:12", "10:13", "10:14",
        "10:15", "10:16", "10:17", "10:18", "10:19"
    ],
    "CPU Usage": [
        45, 52, 48, 55, 51,
        95, 49, 53, 50, 54,
        47, 52, 97, 51, 49,
        55, 48, 53, 92, 50
    ],
    "Memory Usage": [
        60, 62, 61, 63, 60,
        65, 62, 64, 61, 63,
        60, 62, 66, 61, 63,
        62, 60, 64, 61, 62
    ],
    "Response Time": [
        200, 220, 210, 230, 215,
        240, 225, 210, 220, 215,
        230, 220, 250, 210, 225,
        220, 215, 230, 240, 220
    ]
}

df = pd.DataFrame(data)

# Save to CSV for reference
csv_path = os.path.join(os.path.dirname(__file__), "server_logs.csv")
df.to_csv(csv_path, index=False)

# 2. Calculate Basic Statistics
print("==========================================")
print("        AIOps METRIC STATISTICS           ")
print("==========================================")
print(df.describe())
print()

# 3. Detect Anomalies using Threshold-Based Approach
# Thresholds
CPU_THRESHOLD = 90
MEMORY_THRESHOLD = 90
RESPONSE_THRESHOLD = 500

df["Anomaly"] = (
    (df["CPU Usage"] > CPU_THRESHOLD) |
    (df["Memory Usage"] > MEMORY_THRESHOLD) |
    (df["Response Time"] > RESPONSE_THRESHOLD)
)

anomalies = df[df["Anomaly"]]

# 4. Print Summary and Anomalous Records
total_records = len(df)
anomalies_detected = len(anomalies)

print("==========================================")
print(f"Total records: {total_records}")
print(f"Anomalies detected: {anomalies_detected}")
print("==========================================")
print(f"{'Timestamp':<16}{'CPU':<10}{'Status'}")
for _, row in anomalies.iterrows():
    print(f"{row['Timestamp']:<16}{str(row['CPU Usage']) + '%':<10}{'ANOMALY'}")
print("==========================================\n")

# 5. Display and Save Graph
plt.figure(figsize=(10, 5))

# Plot normal metric line
plt.plot(
    df["Timestamp"],
    df["CPU Usage"],
    marker="o",
    color="#2b5c8f",
    label="CPU Usage (%)"
)

# Plot anomalies as prominent scatter points
plt.scatter(
    anomalies["Timestamp"],
    anomalies["CPU Usage"],
    color="#d9381e",
    s=120,
    zorder=5,
    label="Anomaly"
)

# Threshold line
plt.axhline(
    CPU_THRESHOLD,
    color="#e67e22",
    linestyle="--",
    linewidth=1.5,
    label=f"CPU Threshold ({CPU_THRESHOLD}%)"
)

plt.xlabel("Timestamp", fontweight="bold")
plt.ylabel("CPU Usage (%)", fontweight="bold")
plt.title("AIOps Anomaly Detection — Server CPU Usage", fontweight="bold", fontsize=12)
plt.legend(loc="upper left")
plt.xticks(rotation=45)
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()

# Save graph
output_graph_path = os.path.join(os.path.dirname(__file__), "anomaly_graph.png")
plt.savefig(output_graph_path, dpi=150)
print(f"Graph saved successfully to: {output_graph_path}")

# In environments with GUI display, show plot
try:
    plt.show()
except Exception:
    pass
