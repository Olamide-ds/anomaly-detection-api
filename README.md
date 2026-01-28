# Anomaly Detection API (Time-Series)

## Overview
A production-ready anomaly detection system for time-series data using rolling statistical features and an Isolation Forest model. The system exposes predictions through a FastAPI service and is containerized with Docker.

## Why This Project?
Monitoring systems generate continuous streams of metrics such as CPU usage, latency, or throughput. Detecting abnormal behavior in real time without labeled data is difficult. This project demonstrates how unsupervised machine learning can be deployed as a reliable, production-ready service.

## Key Features
- Rolling statistical feature engineering (mean & standard deviation)
- Unsupervised anomaly detection using Isolation Forest
- Proper warm-up handling to prevent data leakage
- REST API for real-time inference
- Dockerized for portability and deployment

## System Architecture
Client → FastAPI → Feature Engineering → Isolation Forest → JSON Response

## API Usage

### POST /predict

Send an ordered list of time-series values to detect anomalies.

**Request**
```json
{
  "values": [0.13, 0.134, 0.132, 2.34, 0.133]
}
