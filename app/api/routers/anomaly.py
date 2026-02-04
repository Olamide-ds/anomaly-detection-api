from typing import List
from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.anomaly.detector import predict_anomalies

router = APIRouter(prefix="/anomaly", tags=["Anomaly Detection"])

class PredictRequest(BaseModel):
    values: List[float] = Field(..., description="Ordered time-series values")

@router.post("")
def run_anomaly(req: PredictRequest):
    return predict_anomalies(req.values)
