import pandas as pd
from pathlib import Path
from inference import predict_anomalies

path = Path("data/raw/NAB/data/realAWSCloudwatch/ec2_cpu_utilization_24ae8d.csv")
df = pd.read_csv(path)

values = df["value"].tolist()
out = predict_anomalies(values)

print("Warmup dropped:", out["warmup_points_dropped"])
print("Output length:", len(out["anomaly"]))
print("Anomalies detected:", sum(out["anomaly"]))
