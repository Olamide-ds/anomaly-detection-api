from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.inference import predict_anomalies

app = FastAPI(title="Anomaly Detection API", version="1.0.0")

class PredictRequest(BaseModel):
    values: List[float] = Field(..., description="Ordered time-series values")

@app.get("/")
def root():
    return {"status": "ok", "message": "Anomaly Detection API is running"}

@app.post("/predict")
def predict(req: PredictRequest):
    return predict_anomalies(req.values)
