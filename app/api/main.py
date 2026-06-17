from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.schemas import (
    TelemetryRequest,
    PredictionResponse
)

from app.services.prediction_service import (
    PredictionService
)

from app.api.events import (
    startup_event,
    shutdown_event
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    startup_event()

    yield

    shutdown_event()


app = FastAPI(
    title="Fleet Anomaly Detection API",
    description="Real-time fleet telemetry anomaly detection service",
    version="1.0.0",
    lifespan=lifespan
)

prediction_service = PredictionService()


@app.get("/")
def health_check():

    return {

        "status": "healthy",

        "service": "fleet-anomaly-api",

        "version": "1.0.0"
    }


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(
        request: TelemetryRequest
):

    return prediction_service.predict(
        request.model_dump()
    )