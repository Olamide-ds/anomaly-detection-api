from fastapi import FastAPI
from app.api.routers import anomaly, explain

app = FastAPI(
    title="Operational Intelligence API",
    version="1.0.0"
)

@app.get("/", include_in_schema=False)
@app.head("/", include_in_schema=False)
def root():
    return {"status": "ok"}

app.include_router(anomaly.router)
app.include_router(explain.router)


