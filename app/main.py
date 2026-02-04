from fastapi import FastAPI
from app.api.routers import anomaly, explain

app = FastAPI(
    title="Operational Intelligence API",
    version="1.0.0"
)

app.include_router(anomaly.router)
app.include_router(explain.router)


