import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Timestamp" : [
        "10:01", "10:02", "10:03", "10:04", "10:05",
        "10:06", "10:07", "10:08", "10:09", "10:10", 
        "10:11", "10:12", "10:13", "10:14", "10:15",
        "10:16", "10:18", "10:19", "10:20", "10:21"
    ],

    "Incoming Traffic" : [
        520, 670, 402, 408, 400,
        480, 870, 920, 470, 550,
        506, 708, 997, 999, 1012,
        1405, 1506, 780, 808, 890,
    ],

    "Outgoing Traffic" : [
        590, 370, 302, 340, 350,
        580, 670, 920, 370, 950,
        406, 808, 797, 899, 912,
        905, 906, 1280, 208, 890,
    ],

    "Packet Loss" : [
        5, 7, 3, 4, 5,
        5, 6, 9, 3, 5,
        4, 8, 7, 8, 2,
        2, 6, 1, 8, 0,
    ],

    "Latency" : [
        220, 120, 102, 208, 100,
        40, 170, 90, 40, 50,
        16, 180, 197, 309, 102,
        125, 206, 280, 208, 290,
    ]

}

df = pd.DataFrame(data)
print("Data :\n",df)

print("Statistics :\n", df.describe())

df["Anomaly"] = (
    (df["Incoming Traffic"] > 900) |
    (df["Outgoing Traffic"] > 800) |
    (df["Packet Loss"] > 5) |
    (df["Latency"] > 200)
)

anomalies = df[df["Anomaly"]]

print("Anomalies : \n", anomalies)

plt.figure(figsize=(10, 5))

plt.plot(
    df["Timestamp"],
    df["Latency"],
    marker="o",
    label="Latency"
)

plt.scatter(
    anomalies["Timestamp"],
    anomalies["Latency"],
    s=100,
    label="Anomaly"
)

plt.axhline(
    LATENCY_THRESHOLD,
    linestyle="--",
    label="Latency Threshold"
)

plt.xlabel("Timestamp")
plt.ylabel("Latency (ms)")
plt.title("Network Latency and Anomalies")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("network_anomaly.png")

print("\nGraph saved as network_anomaly.png")