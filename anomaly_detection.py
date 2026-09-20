import pandas as pd
import matplotlib.pyplot as plt

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

print("Dataset:")
print(df)

print("\nBasic Statistics:")
print(df.describe())

CPU_THRESHOLD = 90
MEMORY_THRESHOLD = 90
RESPONSE_THRESHOLD = 500

df["Anomaly"] = (
    (df["CPU Usage"] > CPU_THRESHOLD) |
    (df["Memory Usage"] > MEMORY_THRESHOLD) |
    (df["Response Time"] > RESPONSE_THRESHOLD)
)

anomalies = df[df["Anomaly"]]

print("\nAnomalies:")
print(anomalies)

plt.figure(figsize=(10, 5))

plt.plot(df["Timestamp"], df["CPU Usage"], marker="o", label="CPU Usage")

plt.scatter(
    anomalies["Timestamp"],
    anomalies["CPU Usage"],
    s=100,
    label="Anomaly"
)

plt.axhline(CPU_THRESHOLD, linestyle="--", label="CPU Threshold")

plt.xlabel("Timestamp")
plt.ylabel("CPU Usage (%)")
plt.title("AIOps CPU Usage and Anomalies")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("anomaly_graph.png")