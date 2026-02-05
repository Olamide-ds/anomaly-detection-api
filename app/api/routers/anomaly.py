from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.anomaly.detector import predict_anomalies

router = APIRouter(
    prefix="/anomaly",
    tags=["Anomaly"]
)

class PredictRequest(BaseModel):
    values: List[float]

@router.post("/predict")
def predict(req: PredictRequest):
    return predict_anomalies(req.values)

