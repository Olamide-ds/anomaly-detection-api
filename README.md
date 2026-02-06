# Anomaly Detection API (Time-Series)

## Dataset (AWS EC2 CPU Utilization)

This project was developed and tested using an **EC2 CPU utilization time-series dataset** (typical cloud monitoring telemetry).

This API is **dataset-agnostic**.  
It is designed to accept **any univariate numeric time-series** (e.g., CPU usage, latency, IoT sensor data).

### Development & Testing
For development and validation, the following approaches were used:
- **Synthetic and sample time-series sequences**, including injected spikes, to validate anomaly behavior
- Manual spot-checks using the live Swagger UI (`/docs`) to confirm scoring logic and warm-up handling

### Dataset Characteristics
- **Signal:** CPU utilization (%)
- **Granularity:** Time-ordered metric values sampled at a fixed interval
- **Input Used:** CPU utilization column as the **univariate series** for feature engineering + Isolation Forest
- **Preprocessing:**
  - Sorted by timestamp
  - Missing values handled
  - Rolling-window features generated (rolling mean, rolling standard deviation)
- **Labels:** Not required (unsupervised). Evaluation was performed by inspecting anomaly scores and flags during normal periods vs CPU spikes

This is a **FastAPI-based, production-style anomaly detection service** for **univariate time-series data**.  
It engineers rolling statistical features and uses an **Isolation Forest** model to flag anomalies and return anomaly scores via a REST API.  
The service is **Docker-ready** for deployment.

---

## Live Demo
- **API Docs (Swagger):** https://anomaly-detection-api-z41e.onrender.com/docs

---
**Why?-** Monitoring metrics are continuous, unlabeled, and anomaly-sparse.
This project demonstrates an unsupervised, API-driven approach with proper
warm-up handling and GenAI-based operational explanations.

---

## Key Features
- Rolling statistical feature engineering (e.g., rolling mean, rolling std)
- Unsupervised anomaly detection using **Isolation Forest**
- **Warm-up handling** (early points that cannot form a full rolling window are excluded from scoring)
- REST API endpoint for real-time inference
- Dockerized deployment (portable and reproducible)
- **GenAI-powered anomaly explanations**
- Retrieval-Augmented Generation (RAG) over operational documentation (runbooks, incident reports)
- Structured JSON explanations suitable for downstream systems

---

## How It Works
1. **Input:** Ordered list of numeric values  
2. **Features:** Rolling mean and standard deviation (after warm-up)  
3. **Scoring:** Isolation Forest generates anomaly scores and flags  
4. **Output:** Warm-up count, aligned anomaly flags, aligned scores

---

## GenAI Explanation (Operational Intelligence)

In addition to detecting anomalies, the API can generate **human-readable, structured explanations** describing anomalous behavior.

### How Explanations Work
1. Relevant operational documents (e.g., runbooks, past incident reports) are indexed using:
   - Sentence Transformers
   - FAISS vector search
2. At request time:
   - Relevant context is retrieved (RAG)
   - A Large Language Model (LLM) generates a **strict JSON explanation**
3. The response is parsed server-side to ensure **valid structured output**

### Explanation Includes
- Root causes
- Operational impact
- Business impact
- Recommended actions
- Assumptions
- Uncertainty
- Source documents used

---

## API

### `POST /predict`
Detect anomalies from an ordered list of time-series values.

#### Request Body
```json
{
  "values": [0.13, 0.134, 0.132, 2.34, 0.133]
}
```
### `POST /explain-anomaly`
Generate a structured GenAI explanation for detected anomalies.

#### Request Body
```json
{
  "anomaly_output": {
    "anomalies": [5],
    "scores": [0.95],
    "mean": 42.3
  }
}
