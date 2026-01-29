## Anomaly Detection API (Time-Series)

### Dataset (AWS EC2 CPU Utilization)
This project was developed and tested using an **EC2 CPU utilization time-series dataset** (typical cloud monitoring telemetry).

This API is **dataset-agnostic**
It is designed to accept **any univariate numeric time-series** (e.g., CPU usage, latency, IoT sensor data).

For development/testing, I used:
- **Synthetic and sample time-series sequences** (including injected spikes) to validate behavior.
- Manual spot-checks in the live Swagger UI (`/docs`) to confirm scoring and warm-up handling.

- **Signal:** CPU utilization (%)
- **Granularity:** time-ordered metric values (sampled at a fixed interval)
- **What I used:** the CPU utilization column as the **univariate series** input to the feature engineering + Isolation Forest pipeline
- **Preprocessing:** sorted by timestamp, handled missing values, then generated rolling-window features (rolling mean/std)
- **Labels:** not required (unsupervised). Evaluation was done by inspecting score/flag behavior on normal periods vs CPU spikes.
  
A FastAPI-based, production-style anomaly detection service for **univariate time-series** data.  
It engineers rolling statistical features and uses an **Isolation Forest** model to flag anomalies and return anomaly scores via a REST API. Docker-ready for deployment.

---

### Live Demo
- **API Docs (Swagger):** https://anomaly-detection-api-z41e.onrender.com/docs

---

### Why This Project?
Monitoring systems generate continuous streams of metrics such as **CPU usage, latency, throughput, transaction volume**, etc. In many real-world setups, anomalies are **rare and unlabeled**, so supervised approaches are not always feasible. This project shows how to:
- build an **unsupervised** anomaly detector,
- expose it as an **API**,
- handle **warm-up** correctly for rolling features,
- and deploy it cleanly.

---

### Key Features
- Rolling statistical feature engineering (e.g., rolling mean, rolling std)
- Unsupervised anomaly detection using **Isolation Forest**
- **Warm-up handling** (early points that can’t form a full rolling window are excluded from scoring)
- REST API endpoint for real-time inference
- Dockerized deployment (portable + reproducible)

---

## How It Works
### 1) Input
You send a list of numeric values representing a time-ordered series.

### 2) Feature Engineering
For each point (after enough history exists), the service builds rolling features such as:
- rolling mean
- rolling standard deviation  
(Feature set may vary depending on your implementation.)

### 3) Scoring
Isolation Forest produces an anomaly score and a binary anomaly flag (0/1).

### 4) Output
The response includes:
- how many points were dropped as warm-up
- an anomaly flag list aligned to the original input
- an anomaly score list aligned to the original input

---

## API
### `POST /predict`
Detect anomalies from an ordered list of time-series values.

#### Request Body
```json
{
  "values": [0.13, 0.134, 0.132, 2.34, 0.133]
}
